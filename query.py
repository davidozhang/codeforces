#!/usr/bin/python

'''
Problem 313B: http://codeforces.com/problemset/problem/313/B
Solved on: 2015-02-22
Result: Accepted 748 ms 3616 KB
'''

def main():
	result, s=[0]*100005, raw_input()
	for i in range (1, len(s)):
		result[i] = result[i-1] + (s[i]==s[i-1])
	for _ in range(int(raw_input())):
		l, r=map(int, raw_input().split())
		print result[r-1]-result[l-1]

if __name__=='__main__':
	main()