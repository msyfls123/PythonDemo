# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = '745784917@qq.com'
password = 'msyfls789abc'
to_addr = raw_input('To: ')
tmsg = raw_input('Content: ')
theader = raw_input('Title: ')
smtp_server = 'smtp.qq.com'

msg = MIMEText(tmsg.decode(), 'plain', 'utf-8')
msg['From'] = _format_addr(u'Kimi <%s>' % from_addr)
msg['To'] = _format_addr(u'你好 <%s>' % to_addr)
msg['Subject'] = Header(theader.decode(), 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()