#!/usr/bin/python

'''
Problem 186A: http://codeforces.com/problemset/problem/186/A
Solved on: 2015-02-17
Result: Accepted 218 ms 2224 KB
'''

def main():
	difference=0
	first=raw_input()
	second=raw_input()

	for i in range(0, min(len(first), len(second))):
		if first[i]!=second[i]:
			difference+=1

	if ''.join(sorted(first))==''.join(sorted(second)) and difference==2:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()