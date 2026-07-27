import os

import requests
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv(override=True)


def deliver_telegram_message(message: str) -> str:
    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not telegram_bot_token or not telegram_chat_id:
        return "Telegram notification skipped: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is not set."

    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {"chat_id": telegram_chat_id, "text": message}
    response = requests.post(url, data=payload, timeout=30)
    response.raise_for_status()
    return f"Telegram message sent: {response.json().get('ok', False)}"


@tool("Send Telegram Message")
def send_telegram_message(message: str) -> str:
    """
    Send a Telegram message to the studio lead.

    Use this after deploying a game to share the live here.now testing URL.

    Args:
        message: The message to send via Telegram.

    Returns:
        A string indicating whether the Telegram message was sent.
    """
    return deliver_telegram_message(message)
