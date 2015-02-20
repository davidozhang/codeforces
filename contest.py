#!/usr/bin/python

'''
Problem 501A: http://codeforces.com/problemset/problem/501/A
Solved on: 2015-02-21
Result: Accepted 46 ms 4 KB
'''

def _max(p,t):
	return max(3*p/10.0, p-(p/250.0)*t)

def main():
	a,b,c,d=map(int, raw_input().split())
	m, v=_max(a,c), _max(b,d)
	if m>v:
		print 'Misha'
	elif m<v:
		print 'Vasya'
	else:
		print 'Tie'

if __name__=='__main__':
	main()