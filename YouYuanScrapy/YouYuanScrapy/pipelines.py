# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy,os,json
import pymongo,pymysql
from scrapy.pipelines.images import ImagesPipeline


class YouyuanscrapyPipeline:
    ''' 写入文件 '''
    def process_item(self, item, spider):
        # line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        # self.file.write(line)
        return item

    # 这个方法在蜘蛛打开时被调用
    # def open_spider(self, spider):
    #     self.file = open('items.jl', 'w')

    # 当蜘蛛关闭时调用此方法
    # def close_spider(self, spider):
    #     self.file.close()


class MongoPipeline:
    ''' 
    存储到MongoDB 
    from_crawler配@classmethod用法
    '''
    # collection_name = 'scrapy_items'

    # def __init__(self, mongo_uri, mongo_db):
    #     self.mongo_uri = mongo_uri
    #     self.mongo_db = mongo_db

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
    #     )

    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_uri)
    #     self.db = self.client[self.mongo_db]

    # def close_spider(self, spider):
    #     self.client.close()

    def process_item(self, item, spider):
        # self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item


class MysqlPipeline(object):
    """
    存储到mysql 
    from_crawler配@classmethod用法
    """
    def __init__(self,host,db,user,passwd,port):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.client = None
        self.cursor = None

    # 从配置文件拿数据注入初始化
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get("MYSQL_HOST"),
            port = crawler.settings.get("MYSQL_PORT"),
            user = crawler.settings.get("MYSQL_USER"),
            passwd = crawler.settings.get("MYSQL_PASSWD"),
            db = crawler.settings.get("MYSQL_DBNAME"),
            )

    # 链接数据库
    def open_spider(self,spider):
        self.client = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            passwd = self.passwd,
            db = self.db,
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor
            )
        self.cursor = self.client.cursor()
        spider.logger.info('open_spider: %s' % "===============成功链接数据库")

    # 数据库操作
    def process_item(self, item, spider):
        # 向数据库中插入数据
        sql = 'insert into baidu(name,a,b,c) VALUES (%s,%s,%s,%s)'
        lis = (item['name'],item['a'],item['b'],item['c'])
        try:
            self.cursor.execute(sql,lis)
            self.client.commit()
        except Exception:
            spider.logger.warning('open_spider: %s' % "=============提交数据库失败")

        return item

    # 关闭数据库
    def close_spider(self,spider):
        self.client.close()
        spider.logger.info('open_spider: %s' % "==============成功关闭数据库")


class ImagespiderPipeline(ImagesPipeline):
    ''' 图片下载 '''
    def get_media_requests(self, item, info):
        # 通过传入的list集合循环每一张图片地址下载
        for image_url in item['img_url']:
            print('\n'*3)
            print(image_url)
            # image_url需要使用绝对路径
            yield scrapy.Request(image_url)
    # 默认保存目录full，这里重写方法将其修改
    def file_path(self, request, response=None, info=None):
        # 图片文件名，可以设置指定的保存目录
        img_name = request.url.split('/')[-1]
        return img_name # 返回文件名
    # def item_completed(self, results, item, info):
    #     return item # 返回给下一个即将被执行的管道类
