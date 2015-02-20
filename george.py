#!/usr/bin/python

'''
Problem 467A: http://codeforces.com/problemset/problem/467/A
Solved on: 2015-02-09
Result: Accepted 46 ms 4 KB
'''

def main():
	n=int(raw_input())
	output=0
	for i in range(0, n):
		occ,cap=map(int, raw_input().split())
		if cap-occ>=2:
			output+=1

	print output

if __name__=='__main__':
	main()