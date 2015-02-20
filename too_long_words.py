#!/usr/bin/python

'''
Problem 71A: http://codeforces.com/problemset/problem/71/A
Solved on: 2015-02-06
Result: Accepted 92 ms 4 KB
'''

def main():
	n=int(raw_input())
	for i in range (0, n):
		w=raw_input()
		if len(w)>10:
			print w[0]+str(len(w)-2)+w[-1:]
		else:
			print w

if __name__=='__main__':
	main()