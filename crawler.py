# Python 2.7.9 之後引入了一个新特性，當使用urllib.urlopen打開一個 https 鏈接時，
# 會驗證一次 SSL，而當目標網站使用的是自簽名的證書時就會拋出異常
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 抓取 Medium.com 的文章資料
import urllib.request as req
url = "https://medium.com/_/api/home-feed"

# 建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url, headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8") # 根據觀察，取得的資料是 JSON 格式，所以無法用bs4解析(它是解析Html格式)
print(data)

# 解析 JSON 格式的資料，取得每篇文章標題
import json
data = data.replace("])}while(1);</x>", "") # 處理奇怪的字串
data = json.loads(data) #把原始的 JSON 資料解析成字典/列表的表使形式

# 取得 JSON 資料中的文章標題
posts = data["payload"]["references"]["Post"]
for key in posts:
    post = posts[key]
    print(post["title"])