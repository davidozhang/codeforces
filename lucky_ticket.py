#!/usr/bin/python
from sets import Set

'''
Problem 146A: http://codeforces.com/problemset/problem/146/A
Solved on: 2015-02-21
Result: Accepted 124 ms 380 KB
'''

def _sum(s):
	result=0
	for i in s:
		result+=int(i)
	return result

def main():
	success, _set, n=True, set(), int(raw_input())
	num=raw_input()
	for i in num:
		_set.add(i)
	if not _set.issubset({'4','7'}) or _sum(num[:n/2])!=_sum(num[n/2:]):
		success=False

	print 'YES' if success else 'NO'

if __name__=='__main__':
	main()