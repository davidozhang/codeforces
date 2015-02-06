#!/usr/bin/python

def main():
	n=int(raw_input())
	result=0
	for i in range(0, n):
		p,v,t=map(int, raw_input().split())
		if p&v or v&t or p&t:
			result+=1
	print result

if __name__=='__main__':
	main()