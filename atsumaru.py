from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# seleniumクローリング
driver = webdriver.Chrome(
    executable_path="./tools/chromedriver.exe", options=options)
driver.implicitly_wait(10)
# 企業名
# 住所
# 電話番号
driver.get("https://atsumaru.jp/area/7/list?sagid=all")
sleep(3)
i = 0
while i <= 2:
    # スクロール
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)

    i = i + 1
# スクレイピング
data_list = []
soup = BeautifulSoup(driver.page_source, "lxml")
a_tags = soup.select("span.exe > a")
data_list = []
for a_tag in a_tags:
    url = "https://atsumaru.jp/" + a_tag.get("href")
    res = requests.get(url)
    res.raise_for_status()
    sleep(3)

    page_soup = BeautifulSoup(res.content, "lxml")
    company_name = page_soup.select_one("#detailBox > h2").text
    adreaa = page_soup.select_one(
        "td:-soup-contains('地図はこちら') > p:first-of-type").text
    tel = page_soup.select_one('div.telNo > p > strong > a').text

    data_list.append({
        "company_name": company_name,
        "adreaa": adreaa,
        "tel": tel
    })

df = pd.DataFrame(data_list)
print(df)
sleep(10)
# driver.quit()
