#!/usr/bin/python

'''
Problem 452A: http://codeforces.com/problemset/problem/452/A
Solved on: 2015-02-17
Result: Accepted 46 ms 4 KB
'''

def convert(s):
	_dict={}
	counter=0
	for i in s:
		if i!='.':
			_dict[s.index(i, counter)]=i
		counter+=1
	return _dict

def subset(dict1, dict2):
	for key in sorted(dict1):
		if dict1[key]!=dict2[key]:
			return False
	return True

def main():
	names=["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
	n=int(raw_input())
	_dict=convert(raw_input())

	if n==8:
		print names[0]
	elif n==6:
		print names[3]
	else:
		for i in names:
			if subset(_dict, convert(i)):
				print i
				break

if __name__=='__main__':
	main()