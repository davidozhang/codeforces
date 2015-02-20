#!/usr/bin/python

'''
Problem 102B: http://codeforces.com/problemset/problem/102/B
Solved on: 2015-03-08
Result: Accepted 186 ms 1192 KB
'''

def main():
	result=0
	n=[int(i) for i in raw_input()]
	while len(n)>1:
		n=[int(i) for i in str(sum(n))]
		result+=1
	print result

if __name__=='__main__':
	main()