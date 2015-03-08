#!/usr/bin/python

'''
Problem 71A: http://codeforces.com/problemset/problem/71/A
Solved on: 2015-02-06
Updated on: 2015-03-08
Result: Accepted 92 ms 4 KB
'''

def main():
	n=int(raw_input())
	for i in range (n):
		w=raw_input()
		print w[0]+str(len(w)-2)+w[-1:] if len(w)>10 else w

if __name__=='__main__':
	main()