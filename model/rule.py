# -*- coding: utf-8 -*-
from sqlalchemy import Column,String,DateTime,Integer
from sqlalchemy.ext.declarative import declarative_base

#//创建对象的基类
Base=declarative_base()

class Rule(Base):
	__tablename__='MC_Spider_Rule'

	#//表结构
	id=Column(Integer,primary_key=True)
	spider_name=Column(String)
	start_urls=Column(String)
	allowed_domains=Column(String)
	restrict_xpaths = Column(String)
	allow_url=Column(String)
	next_page_xpath=Column(String)
	title_xpath=Column(String)
	e_name_xpath=Column(String)
	other_name_xpath=Column(String)
	adaptor_xpath=Column(String)
	director_xpath=Column(String)
	leader_xpath=Column(String)
	kind_xpath=Column(String)
	language_xpath=Column(String)
	duration_xpath=Column(String)
	story_xpath=Column(String)
	keyWord_xpath=Column(String)
	product_person_xpath=Column(String)
	dubbing_xpath=Column(String)
	executiver_xpath=Column(String)
	original_xpath=Column(String)
	productColtd_xpath=Column(String)
	production_time_xpath=Column(String)
	licence_xpath=Column(String)
	registration_xpath=Column(String)
	distributColtd_xpath=Column(String)
	totalNumber_xpath=Column(String)
	updateInfo_xpath=Column(String)
	area_xpath=Column(String)
	status=Column(Integer)
	spider_desc=Column(String)
	create_time=Column(DateTime)
