import smtplib
from email.message import EmailMessage
import ssl

def MailToCounseller(data):
    sender = 'greviencevvit@gmail.com'
    password = 'otfk agzp pvjr hiec '
    receiver = '21bq1a4230@vvit.net'

    subject = 'Complaint by {} '.format(data['name'])
    
    body = """
        {} is facing a/an {} issue . here is their discription about it. {}
    """.format(data['name'],data['type'],data['grevience'])
    mail = EmailMessage()
    mail['From'] = sender
    mail['To'] = receiver
    mail['subject'] = subject
    mail.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,mail.as_string())