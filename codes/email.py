import os
import smtplib
import cred as cd
from email.mime.multipart import MIMEMultipart


Email_address=cd.email
Email_PAss=cd.passow

msg=EmailMessage()
msg['Subject']="grab dinner this weekend"
msg['From']=Email_address
msg['To']='shivamsingh8461@gmail.com'
msg.set_content('email automation using new class')

with smtplib.SMTP_SSL('smtp.gmail.com',455)as smtp:
    smtp.login(Email_address,Email_PAss)
    smtp.send_message(msg)
