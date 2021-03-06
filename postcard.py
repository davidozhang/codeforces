#!/usr/bin/python

'''
Problem 518B: http://codeforces.com/problemset/problem/518/B
Solved on: 2015-02-29
Result: Accepted 233 ms 12372 KB
'''

def main():
	_dict, _used, y, w, first={}, {}, 0, 0, list(raw_input())
	for i in list(raw_input()):
		if i not in _dict:
			_dict[i]=1
		else:
			_dict[i]+=1
	for i, j in enumerate(first):
		if j in _dict and _dict[j]>0:
			y+=1
			_dict[j]-=1
			_used[i]=1
	for i, j in enumerate(first):
		if i not in _used:
			j=j.upper() if j.islower() else j.lower()
			if j in _dict and _dict[j]>0:
				w+=1
				_dict[j]-=1
	print y, w

if __name__=='__main__':
	main()