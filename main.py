# coding: utf-8

import os
import re

from smtplib import SMTP

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

sender = raw_input("Your email: ")
sender = re.match((r'(?P<usr>[\w]+)@(?P<host>.+)'), sender)
password = raw_input("Password: ")
recipient = raw_input("To: ")

folder = raw_input("Folder containing project: ")
mstr = ''
for filename in os.listdir(folder):
        fl = open(folder+'/'+filename, 'r')
        mstr = mstr+fl.read()+'\n\n----\n\n'

msg = MIMEMultipart()
msg['From'] = sender.group("usr")+"@"+sender.group("host")
msg['To'] = recipient
msg['Subject'] = folder

smtp = SMTP("smtp.gmail.com")
smtp.starttls()
smtp.login(sender.group("usr"),password)
smtp.sendmail(sender.group("usr")+"@"+sender.group("host"),recipient,msg)
smtp.quit()
