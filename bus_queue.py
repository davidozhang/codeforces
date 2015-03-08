#!/usr/bin/python

'''
Problem 435A: http://codeforces.com/problemset/problem/435/A
Solved on: 2015-03-28
Result: Accepted 61 ms 4 KB
'''

def main():
	_sum, result = 0, 1
	n, m = map(int, raw_input().split())
	for i in map(int, raw_input().split()):
		if _sum+i > m:
			result+=1
			_sum = 0
		_sum+=i
	print result

if __name__=='__main__':
	main()
