import urllib.request as req
import bs4

url = "https://www.ptt.cc/bbs/movie/index.html"
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)

root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")

for title in titles:
    if title.a is not None:
        print(title.a.string)
