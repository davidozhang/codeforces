#!/usr/bin/python
from math import floor

def main():
	n=int(raw_input())

	if n%2==0:
		print n/2
	else:
		print int(floor(n/2)-n)

if __name__=='__main__':
	main()