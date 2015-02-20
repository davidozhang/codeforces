#!/usr/bin/python

'''
Problem 349A: http://codeforces.com/problemset/problem/349/A
Solved on: 2015-02-15
Result: Accepted 248 ms 3836 KB
'''

def main():
	result={25:0, 50:0, 100:0}
	success=True
	n=int(raw_input())
	_input=map(int, raw_input().split())

	for i in _input:
		if i==50:
			if result[25]==0:
				success=False
			else:
				result[25]-=1
		elif i==100:
			if result[50]==0:
				if result[25]<3:
					success=False
				else:
					result[25]-=3
			else:
				if result[25]==0:
					success=False
				else:
					result[25]-=1
					result[50]-=1
		result[i]+=1

	if success:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()