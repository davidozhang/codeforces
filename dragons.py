#!/usr/bin/python

'''
Problem 230A: http://codeforces.com/problemset/problem/230/A
Solved on: 2015-02-15
Result: Accepted 92 ms 72 KB
'''

def main():
	result={}
	succeed=True
	strength, n=map(int, raw_input().split())
	for i in range(0,n):
		dragon_strength, bonus=map(int, raw_input().split())
		if dragon_strength not in result:
			result[dragon_strength]=bonus
		else:
			result[dragon_strength]+=bonus

	for key in sorted(result):
		if strength>key:
			strength+=result[key]
		if strength<=key:
			succeed=False
			break
	if succeed:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()