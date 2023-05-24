import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikipedia.org/wiki/Python'

def getlinks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'Página principal: {soup.title.string}')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/wiki/'):
            newurl = f'https://pt.wikipedia.org{href}'
            print(f'Página secundária: {newurl}')

getlinks(url)