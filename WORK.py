import requests
from bs4 import BeautifulSoup

def fetch_titles(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return []
    except Exception as err:
        print(f'Other error occurred: {err}')
        return []
    
    # Handle different character encodings
    response.encoding = response.apparent_encoding
    
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = []
    
    for h2 in soup.find_all('h2'):
        titles.append(h2.text.strip())
    
    for h1 in soup.find_all('h1'):
        titles.append(h1.text.strip())
        
    for p in soup.find_all('p'):
        titles.append(p.text.strip())
        
    return titles

url = 'https://example.com'
titles = fetch_titles(url)
for title in titles:
    print(title)
