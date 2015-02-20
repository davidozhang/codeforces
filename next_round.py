#!/usr/bin/python

'''
Problem 158A: http://codeforces.com/problemset/problem/158/A
Solved on: 2015-02-06
Result: Accepted 122 ms 8 KB
'''

def main():
	c=0
	n,l=map(int, raw_input().split())
	nums=map(int, raw_input().split())
	j=nums[l-1]
	for i in nums:
		if i>=j and i>0:
			c+=1
	print c

if __name__=='__main__':
	main()