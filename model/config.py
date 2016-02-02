# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#//初始化数据库连接
engine=create_engine('mysql+mysqldb://root:@@$iere05923*&($@10.1.201.152:3306/MediaCloud?charset=utf8')
#//创建DBSession类型
DBSession=sessionmaker(bind=engine)