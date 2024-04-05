import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            title = article.find('h2').text.strip()
            link = article.find('a')['href']
            print(f'Title: {title}\nLink: {link}\n')
    else:
        print(f'Error: Unable to retrieve data from {url}')
url = 'https://www.example.com'
scrape_website(url)
