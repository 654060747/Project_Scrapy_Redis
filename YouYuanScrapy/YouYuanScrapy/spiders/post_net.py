import scrapy

#如果想要爬虫在一开始的时候就发送post请求,那么就需要在爬虫类中重写start_requests(self)方法,
#并且不再调用start_urls里面的url,如果不重写start_requests(self)那么爬虫会自动获取start_urls里面的url

class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['http://fanyi.youdao.com/']
    # 重写start_requests方法默认不调用
    start_urls = ['http://http://fanyi.youdao.com/']

    # 方法重写，也可以在此方法中获取动态cookie等
    def start_requests(self):
        url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        formdata = {
            "i": "狗",
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
        }
        yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.parse)

    def parse(self, response):
        print('*'*20)
        print(response.text)
        print('*'*20)