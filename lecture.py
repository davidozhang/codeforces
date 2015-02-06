#!/usr/bin/python

def main():
	result={}
	output=''
	n,m=map(int, raw_input().split())
	for i in range(0, m):
		first, second=raw_input().split()
		result[first]=second
	_input=raw_input().split()

	for i in _input:
		if len(i)<=len(result[i]):
			output+=i+' '
		else:
			output+=result[i]+' '

	print output.strip()

if __name__=='__main__':
	main()