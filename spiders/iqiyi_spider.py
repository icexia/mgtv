# -*- coding: utf-8 -*-

import scrapy 
from scrapy.item import Item,Field
from model.mediaItem import MediaItem
#from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import signals, log
from scrapy.http import Request
import urlparse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class IqiyiSpider(Spider):
	name="Iqiyi"
	rule = None

	def __init__(self, rule = None, *args, **kwargs):
		self.allowed_domains=['%s' % (rule.allowed_domains)]
		if rule.id == 1:
			self.start_urls=['http://list.iqiyi.com/www/1/-------------4-%s-1-iqiyi--.html' % p for p in xrange(1,30)]
		elif rule.id == 9 or rule.id == 12:
			self.start_urls=['http://list.iqiyi.com/www/2/-------------4-%s-1-iqiyi--.html' % p for p in xrange(1,30)]
		else:
			self.start_urls=['http://list.iqiyi.com/www/6/-------------4-%s-1-iqiyi--.html' % p for p in xrange(1,30)]
		self.spider_desc=rule.spider_desc
		self.rule = rule
		super(IqiyiSpider,self).__init__(*args, **kwargs)


	def parse(self,response):
		move_list = response.xpath('//div[@class="wrapper-piclist"]/ul/li/div[1]/a/@href')
		for move in move_list:
			yield Request(move.extract(), callback = self.parse_movies_item)

		next_pages = response.xpath(self.rule.next_page_xpath)
		if next_pages:
			next_page = urlparse.urljoin('http://list.iqiyi.com', next_pages[0].extract().strip())
			yield Request(next_page, callback = self.parse)


	def parse_movies_item(self,response):
		item=MediaItem()

		if self.rule.title_xpath:
			title=response.xpath(self.rule.title_xpath).extract()
			item['title']=title if title else ""
		else:
			item['title']=""

		item['page_url']=response.url

		if self.rule.e_name_xpath:
			eName=response.xpath(self.rule.e_name_xpath).extract()
			item['eName']=eName if  eName else ""
		else:
			item['eName']=""

		if self.rule.other_name_xpath:
			otherName=response.xpath(self.rule.other_name_xpath).extract()
			item['otherName']=otherName if otherName else ""
		else:
			item['otherName']=""

		if self.rule.adaptor_xpath:
			adaptor=response.xpath(self.rule.adaptor_xpath).extract()
			item['adaptor']=adaptor if adaptor else ""
		else:
			item['adaptor']=""
		
		if self.rule.director_xpath:
			director=response.xpath(self.rule.director_xpath).extract()
			item['director']=director if director else ""
		else:
			item['director']=""
		
		if self.rule.leader_xpath:
			leader=response.xpath(self.rule.leader_xpath).extract()
			item['leader']=leader if leader else ""
		else:
			item['leader']=""
			
		if self.rule.kind_xpath:
			kind=response.xpath(self.rule.kind_xpath).extract()
			item['kind']=kind if kind else ""
		else:
			item['kind']=""
		
		if self.rule.language_xpath:
			language=response.xpath(self.rule.language_xpath).extract()
			item['language']=language if language else ""
		else:
			item['language']=""
		
		if self.rule.duration_xpath:
			duration=response.xpath(self.rule.duration_xpath).extract()
			item['duration']=duration if duration else ""
		else:
			item['duration']=""
		
		if self.rule.story_xpath:
			story=response.xpath(self.rule.story_xpath).extract()
			item['story']=story if story else ""
		else:
			item['story']=""
		
		if self.rule.keyWord_xpath:
			keyWord=response.xpath(self.rule.keyWord_xpath).extract()
			item['keyWord']=keyWord if keyWord else ""
		else:
			item['keyWord']=""
		
		if self.rule.product_person_xpath:
			productPerson=response.xpath(self.rule.product_person_xpath).extract()
			item['productPerson']=productPerson if productPerson else ""
		else:
			item['productPerson']=""
		
		if self.rule.dubbing_xpath:
			dubbing=response.xpath(self.rule.dubbing_xpath).extract()
			item['dubbing']=dubbing if dubbing else ""
		else:
			item['dubbing']=""
		
		if self.rule.executiver_xpath:
			executiver=response.xpath(self.rule.executiver_xpath).extract()
			item['executiver']=executiver if executiver else ""
		else:
			item['executiver']=""
		
		if self.rule.original_xpath:
			original=response.xpath(self.rule.original_xpath).extract()
			item['original']=original if original else ""
		else:
			item['original']=""
		
		if self.rule.productColtd_xpath:
			productColtd=response.xpath(self.rule.productColtd_xpath).extract()
			item['productColtd']=productColtd if productColtd else ""
		else:
			item['productColtd']=""
		
		if self.rule.production_time_xpath:
			productionTime=response.xpath(self.rule.production_time_xpath).extract()
			item['productionTime']=productionTime if productionTime else ""
		else:
			item['productionTime']=""
		
		if self.rule.licence_xpath:
			licence=response.xpath(self.rule.licence_xpath).extract()
			item['licence']=licence if licence else ""
		else:
			item['licence']=""
		
		if self.rule.registration_xpath:
			registration=response.xpath(self.rule.registration_xpath).extract()
			item['registration']=registration if registration else ""
		else:
			item['registration']=""
		
		if self.rule.distributColtd_xpath:
			distributColtd=response.xpath(self.rule.distributColtd_xpath).extract()
			item['distributColtd']=distributColtd if distributColtd else ""
		else:
			item['distributColtd']=""

		if self.rule.totalNumber_xpath:
			totalNumber=response.xpath(self.rule.totalNumber_xpath).extract()
			item['totalNumber']=totalNumber if totalNumber else ""
		else:
			item['totalNumber']=""

		if self.rule.updateInfo_xpath:
			updateInfo=response.xpath(self.rule.updateInfo_xpath).extract()
			item['updateInfo']=updateInfo if updateInfo else ""
		else:
			item['updateInfo']=""

		if self.rule.area_xpath:
			area=response.xpath(self.rule.area_xpath).extract()
			item['area']=area if area else ""
		else:
			item['area']=""

		if self.rule.playTime_xpath:
			playTime=response.xpath(self.rule.playTime_xpath).extract()
			item['playTime']=playTime if playTime else ""
		else:
			item['playTime']=""

		if self.rule.television_xpath:
			television=response.xpath(self.rule.television_xpath).extract()
			item['television']=television if television else ""
		else:
			item['television']=""

		if self.rule.producer_xpath:
			producer=response.xpath(self.rule.producer_xpath).extract()
			item['producer']=producer if producer else ""
		else:
			item['producer']=""

		if self.rule.spider_desc:
			item['source']=self.rule.spider_desc
		else:
			item['source']='未知'
		
		yield item











