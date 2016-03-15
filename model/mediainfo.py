# -*- coding: utf-8 -*-
from sqlalchemy import Column,String,DateTime,Integer
from sqlalchemy.ext.declarative import declarative_base

#//创建对象的基类
Base=declarative_base()

class MediaInfo(Base):
	__tablename__='MC_MediaInfo'

	id=Column(Integer,primary_key=True)
	title=Column(String)
	page_url=Column(String,unique=True)
	eName=Column(String)
	otherName=Column(String)
	adaptor=Column(String)
	director=Column(String)
	leader=Column(String)
	kind=Column(String)
	language=Column(String)
	duration=Column(String)
	story=Column(String)
	keyWord=Column(String)
	productPerson=Column(String)
	dubbing=Column(String)
	executiver=Column(String)
	original=Column(String)
	productColtd=Column(String)
	productionTime=Column(String)
	licence=Column(String)
	registration=Column(String)
	distributColtd=Column(String)
	totalNumber=Column(String)
	updateInfo=Column(String)
	area=Column(String)
	source=Column(Integer)
	createTime=Column(DateTime)
	updateTime=Column(DateTime)
	updator=Column(String)

	def to_dict(self):
		return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
