# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from model.config import DBSession
from model.mediainfo import MediaInfo
from search.es_access import import_to_es
from datetime import datetime
import codecs
import json
import time

class MysqlPipeline(object):
	def open_spider(self,spider):
		self.session=DBSession()

	def process_item(self,item,spider):
		# now=datetime.utcnow()
		#print item['page_url']
		#print 333333333333333333
		#if spider.crawler.stats.get_value('item_scraped_count')>10:
			#return
		media=MediaInfo(title=self.list_format(item['title'],spider),
			page_url=item['page_url'],
			eName=self.list_format(item['eName'],spider),
			otherName=self.list_format(item['otherName'],spider),
			adaptor=self.list_format(item['adaptor'],spider),
			director=self.list_format(item['director'],spider),
			leader=self.list_format(item['leader'],spider),
			kind=self.list_format(item['kind'],spider),
			language=self.list_format(item['language'],spider),
			duration=self.list_format(item['duration'],spider),
			story=self.list_format(item['story'],spider),
			keyWord=self.list_format(item['keyWord'],spider),
			productPerson=self.list_format(item['productPerson'],spider),
			dubbing=self.list_format(item['dubbing'],spider),
			executiver=self.list_format(item['executiver'],spider),
			original=self.list_format(item['original'],spider),
			productColtd=self.list_format(item['productColtd'],spider),
			productionTime=self.list_format(item['productionTime'],spider),
			licence=self.list_format(item['licence'],spider),
			registration=self.list_format(item['registration'],spider),
			distributColtd=self.list_format(item['distributColtd'],spider),
			totalNumber=self.list_format(item['totalNumber'],spider),
			updateInfo=self.list_format(item['updateInfo'],spider),
			area=self.list_format(item['area'],spider),
			source=item['source'],
			#createTime=self.getNowTime()
			)
		if media.title:
			self.session.add(media)
		# self.session.commit()
			try:
				self.session.flush()#写入数据库
				media_id=media.id
				self.session.commit()
				
				#写入ES
				json_data=json.dumps(media.to_dict(),ensure_ascii=False)#转换成json数组写入es
				import_to_es("mediacloud","mediainfo",media_id,json_data)
			except Exception, e:
				print e
				self.session.rollback()
		

	def close_spider(self,spider):
		self.session.close()

	def list_format(self,input,spider):
		if spider.name!='Baidu':
			return ','.join(input)
		else:
			return input

	def getNowTime(self):
		return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

	def write_file_content(self, filepath, text, mode='w'):
		file_object = open(filepath, mode)
		file_object.write(text)
		file_object.close()