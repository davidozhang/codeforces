#!/usr/bin/python

'''
Problem 43A: http://codeforces.com/problemset/problem/43/A
Solved on: 2015-02-16
Result: Accepted 92 ms 4 KB
'''

def main():
	result={}
	n=int(raw_input())
	for i in range(0, n):
		team=raw_input()
		if team not in result:
			result[team]=1
		else:
			result[team]+=1
	print result.keys()[result.values().index(max(result.values()))]

if __name__=='__main__':
	main()