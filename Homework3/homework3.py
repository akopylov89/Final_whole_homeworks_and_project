#  -*- coding: UTF-8 -*-
import argparse, smtplib
from email.message import Message
from email.header import Header
parser = argparse.ArgumentParser(description='Script to send e-mail')
parser.add_argument('--sender', '-s', type=str, default='lets.python2015@gmail.com', help='sender\'s e-mail')
parser.add_argument('--receiver', '-r', type=str, default='cilicium_2@mail.ru', help='receiver\'s e-mail')
parser.add_argument('--subject', '-b', type=str, default='Homework3. AKopylov', help='message subject')
parser.add_argument('--text', '-t', type=str, nargs='*', default='', help='message text')
parser.add_argument('--smtphost', '-o', type=str, default='smtp.gmail.com', help='SMTP server')
parser.add_argument('--smtpport', '-p', type=int, default=587, help='SMTP port')
args_parsed = parser.parse_args()
args_parsed = vars(args_parsed)
args_parsed['text'] = 'Homework3. AKopylov'.join(args_parsed['text'])
msg = Message()
msg.set_charset('utf-8')
h = Header(args_parsed['subject'], 'utf-8')
msg['Subject'] = h
msg.set_payload(args_parsed['text'].encode('base64'))
smtp_obj = smtplib.SMTP(args_parsed['smtphost'], args_parsed['smtpport'])
smtp_obj.starttls()
smtp_obj.login('lets.python2015@gmail.com', 'nmKoAO1gFpGr7Kc')
smtp_obj.sendmail(args_parsed['sender'], args_parsed['receiver'], msg.as_string())
smtp_obj.quit()