#!/usr/bin/python
import math

'''
Problem 448A: http://codeforces.com/problemset/problem/448/A
Solved on: 2015-02-09
Updated on: 2015-03-08
Result: Accepted 46 ms 4 KB
'''

def main():
	fc, sc, tc=map(int, raw_input().split())
	fm, sm, tm=map(int, raw_input().split())
	cup_shelves=int(math.ceil((fc+sc+tc)/5.0))
	medal_shelves=int(math.ceil((fm+sm+tm)/10.0))
	print 'YES' if (cup_shelves+medal_shelves)<=int(raw_input()) else 'NO'

if __name__=='__main__':
	main()