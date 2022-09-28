import imaplib
from operator import truediv
import pprint
import email
import time
from email.header import decode_header
import pprint

emails = []

looper = True

while looper: 
	user = input('email: ')
	password = input('password: ')
	host = input('email host: ')
	emails.append(dict({'user': user, 'password': password,'host': host}))
	looper = input('add another email? (y for yes): ').lower() == 'y' 

for inbox in emails:
	imap_pass = emails[0]['password']
	imap_host = emails[0]['host']
	imap_user = emails[0]['user']
	# FROM = 'mailing@interia.pl'
	imap = imaplib.IMAP4_SSL(imap_host)
	imap.login(imap_user, imap_pass)
	imap.select()
	tmp, data = imap.search(None, 'ALL')
	for num in data[0].split():
		tmp, data = imap.fetch(num, '(RFC822)')
		msg = email.message_from_bytes(data[0][1])
		subject = decode_header(msg["Subject"])[0][0]
		if isinstance(subject, bytes):
			try:
				subject = subject.decode()
			except:
				subject = subject
		print(subject)
		input()
		
		# print('Message %s\n%s\n' % (num, data[0][1]))
		# imap.store(num, "+FLAGS", "\\Deleted")
		
	# imap.expunge()
	imap.close()
	imap.logout()

















# imap_pass = inbox.password
# 	imap_host = inbox.host
# 	imap_user = inbox.user
# 	# FROM = 'mailing@interia.pl'

# 	imap = imaplib.IMAP4_SSL(imap_host)
# 	imap.login(imap_user, imap_pass)
# 	imap.select()
# 	tmp, data = imap.search(None, f'FROM {FROM}')
# 	f = open('./mail_log.txt', 'a')
# 	f.write(time.strftime("%D %H:%M:%S", time.localtime()))
# 	f.write('\n------------------------\n')
# 	for num in data[0].split():
# 		tmp, data = imap.fetch(num, '(RFC822)')

# 		for response in data:
# 			if isinstance(response, tuple):
# 				msg = email.message_from_bytes(response[1])
# 				subject = decode_header(msg["Subject"])[0][0]
# 				if isinstance(subject, bytes):    
# 					subject = subject.decode()
				
# 				f.write(f'{subject}\n')
# 				print(subject)
		
# 		imap.store(num, "+FLAGS", "\\Deleted")
		
# 	imap.expunge()
# 	imap.close()
# 	imap.logout()

# 	f.close()

