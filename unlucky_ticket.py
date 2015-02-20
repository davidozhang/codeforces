#!/usr/bin/python

'''
Problem 160B: http://codeforces.com/problemset/problem/160/B
Solved on: 2015-02-22
Result: Accepted 124 ms 4 KB
'''

def main():
	n, ticket=int(raw_input()), raw_input()
	first, second=sorted(ticket[:n]), sorted(ticket[n:])
	less=True if first[0]<second[0] else False
	for a, b in zip(first, second):
		if (less and a>=b) or (not less and a<=b):
			print 'NO'
			exit()
	print 'YES'
	
if __name__=='__main__':
	main()