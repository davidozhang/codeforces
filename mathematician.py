#!/usr/bin/python

def main():
	first=raw_input()
	second=raw_input()
	length=len(first)
	result=''

	for i in range(0, length):
		if first[i]==second[i]:
			result+='0'
		else:
			result+='1'

	print result

if __name__=='__main__':
	main()