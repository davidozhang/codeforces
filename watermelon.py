#!/usr/bin/python

'''
Problem 4A: http://codeforces.com/problemset/problem/4/A
Solved on: 2015-02-06
Updated on: 2015-03-08
Result: Accepted 124 ms 4 KB
'''

def main():
	input = raw_input()
	print 'YES' if int(input)>2 and int(input)%2==0 else 'NO'

if __name__=='__main__':
	main()