#!/usr/bin/python

'''
Problem 281A: http://codeforces.com/problemset/problem/281/A
Solved on: 2015-02-08
Result: Accepted 124 ms 4 KB
'''

def main():
	word=raw_input().strip()
	if len(word)>0:
		if ord(word[0])-97>=0:
			print word[0].upper()+word[1:]
		else:
			print word
	else:
		print word

if __name__=='__main__':
	main()