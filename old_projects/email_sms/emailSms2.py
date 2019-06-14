#!/usr/bin/python3


import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com',use_uid=True)
#passwd = input('Enter password: ')
#imapObj.login('yaaanhue@gmail.com',passwd)
imapObj.login('yaaanhue@gmail.com','gxnxlykbbkblsxoq')
select_info = imapObj.select_folder('INBOX')
print('%d messages in INBOX' % select_info[b'EXISTS'])
uids = imapObj.search(['SINCE','01-Jan-2019'])

rawMessages = imapObj.fetch(uids, [b'BODY[]','FLAGS'])

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[uids[b'BODY[]'])
print(message.get_subject())

print(message.get_addresses('cc'))



'''
import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com',use_uid=True)
passwd = input('Enter password: ')
imapObj.login('yaaanhue@gmail.com',passwd)
select_info = imapObj.select_folder('INBOX')
print('%d messages in INBOX' % select_info[b'EXISTS'])
messages = imapObj.search(['SINCE','01-Jan-2019'])
print('%d messages since selcted date' % len(messages))

'''
'''
for msgid, data in imapObj.fetch(messages, ['ENVELOPE']).items():
	envelope = data[b'ENVELOPE']
	print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))
'''




