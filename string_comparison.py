#!/usr/bin/python

'''
Problem 112A: http://codeforces.com/problemset/problem/112/A
Solved on: 2015-02-08
Result: Accepted 124 ms 4 KB
'''

def main():
	a=raw_input().lower()
	b=raw_input().lower()

	if a<b:
		print -1
	elif a==b:
		print 0
	else:
		print 1

if __name__=='__main__':
	main()