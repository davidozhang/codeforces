#!/usr/bin/python

def main():
	n=raw_input()
	if '0000000' in n or '1111111' in n:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()