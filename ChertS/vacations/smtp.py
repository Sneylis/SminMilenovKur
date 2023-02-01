import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .models import VacationFile

def EMessage (message):
    server = smtplib.SMTP(host='127.0.0.1',port=9999)
    msg = MIMEMultipart()
    password = ""
    msg['From'] = "SmtpSbit@gmail.com"
    msg['To'] = "sneylees228@gmai.com"
    msg.attach(MIMEText(message, 'plain'))
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()



