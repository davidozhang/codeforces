#!/usr/bin/python

'''
Problem 59A: http://codeforces.com/problemset/problem/59/A
Solved on: 2015-02-09
Updated on: 2015-03-08
Result: Accepted 154 ms 8 KB
'''

def main():
	upper=lower=0
	word=raw_input()
	for i in word:
		if i.isupper():
			upper+=1
		elif i.islower():
			lower+=1
	print word.upper() if upper>lower else word.lower()

if __name__=='__main__':
	main()