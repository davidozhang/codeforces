#!/usr/bin/python

'''
Problem 127B: http://codeforces.com/problemset/problem/127/B
Solved on: 2015-02-28
Result: Accepted 92 ms 8 KB
'''

def main():
	_dict, num={}, 0
	if int(raw_input())<4:
		print 0
	else:
		for i in raw_input().split():
			if i not in _dict:
				_dict[i]=1
			else:
				_dict[i]+=1
		for i in _dict:
			num+=_dict[i]/2
			_dict[i]%=2
		print num/2 if num%2==0 else (num-1)/2

if __name__=='__main__':
	main()