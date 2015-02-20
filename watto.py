#!/usr/bin/python

'''
Problem 514C: http://codeforces.com/problemset/problem/514/C
Solved on: INCOMPLETE
Result:
'''

def hash(s):
	result=''
	for i in s:
		if i=='a':
			result+='97'
		elif i=='b':
			result+='98'
		else:
			result+='99'
	return int(result)

def check(a,b):
	diff=abs(a-b)
	if diff==0:
		return False
	if diff%(10**(len(str(diff))-1))==0:
		return True
	return False

def main():
	n,m=map(int,raw_input().split())
	memory=[]
	for i in range(0, n):
		memory.append(hash(raw_input()))
	for i in range(0,m):
		result=False
		query=hash(raw_input())
		for j in memory:
			if len(str(query))==len(str(j)):
				if check(query,j):
					result=True
					break
		if result:
			print 'YES'
		else:
			print 'NO'

if __name__=='__main__':
	main()