# -*- coding: utf-8 -*-
from spiders.iqiyi_spider import MgtvSpider
from model.config import DBSession
from model.rule import Rule
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

settings = Settings()

# crawl settings
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
settings.set("ITEM_PIPELINES" , {
	# 'pipelines.DuplicatesPipeline': 200,
	# 'pipelines.CountDropPipline': 100,
	'pipelines.MysqlPipeline': 300,
})

process = CrawlerProcess(settings)

db = DBSession()
rules = db.query(Rule).filter(Rule.status == 1)
for rule in rules:
	process.crawl(MgtvSpider,rule)
process.start()
