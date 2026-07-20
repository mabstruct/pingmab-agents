from dotenv import load_dotenv
import requests
import os
import boto3
from botocore.exceptions import ClientError
import re
import os

load_dotenv(override=True)

aws_region = os.getenv("AWS_REGION", "eu-central-1")
aws_profile = os.getenv("AWS_PROFILE", "default")
EMAIL_SENDER = os.getenv("SES_FROM_EMAIL")
EMAIL_RECIPIENT = os.getenv("SES_TO_EMAIL")



def send_email(
    subject: str,
    body_html: str,
    body_text: str = None
    ) -> str:

    sender = EMAIL_SENDER
    recipient = EMAIL_RECIPIENT
    def html_to_basic_text(html: str,) -> str:
        text = re.sub(r"<br\s*/?>", "\n", html, flags=re.IGNORECASE)
        text = re.sub(r"</p\s*>", "\n\n", text, flags=re.IGNORECASE)
        text = re.sub(r"<[^>]+>", "", text)
        return text.strip()
    
    if body_text is None:
        body_text = html_to_basic_text(body_html)

    ses = boto3.client("ses", os.getenv("AWS_REGION"))
    response = ses.send_email(
        Source=EMAIL_SENDER,
        Destination={
            "ToAddresses": [os.getenv("SES_TO_EMAIL")],
        },
        Message={
            "Subject": {
                "Data": subject,
                "Charset": "UTF-8",
            },
            "Body": {
                "Text": {
                    "Data": html_to_basic_text(body_html),
                    "Charset": "UTF-8",
                },
                "Html": {
                    "Data": body_html,
                    "Charset": "UTF-8",
                },
            },
        },
    )


    
def send_test_email():
    subject = "Test mail from agent-tutorial"
    body_html = (
        "Hello,\n\n"
        "This is test mail from my agent-tutorial.\n\n"
        "Cheers,\n"
        "agent-tutorial-bot"
    )
    try:
        message_id = send_email(
            subject=subject,
            body_html=body_html
        )
    except ClientError as error:
        print("Failed to send email.")
        print(error.response["Error"]["Code"])
        print(error.response["Error"]["Message"])
        return 1

    print(f"Email sent. Message ID: {message_id}")
    return 0
            


if __name__ == "__main__":
    send_test_email()
