from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path="./tools/chromedriver.exe", options=options)
driver.implicitly_wait(10)

driver.get("https://news.yahoo.co.jp/")
sleep(3)

serch_box = driver.find_element_by_css_selector("input.sc-kgoBCf")
sleep(3)

serch_box.send_keys("機械学習")
sleep(3)

serch_box.submit()


while True:
    # スクロール
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)
    # セレクター取得
    button = driver.find_elements_by_css_selector(
        "div.newsFeed > div > span > button")
    sleep(1)
    # ボタンを押す
    if button:
        button[0].click()
    else:
        break
a_tags = driver.find_elements_by_css_selector("a.newsFeed_item_link")

for i, a_tag in enumerate(a_tags):
    print("="*30, i, "="*30)
    print(a_tag.find_element_by_css_selector(".newsFeed_item_title").text)
    print(a_tag.get_attribute("href"))

driver.quit()
