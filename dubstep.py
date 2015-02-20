#!/usr/bin/python

'''
Problem 208A: http://codeforces.com/problemset/problem/208/A
Solved on: 2015-02-08
Result: Accepted 92 ms 4 KB
'''

def main():
	n=raw_input()
	result=n.split('WUB')
	output=''
	for i in result:
		output+=i+' '
	print output.replace('  ',' ').strip()

if __name__=='__main__':
	main()