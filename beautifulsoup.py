from bs4 import BeautifulSoup
import requests

#GETTING THE HTML
url = "https://example.com"
res = requests.get(url)
print(res.status_code)

html = res.text

#CREATING SOUP OBJECT
soup = BeautifulSoup(html , "html.parser")

#PRINT WHOLE HTML (sometimes messy)
print(soup)

#TITLE TAG
print(soup.title)
print(soup.title.string)

#FIRST H1 AND P TAG
print(soup.h1)
print(soup.p)

#FIND FIRST MATCH
tag = soup.find("a")
print(tag)

#FIND ALL LINKS
links = soup.find_all("a")
for i in links:
    print(i)

#GET HREF FROM LINKS
for i in soup.find_all("a"):
    print(i.get("href"))

#CSS SELECTORS (sometimes useful)
print(soup.select("p"))
print(soup.select("a"))

#CLASS AND ID SEARCH
print(soup.find_all("a", class_="nav-link"))
print(soup.find_all(id="main"))

#GET TEXT ONLY
print(soup.get_text())

#GET TEXT FROM TAG
print(soup.find("p").text)

#ATTRIBUTE ACCESS
a = soup.find("a")
print(a["href"])

#SAFE WAY
print(a.get("href"))

#NAVIGATING DOM (basic)
div = soup.find("div")

print(div.parent)
print(div.children)

for i in div.children:
    print(i)

#REAL USE CASE
for i in soup.find_all("h2"):
    print(i.text)

for i in soup.find_all("a"):
    print(i.get("href"))
