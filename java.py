#!/usr/bin/python

'''
Problem 66A: http://codeforces.com/problemset/problem/66/A
Solved on: 2015-02-21
Result: Accepted 92 ms 8 KB
'''

def main():
	_input=long(raw_input())
	if _input<1<<7:
		print 'byte'
	elif _input<1<<15:
		print 'short'
	elif _input<1<<31:
		print 'int'
	elif _input<1<<63:
		print 'long'
	else:
		print 'BigInteger'

if __name__=='__main__':
	main()