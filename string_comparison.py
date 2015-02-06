#!/usr/bin/python

def main():
	a=raw_input().lower()
	b=raw_input().lower()

	if a<b:
		print -1
	elif a==b:
		print 0
	else:
		print 1

if __name__=='__main__':
	main()