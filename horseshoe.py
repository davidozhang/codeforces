#!/usr/bin/python

'''
Problem 228A: http://codeforces.com/problemset/problem/228/A
Solved on: 2015-02-08
Result: Accepted 92 ms 8 KB
'''

def main():
	result={}
	output=0

	for i in map(int, raw_input().split()):
		if i not in result:
			result[i]=1
		else:
			result[i]+=1

	for key, val in result.iteritems():
		if val>1:
			output+=val-1

	print output

if __name__=='__main__':
	main()