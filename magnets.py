#!/usr/bin/python

'''
Problem 344A: http://codeforces.com/problemset/problem/344/A
Solved on: 2015-02-08
Result: Accepted 186 ms 1604 KB
'''

def main():
	cur=''
	result=0
	n=int(raw_input())
	for i in range(0,n):
		inp=raw_input()
		if inp!=cur:
			cur=inp
			result+=1

	print result

if __name__=='__main__':
	main()