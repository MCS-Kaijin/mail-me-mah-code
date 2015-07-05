import os
import re
import zipfile
import tempfile

from smtplib import SMTP

from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = raw_input("Your email: ")
sender = re.match((r'(?P<usr>[\w]+)@(?P<host>.+)'), sender)
password = raw_input("Password: ")
recipient = raw_input("To: ")

folder = raw_input("Folder containing project: ")
attach = zipfile.ZipFile('../code.zip', 'w')
mstr = ''
for root, dirs, files in os.walk(folder):
	for fl in files:
		attach.write(os.path.join(root, fl))
attach = open("../code.zip","r")

msg = MIMEMultipart()
msg['From'] = sender.group("usr")+"@"+sender.group("host")
msg['To'] = recipient
msg['Subject'] = folder
msg.attach(MIMEText(mstr,'plain'))

part = MIMEBase('application', 'zip')
part.set_payload(attach.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="../code.zip"')

msg.attach(part)

smtp = SMTP("smtp."+sender.group("host"))
smtp.starttls()
smtp.login(sender.group("usr"),password)
smtp.sendmail(sender.group("usr")+"@"+sender.group("host"),recipient,msg.as_string())
smtp.quit()
