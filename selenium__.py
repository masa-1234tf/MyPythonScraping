from selenium import webdriver
from time import sleep


# driver　作成
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="./tools/chromedriver.exe",
                          options=options)
driver.implicitly_wait(8)
# drive.get()でサイトにアクセスする
driver.get('https://news.yahoo.co.jp/')
sleep(3)
print(driver.title)
print(driver.current_url)

driver.get('https://www.google.co.jp/')
sleep(3)
print(driver.title)
print(driver.current_url)
# 要素を取得し処理を行う
#search_bar = driver.find_element_by_name("q")
# sleep(3)
# search_bar.send_keys("python")
# sleep(3)
# search_bar.submit()
# sleep(5)
# driver.quit()
driver.save_screenshot("test.png")
driver.back()
driver.forward()
driver.refresh()

driver.close()
