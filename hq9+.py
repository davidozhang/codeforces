#!/usr/bin/python

'''
Problem 133A: http://codeforces.com/problemset/problem/133/A
Solved on: 2015-02-08
Result: Accepted 124 ms 8 KB
'''

def main():
	result={}
	s=raw_input()

	for i in s:
		result[i]=1

	if 'H' in result or 'Q' in result or '9' in result:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()