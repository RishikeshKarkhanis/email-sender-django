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
    msg['From'] = 'your-email-here'
    msg['To'] = f'{request.POST["email"]}'

    text = MIMEText(f'{request.POST["body"]}')

    msg.attach(text)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)        
    server.login("your-email-here", "your-password-here")

    server.sendmail("your-email-here", request.POST["email"], msg.as_string())

    server.quit()

    return redirect("/")
