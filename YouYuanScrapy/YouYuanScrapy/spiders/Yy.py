import scrapy
from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from YouYuanScrapy.items import YouyuanscrapyItem
import re


class YySpider(RedisCrawlSpider):
    name = 'Yy'
    # 静态限制域名
    allowed_domains = ['m.yoyuan.com.cn']
    # # 动态限制域名
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(YySpider, self).__init__(*args, **kwargs)

    # start_urls = ['http://m.yoyuan.com.cn/find/beijing/mm18-0/advance-0-0-0-0-0-0-0/p1/']
    redis_key = 'yyspider:start_urls'

    rules = (
        # Ajax加载的没有翻页页面可使用抓包或查看JS、json等
        Rule(LinkExtractor(allow=r'/mm18-0/advance-0-0-0-0-0-0-0/p\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'/\d+-profile/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = YouyuanscrapyItem()
        # 网名
        item['net_name'] = response.xpath('/html/body/div[2]/div/dl/dd/div[1]/strong/text()').extract()[0].strip()
        # 所在城市
        item['city'] = response.xpath('/html/body/div[2]/div/dl/dd/p/text()').extract()[0].strip().split(" ")[0]
        # 年龄
        age_data = re.findall(r'\d+'+"岁",response.xpath('/html/body/div[2]/div/dl/dd/p/text()').extract()[0].strip())
        if len(age_data) == 0:
            item['age'] = ""
        else:
            item['age'] = age_data[0]
        # 身高
        height_data = re.findall(r'\d+'+"cm",response.xpath('/html/body/div[2]/div/dl/dd/p/text()').extract()[0].strip())
        if len(height_data) == 0:
            item['height'] = ""
        else:
            item['height'] = height_data[0]
        # 工资
        salary_data = re.findall(r'\d+'+"元",response.xpath('/html/body/div[2]/div/dl/dd/p/text()').extract()[0].strip())
        if len(salary_data) == 0:
            item['salary'] = ""
        else:
            item['salary'] = salary_data[0]
        # 房
        item['house'] = response.xpath('/html/body/div[2]/div/dl/dd/p/text()').extract()[0].strip().split(" ")[-1]
        # 体重
        item['weight'] = response.xpath('/html/body/div[4]/ul/li[2]/div/ol[1]/li[2]/span/text()').extract()[0].strip() 
        # 学历
        item['education'] = response.xpath('/html/body/div[4]/ul/li[2]/div/ol[1]/li[3]/span/text()').extract()[0].strip() 
        # 婚姻
        item['marriage'] = response.xpath('/html/body/div[4]/ul/li[2]/div/ol[2]/li[1]/span/text()').extract()[0].strip() 
        # # 图片链接
        img_data = response.xpath('//*[@id="photo"]/div/ul/li/a/img/@src').extract()
        st = ""
        if len(img_data) == 0:
            item['img_url'] = ""
        else:
            for one_img in img_data:
                st = st + one_img + ","
            item['img_url'] = st

        yield item
