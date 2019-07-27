import smtplib
from email.message import EmailMessage


msg = EmailMessage()
msg['Subject'] = 'Python Mail Test ...'
msg['From'] = 'kalphageek@outlook.com'
msg['To'] = 'kalphageek@gmail.com'
msg.set_content('''
안녕하세요.

Python Mail Test 중입니다..
좋은하루 되세요.
''')


# smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp = smtplib.SMTP('smtp.office365.com', 587)
smtp.ehlo()
# SMTP_SSL인경우는 starttls안한다
smtp.starttls()
# smtp.login('soongon@gmail.com', 'tnsrhsl33')
smtp.login('kalphageek@outlook.com','***11211@')
smtp.send_message(msg)
smtp.quit()

