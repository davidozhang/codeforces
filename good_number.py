#!/usr/bin/python
import re

'''
Problem 365A: http://codeforces.com/problemset/problem/365/A
Solved on: 2015-03-29
Result: Accepted 62 ms 4 KB
'''

def main():
	re_string, result = '', 0
	n, k = map(int, raw_input().split())
	for i in range(k+1):
		re_string+='{}+'.format(str(i))
	for _ in range(n):
		match = re.search(re_string, ''.join(sorted(raw_input())))
		if match:
			result+=1
	print result

if __name__=='__main__':
	main()