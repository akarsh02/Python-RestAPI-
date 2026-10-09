import json
import os
file_path = "src/data/products.json"
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig,MessageType

def get_all_products():
   with open(file_path, "r") as p:
    return json.load(p)



def creat_product(product):
  with open(file_path,"w") as p:
    return json.dump(product,p)



async def simple_send(email: str, count: int):
    html = f"<p>Hi, thanks for using Fastapi-Mail.</p><p>You ordered {count} item(s).</p>"

    mail_username = os.getenv("MAIL_USERNAME")
    mail_password = os.getenv("MAIL_PASSWORD")
    mail_from = os.getenv("MAIL_FROM")
    if not mail_username or not mail_password or not mail_from:
        raise RuntimeError("MAIL_USERNAME, MAIL_PASSWORD, and MAIL_FROM must be configured")

    email_conf = ConnectionConfig(
        MAIL_USERNAME=mail_username,
        MAIL_PASSWORD=mail_password,
        MAIL_FROM=mail_from,
        MAIL_PORT=587,
        MAIL_SERVER="smtp.gmail.com",
        MAIL_FROM_NAME="Fastapi Mail",
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True,
    )

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=[email],
        body=html,
        subtype=MessageType.html)

    fm = FastMail(email_conf)
    await fm.send_message(message)