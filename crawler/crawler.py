import scrapy
import requests
from os import mkdir


class government_shitheads(scrapy.Spider):
    name = "governo_brasileiro"
    start_urls = ["http://dados.gov.br/dataset/filiados-partidos-politicos"]
    def start_requests(self):
        yield scrapy.Request('http://dados.gov.br/dataset/filiados-partidos-politicos', self.parse)
    def parse(self, response):
        for href in response.xpath("//li[@class='resource-item']/a/@href").getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
        for href in response.xpath("//p[@class='muted ellipsis']/a/@href").getall():
            resp = requests.get(response.urljoin(href))
            with open("temp/" + href.split('/')[-1], "wb") as zi:
                zi.write(resp.content)

