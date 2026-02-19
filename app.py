import smtplib
from email.message import EmailMessage
import mimetypes

#Definição de dados de envio

remetente = "******************"
destinatario = "************"

assunto = "Armazenamento Crítico"
mensagem = """
Foi verificado que seu armazenamneto está acima dos 90%
"""

senha = "********************"
anexo = "./Alerta_Armazenamento_Critico.pdf"

#Criação do email

msg = EmailMessage()

msg['From'] = remetente
msg['To'] = destinatario
msg['Subject'] = assunto
msg.set_content(mensagem)

#Anexo que vai ao e-mail

mime_types, _ = mimetypes.guess_type(anexo)
mime_types,mime_subtypes = mime_types.split('/')

with open(anexo,'rb') as arquivo:
    msg.add_attachment(arquivo.read(),maintype=mime_types,subtype=mime_subtypes,
                       filename = anexo)

#envio do email

with smtplib.SMTP_SSL("smtp.gmail.com",465) as email:
    email.login(remetente,senha)
    email.send_message(msg)

print("enviado....")
    