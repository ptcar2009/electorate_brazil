init:
	pip install requirements.txt

crawl:
	scrapy runspider crawler/crawler.py