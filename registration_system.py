#!/usr/bin/python

'''
Problem 4C: http://codeforces.com/problemset/problem/4/C
Solved on: 2015-02-22
Result: Accepted 374 ms 2632 KB
'''

def add(_input, system):
	if _input not in system:
		system[_input]=1
		print 'OK'
	else:
		print _input+str(system[_input])
		system[_input]+=1

def main():
	system={}
	for i in range(int(raw_input())):
		add(raw_input(), system)

if __name__=='__main__':
	main()