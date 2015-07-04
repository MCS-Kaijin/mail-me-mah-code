# coding: utf-8

import os
import re

from smtplib import SMTP

sender = raw_input("Your email: ")
sender = re.match((r'(?P<usr>[\w]+)@(?P<host>.+)'), sender)
password = raw_input("Password: ")
recipient = raw_input("To: ")

folder = raw_input("Folder containing project: ")
mstr = ''
for filename in os.listdir(folder):
        fl = open(folder+'/'+filename, 'r')
        mstr = mstr+fl.read()+'\n\n----\n\n'

msg = "From: {}@{}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}".format(sender.group("usr"), sender.group("host"), recipient, folder, mstr)

smtp = SMTP("smtp.gmail.com")
smtp.starttls()
smtp.login(sender.group("usr"),password)
smtp.sendmail(sender.group("usr")+"@"+sender.group("host"),recipient,msg)
smtp.quit()
