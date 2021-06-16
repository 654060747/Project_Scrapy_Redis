import scrapy

#如果想要爬虫在一开始的时候就发送post请求,那么就需要在爬虫类中重写start_requests(self)方法,
#并且不再调用start_urls里面的url,如果不重写start_requests(self)那么爬虫会自动获取start_urls里面的url

class PostSpider(scrapy.Spider):
    ''' scrapy post请求 '''
    name = 'post'
    allowed_domains = ['192.168.xx.xx:5000']
    # 重写start_requests方法默认不调用
    start_urls = ['http://192.168.xx.xx:5000']

    # 方法重写，也可以在此方法中获取动态cookie等
    def start_requests(self):
        url="http://192.168.xx.xx:5000/test1"
        formdata = {
            "name": "狗",
            "age": "AUTO",
        }
        # Scrapy分布式爬虫过滤问题,不会显示更多重复项
        # 报错：DEBUG:Filtered duplicate request:<GET:xxxx>-no more duplicates will be shown
        # 原因：传入的网址是已经爬取过的，判断为已经爬取过的，程序自动结束
        # yield scrapy.FormRequest(xxxurl,callback=self.xxxx)中有重复的请求
        # 要想爬虫再次运行：可以在Request中添加dont_filter=True(强制不过滤)
        yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.parse,dont_filter=True)

    def parse(self, response):
        print('\n'*3)
        print('*'*20)
        print(response.text)
        print('*'*20)
        print('\n'*3)
