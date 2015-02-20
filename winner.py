#!/usr/bin/python

'''
Problem 2A: http://codeforces.com/problemset/problem/2/A
Solved on: 2015-02-28
Result: Accepted 124 ms 56 KB
'''

def main():
	_dict, lst={}, []
	for _ in range(int(raw_input())):
		name, score=raw_input().split()
		if name not in _dict:
			_dict[name]=int(score)
		else:
			_dict[name]+=int(score)
		lst.append((name, _dict[name]))
	_max=max(_dict.values())
	for a, b in lst:
		if b>=_max and _dict[a]==_max:
			print a
			exit()

if __name__=='__main__':
	main()