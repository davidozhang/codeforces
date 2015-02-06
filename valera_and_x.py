#!/usr/bin/python
from sets import Set

def check(s):
	return True if len(s)==1 else False

def main():
	success, diag, others=True, set(), set()
	n=int(raw_input())
	pointer_1, pointer_2=0, n-1
	for _ in range(n):
		row=raw_input()
		diag.add(row[pointer_1])		
		diag.add(row[pointer_2])
		for i in range(n):
			if i!=pointer_1 and i!=pointer_2:
				others.add(row[i])
		if not check(diag) or not check(others) or len(diag.intersection(others))!=0:
			success=False
			break
		pointer_1, pointer_2=pointer_1+1, pointer_2-1

	print 'YES' if success else 'NO'

if __name__=='__main__':
	main()