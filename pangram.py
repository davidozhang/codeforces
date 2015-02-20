#!/usr/bin/python
import string

'''
Problem 520A: http://codeforces.com/problemset/problem/520/A
Solved on: 2015-03-07
Result: Accepted 61 ms 396 KB
'''

def main():
	letters = set(string.ascii_lowercase)
	n=input()
	for i in raw_input().lower():
		try:
			letters.remove(i)
		except KeyError:
			pass
	print 'NO' if len(letters)>0 else 'YES'

if __name__=='__main__':
	main()