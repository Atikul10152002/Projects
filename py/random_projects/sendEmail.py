import smtplib
from sys import argv
from email.mime.text import MIMEText
from getpass import getpass


# myEmail = 'resatikul'
myEmail = input("Your email: ")
# myPass = 'Islam2002@'
myPass = str(getpass("Your password: "))
sendEmail = str(input("Recipient's email: "))


# Message
if '@gmail.com' not in myEmail:
    myEmail += "@gmail.com"
if '@gmail.com' not in sendEmail:
    sendEmail += "@gmail.com"

subject = input("Email Subject: ")
msg = MIMEText(input("Email Body: "))
msg['subject'] = subject

server = smtplib.SMTP_SSL('smtp.gmail.com')
server.login(myEmail, myPass)
server.sendmail(myEmail, [sendEmail], msg.as_string())
server.quit()
