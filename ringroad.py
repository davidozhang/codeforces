#!/usr/bin/python

def main():
	n,m=map(int, raw_input().split())
	lst=[]
	result=0
	prev=1
	lst+=map(int, raw_input().split())
	for i in lst:
		if i<prev:
			result+=n-(prev-i)
		elif i>prev:
			result+=i-prev
		prev=i
	print result

if __name__=='__main__':
	main()