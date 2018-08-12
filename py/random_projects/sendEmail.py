import smtplib
from sys import argv
from email.mime.text import MIMEText
from getpass import getpass


myEmail = input("Your email: ")
myPass = str(getpass("Your password: "))
sendEmail = input("Recipient's email: ")

# Message
subject = input("Email Subject: ")
msg = MIMEText(input("Email Body: "))
msg['subject'] = subject

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myEmail, myPass)
server.sendmail(myEmail, [sendEmail], msg.as_string())
server.quit()