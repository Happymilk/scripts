import csv
import time
import datetime
import codecs
import sys  
import chardet
import re

csv.field_size_limit(sys.maxsize)

inputfile = sys.argv[1]

if __name__ == '__main__':
	start = 0
	temp = []
	with open(inputfile + '_superglued.csv', 'w', encoding='utf8', newline='') as out:
		columns = ["dialog_id", "author_id", "operator", "date", "text"]
		writer = csv.DictWriter(out, fieldnames=columns, delimiter='\t')
		writer.writeheader()
	with open(inputfile, 'r', encoding='utf8') as outcsv:
		reader = csv.reader(outcsv, delimiter='\t')
		for row in reader:
			if start == 1:
				try:
					if temp[1] == row[1] and temp[0] == row[0]:
						temp[4] += '->' + row[4] 
					else:  
						with open(inputfile + '_superglued.csv', 'a', encoding='utf8', newline='') as out:
							writer = csv.writer(out, delimiter='\t')      
							writer.writerow(temp)
						temp = row
				except:
					temp[4] += ' ' + row[0] 
			else:
				start += 1
				temp = row