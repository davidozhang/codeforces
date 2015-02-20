#!/usr/bin/python

'''
Problem 75A: http://codeforces.com/problemset/problem/75/A
Solved on: 2015-03-08
Result: Accepted 92 ms 8 KB
'''

def main():
	first, second=raw_input(), raw_input()
	if (int(str(int(first)+int(second)).replace('0','')))==int(first.replace('0',''))+int(second.replace('0','')):
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()