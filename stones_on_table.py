#!/usr/bin/python

'''
Problem 266A: http://codeforces.com/problemset/problem/266/A
Solved on: 2015-02-08
Result: Accepted 92 ms 8 KB
'''

def main():
	n=int(raw_input())
	stack=[]
	result=0
	for i in raw_input():
		stack.append(i)

	for j in range(1,n):
		if stack[j-1]==stack[j]:
			result+=1
	print result

if __name__=='__main__':
	main()