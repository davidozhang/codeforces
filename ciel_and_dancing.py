#!/usr/bin/python

'''
Problem 322A: http://codeforces.com/problemset/problem/322/A
Solved on: 2015-02-22
Result: Accepted 154 ms 16 KB
'''

def main():
	result=[]
	b,g=map(int,raw_input().split())
	boy, girl={k:False for k in range(1, b+1)}, {k:False for k in range(1, g+1)}
	for i in range(1, b+1):
		for j in range(1, g+1):
			if not boy[i] or not girl[j]:
				result.append(str(i)+' '+str(j))
				boy[i], girl[j]=True, True
	print b+g-1
	for i in result:
		print i

if __name__=='__main__':
	main()