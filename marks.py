#!/usr/bin/python

'''
Problem 152A: http://codeforces.com/problemset/problem/152/A
Solved on: 2015-03-05
Result: Accepted 77 ms 64 KB
'''

def main():
	lst, result=[], []
	n,m= map(int, raw_input().split())
	for _ in range(n):
		result.append(0)
		lst.append(list(raw_input()))
	for i in zip(*lst):
		for j in [a for a, b in enumerate(i) if b==max(i)]:
			result[j]=1
	print result.count(1)

if __name__=='__main__':
	main()