#!/usr/bin/python

'''
Problem 41A: http://codeforces.com/problemset/problem/41/A
Solved on: 2015-02-08
Result: Accepted 92 ms 4 KB
'''

def reverse(word):
	if len(word)==1:
		return word
	return reverse(word[1:])+word[0]

def main():
	s=raw_input()
	if reverse(raw_input())==s:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()