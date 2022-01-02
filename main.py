import requests
import smtplib
import time
from bs4 import BeautifulSoup

url = 'https://www.hepsiburada.com/frisby-fcl-f1272c-4-x-120-mm-argb-4-lu-fan-seti-kit-sessiz-rgb-kasa-fani-p-HBCV00000FMSDC'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

def price_check():

    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    title = title[0:23]
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)

    if price < 350:
        mail_notify(title)



def mail_notify(title):

    sender = 'sender'
    receiver = 'receiver'

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender,'password')
        subject = title + ' beklenen fiyata ulasti.'
        body = 'Bu linkten erisebilirsin ' + url
        mailContent = f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender,receiver,mailContent)
        print('Mail başarılı bir şekilde gönderildi')

    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()


while(1):
    price_check()
    time.sleep(60*60)

