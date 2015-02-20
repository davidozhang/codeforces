#!/usr/bin/python

'''
Problem 339A: http://codeforces.com/problemset/problem/339/A
Solved on: 2015-02-15
Result: Accepted 124 ms 4 KB
'''

def main():
	result={1:0, 2:0, 3:0}
	output=''
	_input=map(int, raw_input().split('+'))

	for i in _input:
		result[i]+=1

	for key in sorted(result):
		while result[key]>0:
			output+=str(key)+'+'
			result[key]-=1

	print output[:-1]

if __name__=='__main__':
	main()