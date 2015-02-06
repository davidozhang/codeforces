#!/usr/bin/python
import math

def main():
	result=[]
	flag=True
	n=int(raw_input())
	if n%2==0:
		print (n**2)/2
	else:
		print (int(math.floor(n/2.0)))**2+(int(math.ceil(n/2.0)))**2
	first='C.'*(n/2)
	second='.C'*(n/2)
	if n%2!=0:
		first+='C'
		second+='.'
	for i in range(0,n):
		if flag:
			print first
		else:
			print second
		flag=flag^1

if __name__=='__main__':
	main()