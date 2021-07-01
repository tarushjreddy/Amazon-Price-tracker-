from os import pipe
import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = "https://www.amazon.in/dp/B06ZZJ7NVH/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=5HHVZMW2JE8311H9ZRTK&pf_rd_t=101&pf_rd_p=3f1351e5-8e46-48ea-a79c-1f38294775f7&pf_rd_i=21524334031"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
title = soup.find(id="productTitle").get_text()

if(soup.find(id="priceblock_ourprice") == None):
    price = soup.find(id="priceblock_dealprice").get_text()
else:
    price = soup.find(id="priceblock_ourprice").get_text()
# print(soup.prettify())

converted_pice = float(price[1:5])
print("Title:", title.strip())
print("Price:", type(converted_pice))


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('"****************@gmail.com', "****************")
    subject = "Price fell down"
    body = f"Hey this is tarush j reddy yout product named {title} costs {converted_pice}"
    msg = f"{subject} {body}"
    server.sendmail(
        '"****************@gmail.com',
        "****************@gmail.com",
        msg)
    server.quit()


send_email()
