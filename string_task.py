#!/usr/bin/python

'''
Problem 118A: http://codeforces.com/contest/118/problem/A
Solved on: 2015-02-06
Result: Accepted 92 ms 4 KB
'''

def main():
	vowels=['a','e','i','o','u','y']
	input=raw_input()
	result=''
	for i in input:
		if i.lower() not in vowels:
			result+='.'+i.lower()

	print result

if __name__=='__main__':
	main()