#!/usr/bin/python

'''
Problem 282A: http://codeforces.com/contest/282/problem/A
Solved on: 2015-02-07
Result: Accepted 62 ms 8 KB
'''

def main():
	n=int(raw_input())
	val=0
	for i in range(0, n):
		input=raw_input()
		if input[0]=='+' or input[-1:]=='+':
			val+=1
		elif input[0]=='-' or input[-1:]=='-':
			val-=1
	print val

if __name__=='__main__':
	main()