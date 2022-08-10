from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

# driver　作成
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="./tools/chromedriver.exe",
                          options=options)
driver.implicitly_wait(8)
# drive.get()でサイトにアクセスする
driver.get(
    'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=')
sleep(3)
while True:
    # スクロール
    driver.execute_script(
        "0,window.scrollBy(0,document.body.scrollHeight)")
    sleep(2)
    driver.execute_script(
        "0,window.scrollBy(0,document.body.scrollHeight)")
    # CSSセレクタ取得
    button = driver.find_element_by_css_selector("p > .DChGS")
    sleep(3)
    # ボタンを押す
    if button:
        button.click()
    else:
        break

driver.close()
