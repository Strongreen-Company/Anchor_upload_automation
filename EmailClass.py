import datetime
import os
import dotenv
import boto3
from botocore.exceptions import ClientError
import logging

logging.basicConfig(
    format="%(asctime)s -%(levelname)s  -  %(message)s ",
    encoding="utf-8",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filename="log/anchor/system_anchor.log",
    filemode="a",
)

dotenv.load_dotenv()


class email_sender:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.sender = os.getenv("AUTOMACAO_EMAIL")
        self.receiver = os.getenv("MAIN_EMAIL")
        self.subject = "automação da publicação no Anchor"
        self.message = f"Olá! o episódio do dia { self.date.now().day } foi publicado com sucesso."

    def send_sucesso(self):
        data = {
            "from": {"email": self.sender},
            "to": [
                os.getenv("EMAIL"),
                os.getenv("SECUNDARY_EMAIL"),
            ],
            "subject": self.subject,
            "html": f"<strong>{self.message}</strong>",
            "category": "automação",
        }
        self.send_api_AWS_SES(data)

    def send_falha(self):
        self.receiver = (
            [
                os.getenv("EMAIL"),
                os.getenv("SECUNDARY_EMAIL"),
            ]
            if os.getenv("SECUNDARY_EMAIL") is not None
            else [{"email": os.getenv("EMAIL")}]
        )
        self.replace_mensage("foi publicado com sucesso", "não foi publicado")
        data = {
            "from": self.sender,
            "to": self.receiver,
            "subject": self.subject,
            "html": f"<strong>{self.message}</strong>",
            "category": "automação",
        }
        self.send_api_AWS_SES(data)

    def replace_mensage(self, oldStr, newStr):
        if self.message is not None:
            self.message = self.message.replace(oldStr, newStr)

    def send_api_AWS_SES(self, data):
        res = boto3.client(
            "ses",
            region_name="us-east-1",
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        )
        try:
            res.send_email(
                Destination={
                    "ToAddresses": data["to"],
                },
                Message={
                    "Body": {
                        "Html": {
                            "Charset": "UTF-8",
                            "Data": data["html"],
                        },
                        "Text": {
                            "Charset": "UTF-8",
                            "Data": data["html"],
                        },
                    },
                    "Subject": {
                        "Charset": "UTF-8",
                        "Data": data["subject"],
                    },
                },
                Source=data["from"],
            )
        except ClientError as e:
            logging.exception(
                "esse é o erro ocorrido: %s", e.response["Error"]["Message"]
            )
            print(e.response["Error"]["Message"])
