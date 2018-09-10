import csv
from datetime import datetime
import operator
import sys

csv.field_size_limit(sys.maxsize)

filename = sys.argv[1]

if __name__ == '__main__':
	with open(filename + '_sort.csv', 'w') as data_file:
		pass
	with open(filename, 'r', encoding='utf-8') as data_file:    
		reader = csv.reader(data_file, delimiter='\t')
		sortedlist = sorted(reader, key=lambda row:(row[0], row[3]), reverse=False)
		with open(filename + '_sort.csv', 'a', encoding='utf-8', newline='') as out:
			writer = csv.writer(out, delimiter='\t')
			writer.writerows(sortedlist)
