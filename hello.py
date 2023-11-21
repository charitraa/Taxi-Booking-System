import smtplib

import os

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('stharabi9862187405@gmail.com', '')
    server.sendmail('stharabi9862187405@gmail.com', to, content)
    server.close()


content = 'hello'
to = 'artibarstha@gmail.com'
sendEmail(to , content)