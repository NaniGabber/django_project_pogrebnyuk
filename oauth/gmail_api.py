import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from django.core.mail.backends.base import BaseEmailBackend


class GmailOAuth2Backend(BaseEmailBackend):
    def send_messages(self, email_messages):
        for msg in email_messages:
            send_gmail_api(to=", ".join(msg.to), subject=msg.subject, body=msg.body)
        return len(email_messages)


def send_gmail_api(to, subject, body):
    creds = Credentials(
        None,
        refresh_token=os.getenv("GMAIL_REFRESH_TOKEN"),
        client_id=os.getenv("GMAIL_CLIENT_ID"),
        client_secret=os.getenv("GMAIL_CLIENT_SECRET"),
        token_uri="https://oauth2.googleapis.com/token",
    )

    service = build("gmail", "v1", credentials=creds)
    message = MIMEText(body)
    message["to"] = to
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    return service.users().messages().send(userId="me", body={"raw": raw}).execute()
