#!/usr/bin/python
import re

'''
Problem 291B: http://codeforces.com/problemset/problem/291/B
Solved on: 2015-03-07
Result: Accepted 93 ms 1280 KB
'''

def main():
	for i in re.findall(r'(".*?"|\S+)', raw_input()):
		print '<{0}>'.format(i.replace('"',''))

if __name__=='__main__':
	main()