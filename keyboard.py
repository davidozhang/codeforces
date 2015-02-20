#!/usr/bin/python

'''
Problem 474A: http://codeforces.com/problemset/problem/474/A
Solved on: 2015-02-09
Result: Accepted 46 ms 4 KB
'''

def make(s, direction):
	result={}
	if direction=='L':
		for i in range(0, len(s)-1):
			result[s[i]]=s[i+1]
	elif direction=='R':
		for j in range(1, len(s)):
			result[s[j]]=s[j-1]
	return result

def main():
	merged='qwertyuiopasdfghjkl;zxcvbnm,./'
	output=''
	direction=raw_input()
	string=raw_input()
	result=make(merged, direction)
	for i in string:
		output+=result[i]
	print output

if __name__=='__main__':
	main()