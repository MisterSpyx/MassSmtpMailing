import base64
import datetime
import glob
import os
import random
import smtplib
import string
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid
from multiprocessing.dummy import Pool
from random import choice

try:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
except:
    pass


# coding is an art https://youtu.be/Mptdcx36qZU?list=RDMptdcx36qZU
# i provide this part of art as a  project for bypassing spam filters when ever you have text to send it to a list of all ur friends / clients / buyers
#
def banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = '''        ..--""|
       |     |
       | .---'
 (\-.--| |---------.
/ \) \ | |          \
|:.  | | |           |
|:.  | |o|           |
|:.  | `"`           |
|:.  |_ __  __ _  __ /
`""""`""|=`|"""""""`
        |=_|
 Moetaz |= |Brayek'''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)


def send(emails):
    emails = emails.replace("\n", "").replace("\t", "")
    try:
        smtp = random.choice(open('config/Smtp.txt').readlines())
        host, port, user, pas = smtp.split("|")
    except:
        print("your smtp information is bad should be user|pass|host|port")
    ######################  this section is for Name Randomizer ###############################
    FromName = random.choice(open('config/Name.txt').readlines())
    FromName_1 = FromName
    FromName_1 = FromName_1.replace('##random_string##',
                                    ''.join(random.sample(string.ascii_lowercase + string.digits, 7)))
    FromName_1 = FromName_1.replace('##time##', datetime.datetime.now().strftime('%H:%M:%S'))
    FromName_1 = FromName_1.replace('##date##', datetime.datetime.now().strftime('%Y-%m-%d'))
    FromName_1 = FromName_1.replace('##date&time##', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    FromName_1 = FromName_1.replace('##random_number##', str(random.randint(0, 9999999)))
    message_bytes = FromName_1.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    FromName = base64_message
    ######################  this section is for Subject Randomizer ###############################
    Subject = random.choice(open('config/Subject.txt').readlines())
    r_subject = Subject.replace('##random_string##', ''.join(random.sample(string.ascii_lowercase + string.digits, 7)))
    r_subject = r_subject.replace('##time##', datetime.datetime.now().strftime('%H:%M:%S'))
    r_subject = r_subject.replace('##date##', datetime.datetime.now().strftime('%Y-%m-%d'))
    r_subject = r_subject.replace('##date&time##', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    r_subject = r_subject.replace('##random_number##', str(random.randint(0, 9999999)))
    message_bytes = r_subject.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    r_subject = base64_message
    Subject = r_subject
    ######################  this section is for Name Randomizer ###############################
    r_domain = [
        'com', 'co.us', 'net', 'org', 'xyz', 'ac', 'ad', 'au', 'gov', 'edu', 'int', 'us', 'ca', 'online',
        'to', 'co.za', 'world', 'vip', 'uk.com', 'team', 'se', 'pizza', 'one', 'org.nz', 'nu', 'guide', 'email', 'cc',
        'io',
        'me']
    for domain in r_domain:
        random_domain = choice(domain)
    FromEmail1 = random.choice(open('config/FromEmails.txt').readlines())
    base64_message = base64_bytes.decode('ascii')
    FromName_1 = base64_message
    FromEmail_1 = FromEmail1
    FromEmail_1 = FromEmail_1.replace('##random_string##',
                                      ''.join(random.sample(string.ascii_lowercase + string.digits, 7)))
    FromEmail_1 = FromEmail_1.replace('##random_domain##', random_domain)
    FromEmail_1 = FromEmail_1.replace('##random_number##', str(random.randint(0, 9999999)))
    e = '<'
    r = '>'
    FromAdd_1 = '=?UTF-8?B?{}?='.format(FromName_1) + e + FromEmail_1 + r
    # use FromAdd_1 when you have a private smtp :D
    ######################  this section is for Letter Randomizer ###############################
    all_letters = glob.glob('config/letter/*.html')
    _letter = choice(all_letters)
    with open(_letter, 'r', encoding='utf-8') as (f):
        r_letter = f.read()
        r_letter = r_letter.replace('##email##', emails)
        r_letter = r_letter.replace('##random_string##',
                                    ''.join(random.sample(string.ascii_lowercase + string.digits, 7)))
        r_letter = r_letter.replace('##time##', datetime.datetime.now().strftime('%H:%M:%S'))
        r_letter = r_letter.replace('##date##', datetime.datetime.now().strftime('%Y-%m-%d'))
        r_letter = r_letter.replace('##date&time##', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        letter = r_letter
    ###################### prority ######################
    if str(x_priority.lower()) == 'low':
        imp = 'low'
    else:
        imp = 'high'

    ###################### domain ######################
    li = [
        'yahoo.com', 'aol.com', 'att.com',
        'cox.net', 'rr.com', 'aim.com', 'gmail.com',
        'inbox.com', 'mail.com', 'yandex.com', 'zoho.com',
        'outlook.com', 'protonmail.com', 'tutanota.com', 'icloud.com',
        '123mail.cl', '123mail.cl', 'amuromail.com', 'arcor.de', 'assamesemail.com',
        'bootmail.com', 'boxemail.com', 'boxemail.com', 'boxemail.com', 'e-mail.ru', 'edmail.com',
        'hushmail.com', 'rickymail.com', 'rickymail.com', 'comcast.net', 'earthlink.net', 'edge.net', 'ehmail.com']
    for d in li:
        do = choice(li)
    try:
        mailserver = smtplib.SMTP(host, port)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(user, pas)
        msg = MIMEMultipart()
        msg.attach(MIMEText(letter, 'html', 'utf-8'))
        msg['From'] = FromName
        msg['To'] = emails
        msg['Subject'] = '=?UTF-8?B?{}?='.format(Subject)
        msg['Importance'] = imp
        msg['Message-ID'] = make_msgid(domain=do)
        msg['X-PHISHTEST'] = 'KnowBe4'
        msg['Content-type'] = 'text/html; charset=utf-8'
        msg['MIME-Version'] = '1.0'
        msg['Content-Transfer-Encoding'] = 'base64'
        mailserver.sendmail(user, emails, msg.as_string())
        mailserver.quit()
        print(' Sent! {0} '.format(emails))
    except smtplib.SMTPException as ex:
        print('  \n\x1b[101m[-] {}'.format(str(ex)))
    # for some security policy , hosts limite requests number but always there's a solution :D
    time.sleep(int(dealytime))


# i set it to high in default mode so u can change it if you have ever had a problem
x_priority = "high"
if __name__ == '__main__':
    banner()
    dealytime = input('\n  [ + ] Enter Deally Between  Msgs Frm 0 - 9  : ')
    emails = input('\n  [ + ] Your Email List ! : ')
    with open(emails, 'r', errors="ignore") as (f):
        emails = f.read().split('\n')
        ThreadPool = Pool(5)
        Threads = ThreadPool.map(send, emails)
