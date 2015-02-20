#!/usr/bin/python

'''
Problem 519B: http://codeforces.com/problemset/problem/519/B
Solved on: 2015-03-07
Result: Accepted 233 ms 9200 KB
'''

def main():
	prev, n = None, int(raw_input())
	for i in [map(int, raw_input().split()) for i in range(3)]:
		_sum = sum(i)
		if prev is not None and sum(i)!=prev:
			print prev-_sum
		prev=_sum

if __name__=='__main__':
	main()