#!/usr/bin/python

'''
Problem 110A: http://codeforces.com/problemset/problem/110/A
Solved on: 2015-02-08
Result: Accepted 92 ms 8 KB
'''

def main():
	total=0
	numbers={}
	n=raw_input()
	for i in n:
		if i not in numbers:
			numbers[i]=1
		else:
			numbers[i]+=1

	if '4' in numbers:
		total+=numbers['4']
	if '7' in numbers:
		total+=numbers['7']

	if total==4 or total==7:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()