import smtplib
import os
from email.message import Message
from pydantic import EmailStr
from dotenv import load_dotenv

load_dotenv()
def message(email:EmailStr,value):

    content = f"<p>The price of bitcoin has changed to {value} USD</p>"
    msg = Message()
    msg['subject'] = 'Price alert'
    msg['from'] = "yuriafonsocani@gmail.com"
    msg['to'] = email
    msg.add_header("content-type", "text/html")
    msg.set_payload(content)

    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(str(os.getenv("Email")),str(os.getenv("PASSWORD")))
    s.sendmail(msg['from'],msg['to'],msg.as_string())