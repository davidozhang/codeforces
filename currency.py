#!/usr/bin/python

'''
Problem 508B: http://codeforces.com/problemset/problem/508/B
Solved on: 2015-02-23
Result: Accepted 234 ms 2256 KB
'''

def swap(s, a, b):
	lst=list(s)
	lst[a],lst[b]=lst[b],lst[a]
	print ''.join(lst)

def main():
	even, n=-1, raw_input()
	for i in range(len(n)):
		if int(n[i])%2==0 and int(n[i])<int(n[-1]):
			swap(n,i,-1)
			exit()
		elif int(n[i])%2==0:
			even=i
	if even==-1:
		print -1
 	else:
 		swap(n,even,-1)

if __name__=='__main__':
	main()