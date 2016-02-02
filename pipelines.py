# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from model.config import DBSession
from model.mediainfo import MediaInfo
from datetime import datetime
import codecs
import json
import time

class MysqlPipeline(object):
	def open_spider(self,spider):
		self.session=DBSession()

	def process_item(self,item,spider):
		# now=datetime.utcnow()
		media=MediaInfo(title=self.list_format(item['title']),
			eName=self.list_format(item['eName']),
			otherName=self.list_format(item['otherName']),
			adaptor=self.list_format(item['adaptor']),
			director=self.list_format(item['director']),
			leader=self.list_format(item['leader']),
			kind=self.list_format(item['kind']),
			language=self.list_format(item['language']),
			duration=self.list_format(item['duration']),
			story=self.list_format(item['story']),
			keyWord=self.list_format(item['keyWord']),
			productPerson=self.list_format(item['productPerson']),
			dubbing=self.list_format(item['dubbing']),
			executiver=self.list_format(item['executiver']),
			original=self.list_format(item['original']),
			productColtd=self.list_format(item['productColtd']),
			productionTime=self.list_format(item['productionTime']),
			licence=self.list_format(item['licence']),
			registration=self.list_format(item['registration']),
			distributColtd=self.list_format(item['distributColtd']),
			source="iqiyi",
			createTime=self.getNowTime())
		self.session.add(media)
		self.session.commit()
		# try:
		# 	self.session.commit()
		# except Exception, e:
		# 	print media
		# 	self.session.rollback()
		

	def close_spider(self,spider):
		self.session.close()

	def list_format(self,input):
		return ','.join(input)
		# return input

	def getNowTime(self):
		return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

	def write_file_content(self, filepath, text, mode='w'):
			file_object = open(filepath, mode)
			file_object.write(text)
			file_object.close()
