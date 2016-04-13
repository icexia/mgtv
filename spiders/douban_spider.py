# -*- coding: utf-8 -*-

import scrapy 
from scrapy.item import Item,Field
from model.mediaItem import MediaItem
from utils.unicode import string2List
#from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import signals, log
from scrapy.http import Request
import urlparse
import json
import time
import sys
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')


class DoubanSpider(Spider):
	name="Douban"
	rule = None

	def __init__(self, rule = None, *args, **kwargs):
		self.allowed_domains=['%s' % (rule.allowed_domains)]
		self.start_urls=['https://movie.douban.com']
		#,'https://movie.douban.com/tv/#!type=tv&tag=%s&sort=recommend&page_limit=20&page_start=0' % p for p in ["热门","美剧","英剧","韩剧","日剧","国产剧","港剧","日本动画"]
		#]

		self.spider_desc=rule.spider_desc
		self.rule = rule
		self.headers={
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',\
			'accept-encoding':'gzip, deflate, sdch',\
			'accept-language':'zh-CN,zh;q=0.8',\
			'cache-control':'max-age=0',\
			':host':'movie.douban.com',\
			':method':'GET',\
			':scheme':'https',\
			'upgrade-insecure-requests':'1',\
			'referer':'https://movie.douban.com/chart',\
			'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',\
			'cookie':'cookie:bid="EFLcOryZq7w"; ll="118267"; gr_user_id=52712993-8b22-4228-906f-fc334f2f7c42; viewed="10590856_3288908"; ap=1; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1460343077%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DlDZyMiUkwpBvL0kSDv86H4YbpacysXQakBXG3Pwl0PuN0vwpulSNms9KwL8PRpkH%26wd%3D%26eqid%3D92aa1cb8001f466300000006570b1126%22%5D; __utma=30149280.660458676.1425630079.1460109185.1460341739.48; __utmc=30149280; __utmz=30149280.1460341739.48.41.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1642199914.1452569258.1460109185.1460343077.8; __utmc=223695111; __utmz=223695111.1460343077.8.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=4b67f30a19df431a.1452569258.8.1460343080.1460109184'
		}
		super(DoubanSpider,self).__init__(*args, **kwargs)


	def parse(self,response):
		
		#movie_types = ['movie','tv']
		movie_types = ['movie']
		for item in movie_types:
			if item == 'movie':
				#tag_list = ['热门','最新','经典','可播放','豆瓣高分','冷门佳片','华语','欧美','韩国','日本','动作','喜剧','爱情','科幻','悬疑','恐怖','文艺']
				tag_list = ['最新']
			else:
				tag_list = ['热门','美剧','英剧','韩剧','日剧','国产剧','港剧','日本动画']
			
			print tag_list
			tag_urls = []
			for tag in tag_list:
				#yield Request(move.extract(), callback = self.parse_movies_item)
				first_page = 'https://movie.douban.com/j/search_subjects?type=%s&tag=%s&sort=time&page_limit=20' % (item,urllib.quote(tag))
				#tag_pages = [first_page+'&page_start=%s' % i*10 for i in range(2,50) if i % 2 ==0]	
				totalPage = [i*10 for i in range(2,50) if i % 2 ==0]
				for page in totalPage:
					tag_pages = [first_page+'&page_start=%s' % page]
				#tag_urls.append(first_page)
			#if tag_urls:
				#for baseurl in tag_urls:
					#yield Request(baseurl,callback = self.crawl_movie_data)
					if tag_pages:
						for element in tag_pages:
							yield Request(element,callback = self.crawl_movie_data)

		#next_pages = response.xpath(self.rule.next_page_xpath)
		#if next_pages:
			#next_page = urlparse.urljoin('http://list.iqiyi.com', next_pages[0].extract().strip())
			#yield Request(next_page, callback = self.parse)
		

	def crawl_movie_data(self,response):
		jsonresponse = json.loads(response.body_as_unicode())
		if jsonresponse.has_key('subjects'):
			for data in jsonresponse['subjects']:
				if data.has_key('url'):
					url = data['url']
					yield Request(url,callback = self.parse_movies_item)
					#time.sleep(2)


	def parse_movies_item(self,response):
		item=MediaItem()

		if self.rule.title_xpath:
			title = response.xpath(self.rule.title_xpath).extract()
			title_tuple = string2List(title)
			if title_tuple:
				item['title'] = title_tuple[0] if title_tuple[0] else ""
			else:
				item['title'] = ""
		else:
			item['title'] = ""
		print item['title']
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









