# import os
# Scrapy settings for YouYuanScrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'YouYuanScrapy'

SPIDER_MODULES = ['YouYuanScrapy.spiders']
NEWSPIDER_MODULE = 'YouYuanScrapy.spiders'

# scrapy-redis设置：
# Redis调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 指纹去重过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#默认队列，按优先级排序，由sorted set实现的一种非FIFO、LIFO方式
SCHEDULER_QUEUE_CLASS ='scrapy_redis.queue.PriorityQueue' 
#先进先出队列(FIFO)
#SCHEDULER_QUEUE_CLASS ='scrapy_redis.queue.FifoQueue'
#后进先出队列(LIFO)
#SCHEDULER_QUEUE_CLASS ='scrapy_redis.queue.LifoQueue'  
#True不清除Redis队列、这样可以暂停/暂停后恢复;False不管有没关闭Redis,Redis数据也会被清空
SCHEDULER_PERSIST = True
# redis数据库有密码情况
REDIS_HOST = '192.168.xx.xx'
REDIS_PORT = 6379
REDIS_PARAMS = {
    'password': 'ubuntu',
}
# 或
# REDIS_URL = "redis://192.168.xx.xx:6379"
#默认情况下,RFPDupeFilter只记录第一个重复请求。将DUPEFILTER_DEBUG设置为True会记录所有重复的请求。
# DUPEFILTER_DEBUG =True

# scrapy-redis其它设置
# 只在使用SpiderQueue或者SpiderStack是有效的参数，指定爬虫关闭的最大间隔时间
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

#item pipeline 将items 序列化 并用如下key名储存在redis中
#REDIS_ITEMS_KEY = '%(spider)s:items'

#默认的item序列化方法是ScrapyJSONEncoder，你也可以使用自定义的序列化方式
#REDIS_ITEMS_SERIALIZER = 'json.dumps'

#你设置的redis其他参数 Custom redis client parameters (i.e.: socket timeout, etc.)
# REDIS_PARAMS  = {}

#自定义的redis客户端类
#REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

#redis的默认encoding是utf-8，如果你想用其他编码可以进行如下设置：
#REDIS_ENCODING = 'latin1'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'YouYuanScrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True	
ROBOTSTXT_OBEY = False	

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 爬虫延迟时间
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 使用settings里面的cookie
# COOKIES_ENABLED = False
# 把settings的cookie关掉，使用自定义cookie
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'YouYuanScrapy.middlewares.YouyuanscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 开启代理、伪装浏览器中间件
DOWNLOADER_MIDDLEWARES = {
#    'YouYuanScrapy.middlewares.YouyuanscrapyDownloaderMiddleware': 543,
	'YouYuanScrapy.middlewares.UserAgentMiddleware': 544,
# 	 'YouYuanScrapy.middlewares.ProxyMiddleware': 545,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 通过配置RedisPipeline将item写入key为 spider.name:items的redis的list中，供后面的分布式处理item
ITEM_PIPELINES = {
	# 'YouYuanScrapy.pipelines.YouyuanscrapyPipeline': 400,
	'scrapy_redis.pipelines.RedisPipeline': 300,
	'YouYuanScrapy.pipelines.ImagespiderPipeline':301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# LOG等级
# LOG_LEVEL = 'DEBUG'

# 增加显示文件为中文　scrapy crawl baidu -o test.json
# FEED_EXPORT_ENCODING = 'utf-8'

# 配置图片的下载路径（相对路径与绝对路径配置）
# (根目录获取方法)
# IMAGES_STORE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
# (当前目录)
IMAGES_STORE = './images'
