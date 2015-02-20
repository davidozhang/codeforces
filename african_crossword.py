#!/usr/bin/python

'''
Problem 90B: http://codeforces.com/problemset/problem/90/B
Solved on: 2015-02-25
Result: Accepted 124 ms 88 KB
'''

def main():
	output=''
	n,m=map(int, raw_input().split())
	rows=[list(raw_input()) for _ in range(n)]
	columns=[list(i) for i in zip(*rows)]
	for i in range(n):
		for j in range(m):
			elem=rows[i][j]
			if rows[i].count(elem)+columns[j].count(elem)==2:
				output+=elem
	print output

if __name__=='__main__':
	main()