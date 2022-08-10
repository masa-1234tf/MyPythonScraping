from time import sleep
import pandas as pd
import requests  # クローリングモジュール
from bs4 import BeautifulSoup  # スクレイピングモジュール


base_url = "https://next.rikunabi.com"
data_list = []
page_base_url = "https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?jb_type_long_cd=0505020507&jb_type_long_cd=0505020509&jb_type_long_cd=1203040000&wrk_plc_long_cd=0101000000&wrk_plc_long_cd=0313000000&curnum={}"
for i in range(3):
    url = page_base_url.format(1+i*50)
    sleep(2)

    res = requests.get(url, timeout=10)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "lxml")
    page_urls = soup.select("a:-soup-contains(企業ページ)")
    for page_url in page_urls:
        page_url = base_url+page_url.get("href")
        sleep(2)
        # リンク先の解析
        page_res = requests.get(page_url, timeout=10)
        page_res.raise_for_status()
        page_soup = BeautifulSoup(page_res.content, "lxml")

        company_name = page_soup.select_one(
            ".rnn-breadcrumb > li:last-of-type").text
        url_in_tag = page_soup.select_one(".rnn-col-11:last-of-type a")
        company_url = url_in_tag.get("href") if url_in_tag else None
        data_list.append({
            "Company": company_name,
            "URL": company_url
        })
        print(data_list[-1])  # 最後のリストを確認する
df = pd.DataFrame(data_list)
print(df)
df.to_csv("rikunabi_company_list.csv", index=None, encoding="utf-8-sig")
