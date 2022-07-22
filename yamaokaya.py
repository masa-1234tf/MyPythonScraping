from cProfile import label
from tkinter import font
import matplotlib.pyplot as plt
import matplotlib.style
import requests  # クローリングモジュール
from bs4 import BeautifulSoup  # スクレイピングモジュール

url = "https://www.yamaokaya.com/menus/regular/"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')

for i, content_found in enumerate(soup.find_all('div', class_='content')):
    #name_found_text = name_found.text.replace('\t', '').replace('\n', '').replace('\r', '')
    name_found_name = content_found.find("dt", class_="name").text.replace(
        '\t', '').replace('\n', '').replace('\r', '')
    name_found_price = content_found.find("dd", class_="price").text.replace(
        '\t', '').replace('\n', '').replace('\r', '').replace('（税込み）', '').replace('東北・新潟地区・北陸地区限定', '').replace(
            ',', '').replace('¥', '')
    print("="*30, i+1, "="*30)
    print(name_found_name, ":", name_found_price)

name = []
price = []
counter = []
for i, content_found in enumerate(soup.find_all('div', class_='content')):
    counter += [i]
    name += [content_found.find("dt", class_="name").text.replace(
        '\t', '').replace('\n', '').replace('\r', '')]
    price += [content_found.find("dd", class_="price").text.replace(
        '\t', '').replace('\n', '').replace('\r', '').replace('（税込み）', '').replace('東北・新潟地区・北陸地区限定', '').replace(
            ',', '').replace('¥', '')]

matplotlib.style.use("ggplot")
# 目盛線を表示
plt.grid()

x = counter
y = list(map(int, price))
labels = name

average = sum(y) / i
plt.axhline(average, ls="-.", color="magenta")
plt.bar(x, y, tick_label=labels, width=1, color='#0096c8',
        edgecolor='b', linewidth=2, label="値段")
plt.xlabel("商品名")
plt.xticks(fontsize=8)
plt.ylabel("値段")
plt.show()
