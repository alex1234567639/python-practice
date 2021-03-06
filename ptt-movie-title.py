# Python 2.7.9 之後引入了一个新特性，當使用urllib.urlopen打開一個 https 鏈接時，
# 會驗證一次 SSL，而當目標網站使用的是自簽名的證書時就會拋出異常
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 執行檔案： python3.9 檔案名稱.py
# 抓取 PTT 電影版的網頁原始碼
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"

# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url, headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)

# 下載beautifulsoup4遇到的問題
# https://blog.csdn.net/sunnywuxian/article/details/82870803

# 解析原始碼，取得每篇的文章標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser") # 將抓到的hrml丟給bs4解析

# 抓 title tag 裡的文字
# print(root.title.string)

# titles = root.find("div", class_="title") # 尋找 class="title" 的 div 標籤 (只印出第一個)

titles = root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤
for title in titles:
    if title.a != None:
        print(title.a.string)