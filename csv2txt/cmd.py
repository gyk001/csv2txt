#!/usr/bin/env python
# encoding=utf-8

import os
import argparse
import csv2txt

def convert_by_cmd():
	# 参数定义
	parser = argparse.ArgumentParser(description="Convert a csv file to token separator txt file")
	parser.add_argument('--version', '-v', action='version', version='%(prog)s version : v'+csv2txt.getVersion(), help='show the version')
	parser.add_argument('--separator', '-s', metavar='"\\t"', default= "\t", help='The separator between column, default is TAB(\\t)')
	parser.add_argument("csv", type=argparse.FileType('r'), help='input csv file path to convert')
	parser.add_argument("txt", type=argparse.FileType('w'), help='ouput txt file path')
	
	# 解析参数
	args = parser.parse_args()	
	csvPath=os.path.abspath(args.csv.name)
	txtPath=os.path.abspath(args.txt.name)
	separator=csv2txt.escapeSeparatorFlipDict.get(args.separator, args.separator);

	escapeSeparator= csv2txt.escapeSeparator(separator);
	print(u'Convert '+csvPath+' to ' +txtPath+ ' with separator '+ escapeSeparator)

	# 执行转换
	csv2txt.convertByFile(args.csv, args.txt, separator);
