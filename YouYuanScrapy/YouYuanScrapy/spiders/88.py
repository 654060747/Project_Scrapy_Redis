import scrapy
from scrapy.linkextractors import LinkExtractor

class YySpider(scrapy.Spider):
	name = 'huangye88'
	allowed_domains = ['huangye88.com']
	start_urls = 'https://so.huangye88.com/?kw=%E7%BB%B4%E4%BF%AE&page=2'

	def start_requests(self):
		''' 自定义cookie使用 '''

		cookies = {
		# "Cookie": "Hm_lvt_c8184fd80a083199b0e82cc431ab6740=1623134462,1623134791,1623317929; hy88showeditems=a%3A1%3A%7Bi%3A277343062%3Ba%3A3%3A%7Bs%3A7%3A%22subject%22%3Bs%3A91%3A%22%E6%BC%94%E8%AE%B2%E7%A8%BF%E6%80%8E%E4%B9%88%E5%86%99%E8%8C%83%E6%96%87%E5%A4%A7%E5%85%A8-%E8%87%AA%E6%88%91%E5%88%86%E4%BA%AB%E6%BC%94%E8%AE%B2%E7%A8%BF-%E6%BC%94%E8%AE%B2%E7%A8%BF%E6%A0%BC%E5%BC%8F%E5%8F%8A%E8%8C%83%E6%96%87%5B%E6%AC%A2%E9%B9%B0%E6%96%87%E6%A1%88%5D%22%3Bs%3A3%3A%22url%22%3Bs%3A62%3A%22https%3A%2F%2Fshanghai.huangye88.com%2Fxinxi%2F17272_e01hiv104f26c2.html%22%3Bs%3A3%3A%22img%22%3Bs%3A68%3A%22http%3A%2F%2Foss.huangye88.net%2Flive%2Fuser%2F2486993%2F1533810731027679400-0.jpg%22%3B%7D%7D; PHPSESSID=16233991437485-dba874b205c495eb4cf0b4a9c549cf7d06f3ceaa; hy88loginid=3427140; hy88username=u3427140; hy88usergroup=12; hy88mobile=xxx; Hm_lpvt_c8184fd80a083199b0e82cc431ab6740=1623745683",
		"Hm_lvt_c8184fd80a083199b0e82cc431ab6740":"1623134462,1623134791,1623317929",
		"hy88showeditems":"a%3A1%3A%7Bi%3A277343062%3Ba%3A3%3A%7Bs%3A7%3A%22subject%22%3Bs%3A91%3A%22%E6%BC%94%E8%AE%B2%E7%A8%BF%E6%80%8E%E4%B9%88%E5%86%99%E8%8C%83%E6%96%87%E5%A4%A7%E5%85%A8-%E8%87%AA%E6%88%91%E5%88%86%E4%BA%AB%E6%BC%94%E8%AE%B2%E7%A8%BF-%E6%BC%94%E8%AE%B2%E7%A8%BF%E6%A0%BC%E5%BC%8F%E5%8F%8A%E8%8C%83%E6%96%87%5B%E6%AC%A2%E9%B9%B0%E6%96%87%E6%A1%88%5D%22%3Bs%3A3%3A%22url%22%3Bs%3A62%3A%22https%3A%2F%2Fshanghai.huangye88.com%2Fxinxi%2F17272_e01hiv104f26c2.html%22%3Bs%3A3%3A%22img%22%3Bs%3A68%3A%22http%3A%2F%2Foss.huangye88.net%2Flive%2Fuser%2F2486993%2F1533810731027679400-0.jpg%22%3B%7D%7D",
		"PHPSESSID":"16233991437485-dba874b205c495eb4cf0b4a9c549cf7d06f3ceaa",
		"hy88loginid":"3427140",
		"hy88username":"u3427140",
		"hy88usergroup":"12",
		"hy88mobile":"xxx",
		"Hm_lpvt_c8184fd80a083199b0e82cc431ab6740":"1623745683",

		}
		# 有用headers缩减到最少
		headers={
		"Referer": "https://so.huangye88.com/",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
		}
		# COOKIES_ENABLED = True文件settings关闭默认cookie，使用自定义的
		# 此处的cookie已加在中间件
		yield scrapy.Request(self.start_urls,headers=headers,callback=self.parse,dont_filter=True)
		# cookie未加中间件
		# yield scrapy.Request(self.start_urls,headers=headers,cookies=cookies,callback=self.parse,dont_filter=True)


	def parse(self,reponse):
		print(reponse.text)
		pass

