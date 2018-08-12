import smtplib
from sys import argv
from email.mime.text import MIMEText



myEmail = 'resatikul@gmail.com'
sendEmail = argv[1]
# msg = "THIS IS WORKING"
msg = MIMEText(argv[3])
msg['subject'] = argv[2]

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myEmail, 'Islam2002@')
server.sendmail(myEmail, [sendEmail], msg.as_string())
server.quit()