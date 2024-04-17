from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://twitter.com').text

soup = BeautifulSoup(source, 'lxml')

# open new file for writing - will erase file if it already exists -
csv_file = open('cms_scrape.csv', 'w', newline='', encoding='utf-8')

# make a new variable - c - for Python's CSV writer object -
csv_writer = csv.writer(csv_file)
# write a column headings row - do this only once -
csv_writer.writerow(['headline', 'summary', 'yt_link'])

for html in soup.find_all('html'):
	headline = html.find('div', class_='errorContainer').p.text
	print(headline)

	summary = html.find('div', class_='errorContainer').h1.text
	print(summary)	

	try:
		vid_src = html.find('div', class_='errorContainer').img['srcset']

		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]

		yt_link = f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = None

	print(yt_link)

	print()
	# write a column headings row - do this only once -
	csv_writer.writerow([headline, summary, yt_link])

# save and close the file
csv_file.close()

# Value = soup.find_all("p", {"class": "errorButton"})
# print(Value)

# Players = soup.find_all("a", {"class": ""})

# imgs = [html.find('img') for html in soup.find_all("html", {"class": ""}) if html.find('img')]
# team = [img.get('alt') for img in imgs]
# print(team)

# Team = [html.find('img').get('alt') for html in soup.find_all("html", {"class": ""}) if html.find('img')]
# print(Team)

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

