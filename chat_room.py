#!/usr/bin/python
import re

'''
Problem 58A: http://codeforces.com/problemset/problem/58/A
Solved on: 2015-02-09
Updated on: 2015-03-08
Result: Accepted 92 ms 8 KB
'''

def main():
	m=re.search('h+(.*)e+(.*)l+(.*)l+(.*)o+',raw_input())
	print 'YES' if m else 'NO'

if __name__=='__main__':
	main()