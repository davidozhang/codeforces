#!/usr/bin/python

def main():
	n=int(raw_input())
	val=0
	for i in range(0, n):
		input=raw_input()
		if input[0]=='+' or input[-1:]=='+':
			val+=1
		elif input[0]=='-' or input[-1:]=='-':
			val-=1
	print val

if __name__=='__main__':
	main()