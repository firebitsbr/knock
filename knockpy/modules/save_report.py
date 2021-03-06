import time
import json

def touch(filename):
	fname = filename
	file = open(fname, 'w')
	file.close()

def export(domain, report, _type):
	timestamp = time.time()
	filename = domain.replace('.', '_')+'_'+str(timestamp)+'.'+_type
	if _type == 'csv':
		csv_report = ''
		for item in report:
			csv_report += item + '\n'
		report = csv_report
	try:
		with open(filename, 'a') as f:
			f.write(report)
		f.close()
		return '\n'+_type.upper()+' report saved in: '+filename
	except: 
		return '\nCannot write report file: '+filename
