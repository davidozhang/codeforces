#!/usr/bin/python

'''
Problem 63A: http://codeforces.com/problemset/problem/63/A
Solved on: 2015-02-16
Result: Accepted 92 ms 8 KB
'''

def main():
	order=['rat','woman/child','man','captain']
	result={}
	n=int(raw_input())
	for i in range(0, n):
		name, pos=raw_input().split()
		if pos=='woman' or pos=='child':
			pos='woman/child'
		if pos not in result:
			result[pos]=[]
		result[pos].append(name)

	for i in order:
		if i in result:
			for j in result[i]:
				print j

if __name__=='__main__':
	main()