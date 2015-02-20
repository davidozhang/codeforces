#!/usr/bin/python

'''
Problem 318B: http://codeforces.com/problemset/problem/318/B
Solved on: 2015-03-05
Result: Accepted 248 ms 5604 KB
'''

def main():
	result, lst = 0, raw_input().split('heavy')
	for i in range(len(lst)):	
		result+=lst[i].count('metal')*i
	print result

if __name__=='__main__':
	main()