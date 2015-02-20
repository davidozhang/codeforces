#!/usr/bin/python

'''
Problem 231A: http://codeforces.com/problemset/problem/231/A
Solved on: 2015-02-07
Result: Accepted 92 ms 16 KB
'''

def main():
	n=int(raw_input())
	result=0
	for i in range(0, n):
		p,v,t=map(int, raw_input().split())
		if p&v or v&t or p&t:
			result+=1
	print result

if __name__=='__main__':
	main()