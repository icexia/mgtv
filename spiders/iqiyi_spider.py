# -*- coding: utf-8 -*-

import scrapy 
from scrapy.item import Item,Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import signals, log
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MediaItem(Item):
	url=Field()
	title=Field()
	eName=Field()
	otherName=Field()
	adaptor=Field()
	director=Field()
	leader=Field()
	kind=Field()
	language=Field()
	duration=Field()
	story=Field()
	keyWord=Field()
	productPerson=Field()
	dubbing=Field()
	executiver=Field()
	original=Field()
	productColtd=Field()
	productionTime=Field()
	licence=Field()
	registration=Field()
	distributColtd=Field()
	source=Field()
	createTime=Field()
	updateTime=Field()
	updator=Field()


class MgtvSpider(CrawlSpider):
	name="Mgtv"

	def __init__(self,rule):
		self.rule=rule
		self.name=rule.spider_name
		# self.allowed_domains=rule.allowed_domains
		self.allowed_domains=['v.ifeng.com']
		# self.start_urls=rule.start_urls
		self.start_urls=['http://v.ifeng.com/vlist/nav/movie/update/1/list.shtml']
		rule_list=[]

		rule_list.append(Rule(LinkExtractor(
			allow=("http://v\.ifeng\.com/movie/201411/", )),
			callback='parse_movies_item'))
		self.rules=tuple(rule_list)
		# self.rules=[
		# 	Rule(LinkExtractor(allow=("http://v\.ifeng\.com/movie/201411/", )), callback='parse_movies_item'),
		# ]
		super(MgtvSpider,self).__init__()


	def parse_movies_item(self,response):
		print response.url
		item=MediaItem()

		if self.rule.title_xpath:
			title=response.xpath(self.rule.title_xpath).extract()
			item['title']=title if title else ""
		else:
			item['title']=""

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
		
		return item



