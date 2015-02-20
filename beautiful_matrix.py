#!/usr/bin/python

'''
Problem 263A: http://codeforces.com/problemset/problem/263/A
Solved on: 2015-02-10
Result: Accepted 92 ms 4 KB
'''

def main():
	for i in range(0,5):
		n=raw_input()
		if '1' in n:
			result=str(abs(int(n.replace(' ','').index('1'))-2)+abs(i-2))
	print result
			
if __name__=='__main__':
	main()