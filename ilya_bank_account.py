#!/usr/bin/python

'''
Problem 313A: http://codeforces.com/problemset/problem/313/A
Solved on: 2015-03-08
Result: Accepted 92 ms 4 KB
'''

def main():
	n=raw_input()
	print n if n[0]!='-' else max(int(n[:-1]), int(n[:-2]+n[-1]))

if __name__=='__main__':
	main()