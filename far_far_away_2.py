#!/usr/bin/python

'''
Problem 143B: http://codeforces.com/problemset/problem/143/B
Solved on: 2015-02-21
Result: Accepted 92 ms 8 KB
'''

def negative(s):
	return '('+s.replace('-','')+')'

def commafy(s):
	return '{:,}'.format(int(s))

def process(lst=None, _str=None, _neg=False):
	if lst:
		integer=commafy(lst[0])
		decimal=lst[1]+'0' if len(lst[1])<2 else lst[1][:2]
	else:
		integer=commafy(_str)
		decimal='00'
	print negative('${0}.{1}'.format(integer, decimal)) if _neg else '${0}.{1}'.format(integer, decimal)

def main():
	n=raw_input()
	process(lst=n.split('.'), _neg=n.split('.')[0][0]=='-') if '.' in n else process(_str=n, _neg=n[0]=='-')

if __name__=='__main__':
	main()