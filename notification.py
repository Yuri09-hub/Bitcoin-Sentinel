import smtplib
import os
from email.message import EmailMessage
from pydantic import EmailStr
from dotenv import load_dotenv

load_dotenv()
def message(email:EmailStr,value):
    msg = EmailMessage()

    msg['subject'] = 'Price alert'
    msg['from'] = email
    msg['to'] = ...

    msg.set_content(
        f'The price of bitcoin has changed to {value} USD'
    )

    server = smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    )

    server.login(
        f"{str(os.getenv("Email"))}",
        f"{str(os.getenv("PASSWORD"))}"
    )

    server.send_message(msg)

    server.quit()