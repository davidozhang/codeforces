#!/usr/bin/python

'''
Problem 266B: http://codeforces.com/problemset/problem/266/B
Solved on: 2015-03-09
Result: Accepted 92 ms 4 KB
'''

def main():
	n, t=map(int, raw_input().split())
	queue=raw_input()
	for i in range(t):
		queue=queue.replace('BG','GB')
	print queue

if __name__=='__main__':
	main()