#!/usr/bin/python

def main():
	result={}
	s=raw_input()

	for i in s:
		result[i]=1

	if 'H' in result or 'Q' in result or '9' in result:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()