from bs4 import BeautifulSoup
import requests

source = requests.get('https://twitter.com').text

soup = BeautifulSoup(source, 'lxml')

html = soup.find('html')

print(soup.prettify())

# summary = html.find('div', class_='errorContainer').h1.text
# print(summary)

# vid_src = html.find('img', alt='Twitter')['src']
# print(vid_src)

# Value = soup.find_all("p", {"class": "errorButton"})
# print(Value)

# Players = soup.find_all("a", {"class": ""})

# imgs = [html.find('img') for html in soup.find_all("html", {"class": ""}) if html.find('img')]
# team = [img.get('alt') for img in imgs]
# print(team)

Team = [html.find('img').get('alt') for html in soup.find_all("html", {"class": ""}) if html.find('img')]
print(Team)

# with open('example.html') as html_file:
# 	soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
# match = soup.title.text
# match = soup.div
# match = soup.find('div')
# match = soup.find('div', class_='footer')
# print(match)

# article = soup.find('div', class_='article')
# print(article)

# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)


# for article in soup.find_all('div', class_='article'):
# 	headline = article.h2.a.text
# 	print(headline)

# 	summary = article.p.text
# 	print(summary)

