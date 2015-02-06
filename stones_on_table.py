#!/usr/bin/python

def main():
	n=int(raw_input())
	stack=[]
	result=0
	for i in raw_input():
		stack.append(i)

	for j in range(1,n):
		if stack[j-1]==stack[j]:
			result+=1
	print result

if __name__=='__main__':
	main()