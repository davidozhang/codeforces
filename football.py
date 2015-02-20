#!/usr/bin/python

'''
Problem 96A: http://codeforces.com/problemset/problem/96/A
Solved on: 2015-02-08
Result: Accepted 122 ms 12 KB
'''

def main():
	n=raw_input()
	if '0000000' in n or '1111111' in n:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()