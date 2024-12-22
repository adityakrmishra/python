import requests
from bs4 import BeautifulSoup

def fetch_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = []
    for h2 in soup.find_all('h2'):
        titles.append(h2.text)
    return titles

url = 'https://example.com'
titles = fetch_titles(url)
for title in titles:
    print(title)
