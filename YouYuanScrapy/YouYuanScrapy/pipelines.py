# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy,os,json
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
		return img_name	# 返回文件名
    # def item_completed(self, results, item, info):
    #     return item # 返回给下一个即将被执行的管道类