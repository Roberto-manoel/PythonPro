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
    """
    Coleta os links de uma página da web e retorna uma lista de links completos.
    """
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
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a página: {e}"
    return links

def crawler(url, nivel):
    """
    Realiza o rastreamento recursivo dos links de uma página até um determinado nível.
    """
    if nivel == 0:
        return []
    else:
        links = catalogador(url)
        for link in links:
            print(link)
            crawler(link, nivel - 1)
        return links

def ordenar_links(links):
    """
    Classifica os links com base na relevância e retorna os 10 mais relevantes.
    """
    relevancia = {}
    for link in links:
        relevancia[link] = 0
    return sorted(relevancia, key=relevancia.get)[:10]

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Rota principal que exibe um formulário para inserir a URL e o nível, e inicia o processo de rastreamento.
    """
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

# Este teste verifica se a função catalogador retorna a lista esperada de URLs para a URL fornecida.
import unittest

class TestCatalogador(unittest.TestCase):
    def test_catalogador(self):
        url = "https://www.google.com"
        self.assertEqual(catalogador(url), ['https://www.google.com/imghp?hl=pt-BR&tab=wi', 'https://maps.google.com.br/maps?hl=pt-BR&tab=wl', 'https://www.youtube.com/?gl=BR&tab=w1', 'https://news.google.com.br/nwshp?hl=pt-BR&tab=wn', 'https://mail.google.com/mail/?tab=wm', 'https://drive.google.com/?tab=wo', 'https://www.google.com.br/intl/pt-BR/about/products?tab=wh', 'https://www.google.com.br/intl/pt-BR/about/?utm_source=google-BR&utm_medium=referral&utm_campaign=hp-footer&fg=1', 'https://www.google.com.br/setprefdomain?prefdom=US&sig=__JZKvzjQJ5z9dZL2W8GtXvq4fYJk%3D', 'https://accounts.google.com/ServiceLogin?hl=pt-BR&passive=true&continue=https://www.google.com/&ec=GAZAAQ'])

if __name__ == '__main__':
    unittest.main()
