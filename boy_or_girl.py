#!/usr/bin/python

'''
Problem 236A: http://codeforces.com/problemset/problem/236/A
Solved on: 2015-02-08
Result: Accepted 122 ms 12 KB
'''

def main():
	letters={}
	name=raw_input()
	for i in name:
		letters[i]=1

	if len(letters)%2==0:
		print 'CHAT WITH HER!'
	else:
		print 'IGNORE HIM!'

if __name__=='__main__':
	main()
		