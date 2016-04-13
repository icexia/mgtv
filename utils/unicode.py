# -*- coding: utf-8 -*-
"""
unicode编码处理工具
"""

def is_chinese(uchar):
	"""判断一个unicode是否是汉字"""
	if uchar >= u'u4e00' and uchar<=u'u9fa5':
			return True
	else:
			return False

def is_other(uchar):
	"""判断是否非汉字，数字和英文字符"""
	if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
			return True
	else:
			return False

def string2List(ustring):
	"""将ustring按照中文，非中文分开"""
	str_cn = ""
	str_en = ""
	for uchar in ustring:
		if is_chinese(uchar):
			str_cn += uchar
		else:
			str_en += uchar

	return str_en,str_en