import imaplib
import pprint
import email
import time
from email.header import decode_header

imap_host = input('input imap host of your mailbox:\t')
imap_user = input('input your email adress:\t')
imap_pass = input('input a paswword to your email:\t')
FROM = input('enter the e-mail address of the sender whose e-mails you want to delete:\t')

imap = imaplib.IMAP4_SSL(imap_host)
imap.login(imap_user, imap_pass)
imap.select()
tmp, data = imap.search(None, f'FROM {FROM}')
f = open('./mail_log.txt', 'a')
f.write(time.strftime("%D %H:%M:%S", time.localtime()))
f.write('\n------------------------\n')
for num in data[0].split():
    tmp, data = imap.fetch(num, '(RFC822)')

    for response in data:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):    
                subject = subject.decode()
            
            f.write(f'{subject}\n')
    
    imap.store(num, "+FLAGS", "\\Deleted")
    
imap.expunge()
imap.close()
imap.logout()

f.close()

