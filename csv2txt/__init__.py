#! /usr/bin/env python
# encoding=utf-8

import csv

defaultSeparator='\t'

# 分隔符转义对
escapeSeparatorDict={
	'\t' : '\\t'
}

# 翻转的分隔符转义对
escapeSeparatorFlipDict=dict(zip(escapeSeparatorDict.values(), escapeSeparatorDict.keys()))

def getVersion():
	return '0.0.1'

def escapeSeparator(separator):
	return escapeSeparatorDict.get(separator, separator);

def buildRow(row, fieldNames, separator, escapedSeparator):
	line=[];
	for field in fieldNames:
		cell=row[field].replace('\n', '\\n').replace(separator, escapedSeparator);
		line.append(cell);
	return separator.join(line);

def convertByPath(csvFilePath, txtFilePath, separator=defaultSeparator):
	with open(txtFilePath, 'w') as txtFile:
		with open(csvFilePath, 'rb') as csvFile:
			return convertByFile(csvFile, txtFile, separator);

def convertByFile(csvFile, txtFile, separator=defaultSeparator):
	es=escapeSeparator(separator)
	reader = csv.DictReader(csvFile)
	writeHeader=False
	if (not writeHeader):
		headerRow = dict((h, h) for h in reader.fieldnames)
		line=buildRow(headerRow, reader.fieldnames, separator, es);
		txtFile.write(line+'\n');
		writeHeader=True;

	for row in reader:
		line=buildRow(row, reader.fieldnames, separator, es);
		txtFile.write(line+'\n');
	return 0;
