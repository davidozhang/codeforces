#!/usr/bin/python

'''
Problem 237A: http://codeforces.com/problemset/problem/237/A
Solved on: 2015-03-08
Result: Accepted 186 ms 1748 KB
'''

def main():
	_dict={}
	for _ in range(int(raw_input())):
		_input=raw_input()
		if _input not in _dict:
			_dict[_input]=1
		else:
			_dict[_input]+=1
	print max(_dict.values())

if __name__=='__main__':
	main()