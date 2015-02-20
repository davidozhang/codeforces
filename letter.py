#!/usr/bin/python

'''
Problem 43B: http://codeforces.com/problemset/problem/43/B
Solved on: 2015-02-24
Result: Accepted 92 ms 4 KB
'''

def add(s):
	_dict={}
	for i in s:
		for j in i:
			try:
				_dict[j]+=1
			except KeyError:
				_dict[j]=1
	return _dict

def main():
	first=add(raw_input().split())
	for i in raw_input().split():
		for j in i:
			if j not in first or first[j]==0:
				print 'NO'
				exit()
			else:
				first[j]-=1
	print 'YES'

if __name__=='__main__':
	main()