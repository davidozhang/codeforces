#!/usr/bin/python
from math import floor

'''
Problem 486A: http://codeforces.com/problemset/problem/486/A
Solved on: 2015-02-08
Updated on: 2015-03-08
Result: Accepted 61 ms 8 KB
'''

def main():
	n=int(raw_input())
	print n/2 if n%2==0 else int(floor(n/2)-n)

if __name__=='__main__':
	main()