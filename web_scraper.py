import requests
from bs4 import BeautifulSoup
from notification import message

def Value():
    link = "https://coinmarketcap.com/currencies/bitcoin/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
    req = requests.get(link, headers=headers)

    site = BeautifulSoup(req.text, "html.parser")
    price = site.find("div", class_="sc-c1554bc0-0 hcOVLX flexStart alignBaseline")
    value = price.find("span", class_="sc-c1554bc0-0 RbQXx base-text").text
    return value

price = Value()

def Alerta(email1,senha,email2):
    global price

    new_value = Value()

    if price != new_value:
        price = new_value
        message(email1,price)






