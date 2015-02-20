#!/usr/bin/python

'''
Problem 160A: http://codeforces.com/problemset/problem/160/A
Solved on: 2015-02-15
Result: Accepted 124 ms 4 KB
'''

def main():
	result={}
	output=0
	individual_sum=0
	_sum=0
	n=int(raw_input())
	_input=map(int, raw_input().split())

	for i in _input:
		_sum+=i
		if i not in result:
			result[i]=1
		else:
			result[i]+=1

	for key in reversed(sorted(result)):
		while individual_sum<=_sum-individual_sum and result[key]>0:
			result[key]-=1
			individual_sum+=key
			output+=1
	print output

if __name__=='__main__':
	main()