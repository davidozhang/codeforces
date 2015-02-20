#!/usr/bin/python

'''
Problem 465B: http://codeforces.com/problemset/problem/465/B
Solved on: 2015-02-20
Result: Accepted 46 ms 20 KB
'''

def traverse(lst):
	count, check=0, False
	for i in range(len(lst)):
		if lst[i]==1:
			check=True
			count+=1
		else:
			if check and i+1<=len(lst)-1 and lst[i+1]==1:
				count+=1
	return count

def main():
	n=int(raw_input())
	print traverse(map(int, raw_input().split()))

if __name__=='__main__':
	main()