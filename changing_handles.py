#!/usr/bin/python

'''
Problem 501B: http://codeforces.com/problemset/problem/501/B
Solved on: 2015-02-23
Result: Accepted 61 ms 200 KB
'''

def main():
	old, _dict=[], {}
	for _ in range(int(raw_input())):
		a,b=raw_input().split()
		_dict[a]=b
		if a not in _dict.values():
			old.append(a)
	print len(old)
	for i in old:
		val=_dict[i]
		while val in _dict:
			val=_dict[val]
		print i, val

if __name__=='__main__':
	main()