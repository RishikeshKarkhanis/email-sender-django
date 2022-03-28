from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
from django.shortcuts import redirect, render

def index(request):
    return render(request, "index.html")

def send(request):

    msg = MIMEMultipart()
    msg['Subject'] = f'{request.POST["subject"]}'
    msg['From'] = 'rishikeshkarkhanis0101@gmail.com'
    msg['To'] = f'{request.POST["email"]}'

    text = MIMEText(f'{request.POST["body"]}')

    msg.attach(text)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)        
    server.login("rishikeshkarkhanis0101@gmail.com", "ajmzippuoknpingm")

    server.sendmail("rishikeshkarkhanis0101@gmail.com", request.POST["email"], msg.as_string())

    server.quit()

    return redirect("/")