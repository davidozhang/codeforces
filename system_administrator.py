#!/usr/bin/python

'''
Problem 34C: http://codeforces.com/problemset/problem/34/C
Solved on: 2015-03-04
Result: Accepted 124 ms 20 KB
'''

def main():
	_list=[{0:0, 1:0}, {0:0, 1:0}]
	for _ in range(int(raw_input())):
		t, x, y=map(int, raw_input().split())
		_list[t-1][1]+=x
		_list[t-1][0]+=y 
	for i in _list:
		print 'LIVE' if i[1]>=i[0] else 'DEAD'

if __name__=='__main__':
	main()