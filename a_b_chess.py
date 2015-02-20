#!/usr/bin/python

'''
Problem 519A: http://codeforces.com/problemset/problem/519/A
Solved on: 2015-03-08
Result: Accepted 46 ms 20 KB
'''

def main():
	_dict={'Q':9, 'q':9, 'R':5, 'r':5, 'B':3, 'b':3, 'N':3, 'n':3, 'P':1, 'p':1, 'K':0, 'k':0}
	result={'w':0,'b':0}
	for i in range(8):
		for j in raw_input():
			if j!='.' and j.isupper():
				result['w']+=_dict[j]
			elif j!='.' and j.islower():
				result['b']+=_dict[j]
	if result['w']>result['b']:
		print 'White'
	elif result['w']<result['b']:
		print 'Black'
	else:
		print "Draw"

if __name__=='__main__':
	main()