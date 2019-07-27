import imaplib
import datetime
imap = imaplib.IMAP4_SSL('outlook.office365.com')
imap.login('kalphageek@outlook.com','***11211@')
imap.select('inbox')
# - 전부 가져오기
# result, data = imap.uid('search', None, 'ALL')
# - kalphageek@outlook.com가 보낸 메일 가져오기
# result, data = imap.uid('search', None, '(HEADER From "kalphageek@outlook.com")')
# - 어제날짜 이후 가져오기
# date = (datetime.date.today() - datetime.timedelta(1)).strftime("%Y-%m-%d")
# result, data = imap.uid('search', None, '(SENTSINCE {})'.format(date))
result, data = imap.uid('fetch', '7', '(RFC822)')
email_message = email.message_from_string(data[0][1].decode('utf-8'))
msg = email.message_from_string(data[0][1].decode('utf-8'))
to = msg['To']
# --> ('', 'bi8i@hotmail.com')#
# msg['From'] #--> encode된 형태
from = email.utils.parseaddr(msg['From'])

if msg.is_multipart():
    for p in msg.get_payload():
        print(p.get_payload())

imap.uid('store','7', '+FLAGS', '(\\Deleted)') #uid=7 삭제