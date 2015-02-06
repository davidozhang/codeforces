#!/usr/bin/python

def main():
	input = raw_input()
	if int(input)>2 and int(input)%2==0:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()