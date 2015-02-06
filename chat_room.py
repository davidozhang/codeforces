#!/usr/bin/python
import re

def main():
	m=re.search('h+(.*)e+(.*)l+(.*)l+(.*)o+',raw_input())
	if m:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()