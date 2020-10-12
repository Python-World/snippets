import requests
from bs4 import BeautifulSoup
import re
import smtplib
import time

# *********************CHANGE THIS*************************
# *********************************************************
# *********************************************************

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
# Google "my user agent" and replace the above text
headers = {"User-Agent": USER_AGENT}
URL = '$amazon_flipkart_url_here'
# Link for the product that you want to trace

MY_BUDGET = 360
# the price on which you want the notification
mins = 60
# time after you want to check again

sender_mail = 'sender@gmail.com'
sender_mail_password = "################"
# Use app passwords (create a 16 character separate password for this app)
# https://myaccount.google.com/apppasswords
receiver_mail = "receiver@gmail.com"

# *********************CHANGE THIS*************************
# *********************************************************
# *********************************************************


def get_current_price(page_source):
    if (URL[12:18])== 'amazon':
        try:
            price = page_source.find(id="priceblock_dealprice").get_text()
            # Check the deal price first
        except:
            try:
                price = page_source.find(id="priceblock_saleprice").get_text()
            except:
                try:
                    price = page_source.find(id="priceblock_ourprice").get_text()
                except:
                    print("Add new block in string")
                    # text("Unable to find the price class")
        price = re.sub("[^0-9]", "", price)[0:-2]
    else:
        # FLIPKART
        try:
            # price = page_source.find("div", {"class": ""}).get_text()
            price = page_source.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text()
        except:
                print("Add new block in string")
        price = re.sub("[^0-9]", "", price)
    
    return int(price)


def get_product_title(page_source):
    if (URL[12:18])== 'amazon':
        product = page_source.find(id="productTitle").get_text().strip()
    else:
        product = page_source.find("span", {"class": "_35KyD6"}).get_text().strip()
    count = 0
    p = ""
    for s in product.split():
        p = p + " " + s
        count += 1
        if count > 3:
            break
    product = p
    return product


def check_price():
    response = requests.get(URL, headers=headers)
    page_source = BeautifulSoup(response.content, "html.parser")
    # priceblock_dealprice
    # priceblock_ourprice
    # priceblock_saleprice
    price = get_current_price(page_source)
    product = get_product_title(page_source)
    if price <= MY_BUDGET:
        Subject = "Price fell down!!"
        Body = (
            "The price of"
            + product
            + "went down to "
            + str(price)
            + " INR. Buy now: "
            + URL
        )
        message = Subject + "\n\n" + Body
        message = f"Subject: {Subject}\n\n {message}"
        send_mail(message)
    else:
        print("Will check after 1 hour again!")


def send_mail(message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sender_mail, sender_mail_password)
    server.sendmail(sender_mail, receiver_mail, message)
    print("Email sent successfully!")
    server.quit()


while True:
    check_price()
    time.sleep(60 * mins)
