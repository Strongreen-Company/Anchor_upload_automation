import datetime

import os
# from dotenv import load_dotenv


# load_dotenv()


class email_sender:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.sender = os.getenv("EMAIL")
        self.receiver = os.getenv("SECONDARY_EMAIL")
        self.subject = "automação da publicação do epsiodeo no Anchor"
        self.message = f"Olá! o episódio do dia { self.date.now().day } foi publicado com sucesso "

    def send_sucesso(self):
        print("de: ", self.sender)
        print("para: ", self.receiver)
        message = mail(
            from_email=self.sender,
            to_emails=self.receiver,
            subject=self.subject,
            html_content=f"<strong>{self.message}</strong>",
        )
        try:
            sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
            sg.send(message)
        except Exception as e:
            print(e)

    def send_falha(self, list_email=None):
        self.receiver = [(os.getenv('MAIN_EMAIL')), (os.getenv('SECONDARY_EMAIL'))]
        self.replace_mensage("foi publicado com sucesso", "não foi publicado")
        print("de: ", self.sender)
        print("para: ", self.receiver)
        print("assunto: ", self.subject)
        print("mensagem: ", self.message)
        print("data: ", self.date)
        print("email enviado")

    def replace_mensage(self, oldStr, newStr):
        if self.message is not None:
            self.message = self.message.replace(oldStr, newStr)


lucas = email_sender()
print(lucas.send_sucesso())
