#!/usr/bin/python

'''
Problem 59A: http://codeforces.com/problemset/problem/59/A
Solved on: 2015-02-09
Result: Accepted 154 ms 8 KB
'''

def main():
	word=raw_input()
	upper=0
	lower=0
	for i in word:
		if i.isupper():
			upper+=1
		elif i.islower():
			lower+=1

	if upper>lower:
		print word.upper()
	elif upper<=lower:
		print word.lower()

if __name__=='__main__':
	main()