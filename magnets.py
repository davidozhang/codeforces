#!/usr/bin/python

def main():
	cur=''
	result=0
	n=int(raw_input())
	for i in range(0,n):
		inp=raw_input()
		if inp!=cur:
			cur=inp
			result+=1

	print result

if __name__=='__main__':
	main()