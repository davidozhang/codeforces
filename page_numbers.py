#!/usr/bin/python
from operator import itemgetter
from itertools import groupby

'''
Problem 34C: http://codeforces.com/problemset/problem/34/C
Solved on: 2015-02-26
Result: Accepted 122 ms 8 KB
'''

def main():
	output=''
	unique=sorted(set(map(int, raw_input().split(','))))
	for i, j in groupby(enumerate(unique), lambda (a,b):a-b):
		lst=map(itemgetter(1),j)
		output+=str(lst[0])+',' if len(lst)==1 else str(lst[0])+'-'+str(lst[-1])+','
	print output[:-1]

if __name__=='__main__':
	main()