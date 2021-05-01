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
print(data)

# 