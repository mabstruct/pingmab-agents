from crewai.tools import tool
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

@tool("Send Push Notification")
def send_push_notification(message: str) -> str:
    """
    Use this tool to send a push notification to the user.
    Args:
        message: The message to be sent as a push notification to the user.
    Returns:
        A string indicating the status of the push notification.
    """
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    response = requests.post(url, data=payload)
    return response.json()


