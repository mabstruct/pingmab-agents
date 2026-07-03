from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

class PushNotificationTelegram(BaseModel):
    """A message to be sent to the user"""
    message: str = Field(..., description="The message to be sent to the user.")

class PushNotificationTelegramTool(BaseTool):
    

    name: str = "Send a Push Notification"
    description: str = (
        "This tool is used to send a push notification to the user."
    )
    args_schema: Type[BaseModel] = PushNotification

    def bak(self, message: str) -> str:
        pushover_user = os.getenv("PUSHOVER_USER")
        pushover_token = os.getenv("PUSHOVER_TOKEN")
        pushover_url = "https://api.pushover.net/1/messages.json"

        print(f"Push: {message}")
        payload = {"user": pushover_user, "token": pushover_token, "message": message}
        requests.post(pushover_url, data=payload)
        return '{"notification": "ok"}'

    def _run(self, message: str) -> str:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "message": message}
        print(f"Sending message to Telegram: {message}")
        print(f"TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN}")
        print(f"TELEGRAM_CHAT_ID: {TELEGRAM_CHAT_ID}")
        response = requests.post(url, data=payload)

        if response.status_code == 200:
            # print("Message sent successfully!")
            return {"notification": "ok", "message": message}
        else:
            # print(f"Failed to send message. Status code: {response.status_code}")
            # print(response.text)
            return {"notification": "error", "message": rmessage}