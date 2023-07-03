from flask import Flask, request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.crawler import CrawlerProcess

app = Flask(__name__)

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = []

    def parse(self, response):
        # Extrai todos os links da página
        links = response.css('a::attr(href)').extract()
        # Itera sobre cada link e faz uma nova requisição
        for link in links:
            yield scrapy.Request(link, callback=self.parse)

    def start_requests(self):
        # Inicia o processo com a URL informada pelo usuário
        url = getattr(self, 'url', None)
        if url is not None:
            self.start_urls.append(url)
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

def catalogador(url):
    links = []
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href.startswith('http'):
                links.append(href)
            else:
                parsed_uri = urlparse(url)
                domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
                links.append(domain + href)
    except:
        print("Erro ao acessar a página")
    return links

def crawler(url, nivel):
    if nivel == 0:
        return []
    else:
        links = catalogador(url)
        for link in links:
            print(link)
            crawler(link, nivel - 1)

def ordenar_links(links):
    relevancia = {}
    for link in links:
        relevancia[link] = 0
    return sorted(relevancia, key=relevancia.get)[:10]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        nivel = int(request.form['nivel'])
        process = CrawlerProcess()
        process.crawl(MySpider, url=url)
        process.start()
        # Ordena os links coletados e retorna os 10 mais relevantes
        links_ordenados = ordenar_links(catalogador(url))
        return f'Os 10 links mais relevantes são: {links_ordenados}'
    else:
        return '''
            <form method="post">
                <p>Insira a URL:</p>
                <p><input type="text" name="url"></p>
                <p>Insira o nível:</p>
                <p><input type="text" name="nivel"></p>
                <p><input type="submit" value="Iniciar"></p>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
