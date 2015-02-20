#!/usr/bin/python

'''
Problem 339B: http://codeforces.com/problemset/problem/339/B
Solved on: 2015-02-11
Result: Accepted 218 ms 5244 KB
'''

def main():
	n,m=map(int, raw_input().split())
	lst=[]
	result=0
	prev=1
	lst+=map(int, raw_input().split())
	for i in lst:
		if i<prev:
			result+=n-(prev-i)
		elif i>prev:
			result+=i-prev
		prev=i
	print result

if __name__=='__main__':
	main()