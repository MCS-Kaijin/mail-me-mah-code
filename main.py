import os
import zipfile

from smtplib import SMTP

from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = raw_input('Your email: ').strip()
usr, _, host = sender.partition('@')
password = raw_input('Password: ').strip()
recipient = raw_input('To: (sender) ').strip() or sender

zip_file_path = os.path.expanduser('~/Documents/code.zip')
folder = raw_input('Folder containing project: ').strip()
with zipfile.ZipFile(zip_file_path, 'w') as attach:
    for root, dirs, files in os.walk(folder):
        for fl in files:
            attach.write(os.path.join(root, fl))

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = folder

part = MIMEBase('application', 'zip')
with open(zip_file_path, 'r') as attach:
    part.set_payload(attach.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',
                'attachment; filename="{}"'.format(filename))
msg.attach(part)

smtp = SMTP('smtp.' + host)
smtp.starttls()
smtp.login(usr, password)
smtp.sendmail(sender, recipient, msg.as_string())
smtp.quit()
print('Done.')
