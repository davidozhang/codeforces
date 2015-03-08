#!/usr/bin/python

'''
Problem 141A: http://codeforces.com/problemset/problem/141/A
Solved on: 2015-02-08
Updated on: 2015-03-08
Result: Accepted 92 ms 8 KB
'''

def add(s):
	result={}
	for i in s:
		if i not in result:
			result[i]=1
		else:
			result[i]+=1
	return result

def main():
	merged=raw_input()+raw_input()
	pile=raw_input()
	merged_count, pile_count=add(merged), add(pile)
	print 'YES' if merged_count==pile_count else 'NO'

if __name__=='__main__':
	main()