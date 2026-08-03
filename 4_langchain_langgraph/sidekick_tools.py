"""Tools for the Sidekick: a mix of MCP servers, ready-made LangChain tools and our own."""

import asyncio
import os
from contextlib import AsyncExitStack

import requests
import wikipedia
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_tavily._utilities import TavilySearchAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools

load_dotenv(override=True)

# Getting the Telegram bot token and chat ID from environment variables
# You can also replace these with your actual values directly

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "UNKNOWN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "UNKNOWN")

# Wikimedia rejects the wikipedia library's default user agent, so identify ourselves properly
wikipedia.set_user_agent("agentic-track-course (https://edwarddonner.com)")

search = TavilySearch(api_wrapper=TavilySearchAPIWrapper())
wikipedia_lookup = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())


def send_telegram_message(text):
    if not TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN == "UNKNOWN":
        return {"status": "error", "message": "TELEGRAM_BOT_TOKEN is not set"}
    if not TELEGRAM_CHAT_ID or TELEGRAM_CHAT_ID == "UNKNOWN":
        return {"status": "error", "message": "TELEGRAM_CHAT_ID is not set"}

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return {"status": "success", "message": text}
    return {"status": "error", "message": response.text}


@tool
def send_push_notification(text: str) -> str:
    """Send a short push notification to the user's phone."""
    result = send_telegram_message(text)
    if result["status"] != "success":
        raise RuntimeError(f"Telegram notification failed: {result['message']}")
    return "Notification sent"


@tool
def request_human_help(instructions: str) -> str:
    """Ask the user to do something in the browser window that you cannot do yourself,
    such as logging in to a site, passing a captcha, or approving two-factor authentication.
    Explain exactly what you need them to do. The run pauses until they have done it."""
    return "The user says it is done. Continue with the task."


def mcp_connections(sandbox: str) -> dict:
    """The MCP servers the Sidekick uses: a headed browser and a sandbox filesystem."""
    return {
        "playwright": {
            "transport": "stdio",
            "command": "npx",
            "args": ["@playwright/mcp@latest", "--isolated"],
        },
        "filesystem": {
            "transport": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", sandbox],
        },
    }


class McpSessions:
    """Holds persistent MCP sessions open so the browser keeps its state between tool calls.

    The stdio transport must be opened and closed from the same asyncio task, so one
    background task owns the sessions: it opens them, waits, and unwinds them when stop()
    is called. Stopping shuts down the servers, and you will see the browser close.
    """

    def __init__(self, connections: dict):
        self.connections = connections
        self.tools = []
        self._ready = asyncio.Event()
        self._stop = asyncio.Event()
        self._task = None

    async def _run(self):
        client = MultiServerMCPClient(self.connections)
        async with AsyncExitStack() as stack:
            for name in self.connections:
                session = await stack.enter_async_context(client.session(name))
                self.tools += await load_mcp_tools(session, server_name=name)
            self._ready.set()
            await self._stop.wait()

    async def start(self) -> list:
        self._task = asyncio.create_task(self._run())
        ready = asyncio.create_task(self._ready.wait())
        await asyncio.wait([ready, self._task], return_when=asyncio.FIRST_COMPLETED)
        ready.cancel()
        if self._task.done():
            self._task.result()  # the servers failed to start; raise the real error
        return self.tools

    def stop(self):
        self._stop.set()


async def get_all_tools(sandbox: str):
    """Return the full tool list (our tools plus the MCP server tools) and the session holder."""
    sessions = McpSessions(mcp_connections(sandbox))
    mcp_tools = await sessions.start()
    our_tools = [search, send_push_notification, wikipedia_lookup, request_human_help]
    return our_tools + mcp_tools, sessions
