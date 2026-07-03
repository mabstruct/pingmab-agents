import os
import sys

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def send_basic_email(
    sender: str,
    recipient: str,
    subject: str,
    body_text: str,
    region: str,
) -> str:
    ses = boto3.client("ses", region_name=region)

    response = ses.send_email(
        Source=sender,
        Destination={
            "ToAddresses": [recipient],
        },
        Message={
            "Subject": {
                "Data": subject,
                "Charset": "UTF-8",
            },
            "Body": {
                "Text": {
                    "Data": body_text,
                    "Charset": "UTF-8",
                },
            },
        },
    )

    return response["MessageId"]


def main() -> int:
    load_dotenv()

    region = require_env("AWS_REGION")
    sender = require_env("SES_FROM_EMAIL")
    recipient = require_env("SES_TO_EMAIL")

    subject = "Test email from AWS SES"
    body_text = (
        "Hello,\n\n"
        "This is a basic test email sent from Python via Amazon SES.\n\n"
        "Regards,\n"
        "SES test client"
    )

    try:
        message_id = send_basic_email(
            sender=sender,
            recipient=recipient,
            subject=subject,
            body_text=body_text,
            region=region,
        )
    except ClientError as error:
        print("Failed to send email.")
        print(error.response["Error"]["Code"])
        print(error.response["Error"]["Message"])
        return 1

    print(f"Email sent. Message ID: {message_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())