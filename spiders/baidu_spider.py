# -*- coding: utf-8 -*-

from __future__ import division
from scrapy.item import Item,Field
from model.mediaItem import MediaItem
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import signals, log
from scrapy.http import Request
import json
import math

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BaiduSpider(Spider):
	name="Baidu"
	base_url=""

	def __init__(self, rule=None, *args, **kwargs):
		self.allowed_domains=['%s' % (rule.allowed_domains)]
		self.start_urls=['%s' % (rule.start_urls)]
		self.base_url=rule.start_urls
		self.spider_desc=rule.spider_desc
		super(BaiduSpider,self).__init__(*args, **kwargs)

	def parse(self,response):
		jsonresponse = json.loads(response.body_as_unicode())
		total_url = 1
		if jsonresponse.has_key('total_num'):
			total_url = int(jsonresponse['total_num'])
			total_url = math.floor(total_url/18)
		if jsonresponse.has_key('videoshow'):
			if jsonresponse['videoshow'].has_key('videos'):
				for media in jsonresponse['videoshow']['videos']:
					item=MediaItem()

					if media.has_key('title'):
						item['title']=media['title'] if media['title'] else ""
					else:
						item['title']=""

					if media.has_key('url'):
						item['page_url']=media['url'] if media['url'] else ""
					else:
						item['page_url']=""

					if media.has_key('eName'):
						item['eName']=media['eName'] if media['eName'] else ""
					else:
						item['eName']=""

					if media.has_key('otherName'):
						item['otherName']=media['otherName'] if media['otherName'] else ""
					else:
						item['otherName']=""

					if media.has_key('adaptor'):
						item['adaptor']=media['adaptor'] if media['adaptor'] else ""
					else:
						item['adaptor']=""

					if media.has_key('director'):
						if media['director']:
							director_list=""
							for director in media['director']:
								director_list=director_list+','+director['name']
							if director_list:
								item['director']=director_list.lstrip(',')
							else:
								item['director']=""
							
							#item['director']=media['director'][0]['name'] if media['director'][0]['name'] else ""
						else:
							item['director']=""
					else:
						item['director']=''

					if media.has_key('actor'):
						if media['actor']:
							#item['leader']=media['actor'][0]['name'] if media['actor'][0]['name'] else ""
							actor_list=""
							for actor in media['actor']:
								actor_list=actor_list+','+actor['name']
							if actor_list:
								item['leader']=actor_list.lstrip(',')
							else:
								item['leader']=""
						else:
							item['leader']=""
					else:
						item['leader']=""

					if media.has_key('language'):
						item['language']=media['language'] if media['language'] else ""
					else:
						item['language']=""

					if media.has_key('type'):
						if media['type']:
							type_list=""
							for stype in media['type']:
								type_list=type_list+','+stype['name']
							if type_list:
								item['kind']=type_list.lstrip(',')
							else:
								item['kind']=""
							
							#item['kind']=media['type'][0]['name'] if media['type'][0]['name'] else ""
						else:
							item['kind']=""
					else:
						item['kind']=""

					if media.has_key('duration'):
						item['duration']=media['duration'] if media['duration'] else ""
					else:
						item['duration']=""

					if media.has_key('intro'):
						item['story']=media['intro'] if media['intro'] else ""
					else:
						item['story']=""

					if media.has_key('keyWord'):
						item['keyWord']=media['keyWord'] if media['keyWord'] else ""
					else:
						item['keyWord']=""

					if media.has_key('productPerson'):
						item['productPerson']=media['productPerson'] if media['productPerson'] else ""
					else:
						item['productPerson']=""

					if media.has_key('dubbing'):
						item['dubbing']=media['dubbing'] if media['dubbing'] else ""
					else:
						item['dubbing']=""

					if media.has_key('executiver'):
						item['executiver']=media['executiver'] if media['executiver'] else ""
					else:
						item['executiver']=''

					if media.has_key('original'):
						item['original']=media['original'] if media['original'] else ""
					else:
						item['original']=""

					if media.has_key('productColtd'):
						item['productColtd']=media['productColtd'] if media['productColtd'] else ""
					else:
						item['productColtd']=""

					if media.has_key('date'):
						item['productionTime']=media['date'] if media['date'] else ""
					else:
						item['productionTime']=""

					if media.has_key('licence'):
						item['licence']=media['licence'] if media['licence'] else ""
					else:
						item['licence']=""

					if media.has_key('registration'):
						item['registration']=media['registration'] if media['registration'] else ""
					else:
						item['registration']=""

					if media.has_key('distributColtd'):
						item['distributColtd']=media['distributColtd'] if media['distributColtd'] else ""
					else:
						item['distributColtd']=""

					if media.has_key('totalNumber'):
						item['totalNumber']=media['totalNumber'] if media['totalNumber'] else ""
					else:
						item['totalNumber']=""

					if media.has_key('update'):
						item['updateInfo']=media['update'] if media['update'] else ""
					else:
						item['updateInfo']=""

					if media.has_key('area'):
						if media['area']:
							item['area']=media['area'][0]['name'] if media['area'][0]['name'] else ""
						else:
							item['area']=""
					else:
						item['area']=""

					if media.has_key('playTime'):
						item['playTime']=media['playTime'] if media['playTime'] else ""
					else:
						item['playTime']=""

					if media.has_key('television'):
						item['television']=media['television'] if media['television'] else ""
					else:
						item['television']=""

					if media.has_key('producer'):
						item['producer']=media['producer'] if media['producer'] else ""
					else:
						item['producer']=""

					item['source']=self.spider_desc if self.spider_desc else ""
				
					yield item

		next_urls=[]
		count= int(total_url)
		for k in xrange(2,count):
			base_url=self.base_url+str(k)
			next_urls.append(base_url)
		for next_url in next_urls:
			self.logger.info('---------------------------Fetch url : %s',next_url)
			yield Request(next_url,callback=self.parse)
