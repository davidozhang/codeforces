#!/usr/bin/python

'''
Problem 141A: http://codeforces.com/problemset/problem/141/A
Solved on: 2015-02-08
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
	merged_count=add(merged)
	pile_count=add(pile)

	if merged_count==pile_count:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()