# Python 2.7.9 之後引入了一个新特性，當使用urllib.urlopen打開一個 https 鏈接時，
# 會驗證一次 SSL，而當目標網站使用的是自簽名的證書時就會拋出異常
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 抓取 PTT 八卦版的網頁原始碼 (注意有Cookie)
import urllib.request as req

def getData(url):
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request = req.Request(url, headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "cookie": "over18=1"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 解析原始碼，取得每篇的文章標題
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser") # 將抓到的hrml丟給bs4解析

    titles = root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤
    for title in titles:
        if title.a != None:
            print(title.a.string)

    # 抓取上一頁的連結
    nextLink = root.find("a", string = "‹ 上頁") # 找到內文是 "‹ 上頁" 的 a 標籤 
    return(nextLink["href"])


# 抓取一個頁面的標題
pageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 3: # 連續抓三頁的標題
    pageUrl = "https://www.ptt.cc" + getData(pageUrl)
    count += 1