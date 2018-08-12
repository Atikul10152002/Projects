import smtplib
from email.mime.text import MIMEText

myEmail = 'resatikul@gmail.com'
sendEmail = 'atikul10152002@gmail.com'
# msg = "THIS IS WORKING"
msg = MIMEText("THIS IS WORKING")
msg['subject'] = 'Our family reunion'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myEmail, 'Islam2002@')
server.sendmail(myEmail, [sendEmail], msg.as_string())
server.quit()