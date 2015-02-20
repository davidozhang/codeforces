#!/usr/bin/python

'''
Problem 465A: http://codeforces.com/problemset/problem/465/A
Solved on: 2015-02-13
Result: Accepted 46 ms 8 KB
'''

def main():
	n=int(raw_input())
	cell=raw_input()
	if cell[0]=='1':
		result=0
		for i in cell:
			if i=='1':
				result+=1
			elif i=='0':
				result+=1
				break
		print result
	else:
		print '1'

if __name__=='__main__':
	main()