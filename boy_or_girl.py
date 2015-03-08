#!/usr/bin/python

'''
Problem 236A: http://codeforces.com/problemset/problem/236/A
Solved on: 2015-02-08
Updated on: 2015-03-08
Result: Accepted 122 ms 12 KB -> 124 ms 4 KB
'''

def main():
	letters=set()
	name=raw_input()
	for i in name:
		letters.add(i)
	print 'CHAT WITH HER!' if len(letters)%2==0 else 'IGNORE HIM!'

if __name__=='__main__':
	main()