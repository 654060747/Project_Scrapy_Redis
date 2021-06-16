import scrapy,json
from scrapy_redis.spiders import RedisSpider


class PostSpider(RedisSpider):
    ''' scrapy-redis post请求 '''
    name = 'redis_post'
    allowed_domains = ['192.168.xx.xx:5000']
    # start_urls = ['http://192.168.xx.xx:5000/test1']
    redis_key = 'post:start_urls'

    # 方法重写，也可以在此方法中获取动态cookie等
    def make_request_from_data(self,data): # data数据即为post:start_urls发送过来的数据，不过为bytes类型
        print("\n"*10)
        print("=========="+data.decode())
        url = data.decode()
        formdata = {
            "name": "狗",
            "age": "AUTO",
            "age": "AUTO",
        }
        # Scrapy分布式爬虫过滤问题,不会显示更多重复项
        # 报错：DEBUG:Filtered duplicate request:<GET:xxxx>-no more duplicates will be shown
        # 原因：传入的网址是已经爬取过的，判断为已经爬取过的，程序自动结束
        # yield scrapy.Request(xxxurl,callback=self.xxxx)中有重复的请求
        # 要想爬虫再次运行：可以在Request中添加dont_filter=True(强制不过滤)
        # scrapy-redis发送post请求，重写方法make_request_from_data，这里必须return
        return scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse, dont_filter=True)


    def parse(self, response):
        print('\n'*3)
        print('*'*20)
        print(response.text)
        print('*'*20)
        print('\n'*3)