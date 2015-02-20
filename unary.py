#!/usr/bin/python

'''
Problem 133B: http://codeforces.com/problemset/problem/133/B
Solved on: 2015-03-09
Result: Accepted 122 ms 24 KB
'''

def main():
	_dict={'>':8, '<':9, '+':10, '-':11, '.':12, ',':13, '[':14,']':15}
	result, _input=0, raw_input()
	length=len(_input)
	for i in range(length):
		result+=_dict[_input[i]]*(16**(length-1-i))
	print result%1000003

if __name__=='__main__':
	main()