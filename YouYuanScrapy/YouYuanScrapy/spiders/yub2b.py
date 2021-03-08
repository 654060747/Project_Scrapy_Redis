import scrapy
from scrapy.linkextractors import LinkExtractor

class YySpider(scrapy.Spider):
	name = 'yub2b'
	allowed_domains = ['yub2b.com']
	start_urls = ['http://www.yub2b.com/news/list-49-3.html']

	def parse(self, response):
		link = LinkExtractor(restrict_xpaths='/html/body/div[3]/div/div[1]/div/div[2]/div')
		links = link.extract_links(response)
		for link_one in links:
			print(link_one)
			print("$$$$$$$$$$$$$$$$$$$"+link_one.url)
			print("+++++++++++++++++++++++++++"+link_one.text)
