#!/usr/bin/python

'''
Problem 334A: http://codeforces.com/problemset/problem/334/A
Solved on: 2015-02-13
Result: Accepted 124 ms 84 KB
'''

def main():
	n=int(raw_input())
	maximum=n**2
	for i in range(0, (n**2)/2):
		print str(i+1)+' '+str(maximum-i)

if __name__=='__main__':
	main()