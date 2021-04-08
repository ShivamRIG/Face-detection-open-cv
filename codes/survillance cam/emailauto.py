import os
import smtplib
import imghdr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import time

def email_send(img):
    Email_address= os.environ.get('EMAIL_USER')
    Email_PASS='qxxbwobcequbaoqo'


    msg=MIMEMultipart()
    msg['Subject']="Security issue"
    msg['From']=Email_address
    msg['To']='shivamsingh8461@outlook.com'
    filename = img
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

# Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

# Add attachment to message and convert message to string
    msg.attach(part)
    with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:     
        smtp.login(Email_address,Email_PASS)
        time.sleep(2)
        smtp.send_message(msg)
        print("email send")