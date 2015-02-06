#!/usr/bin/python

def main():
	vowels=['a','e','i','o','u','y']
	input=raw_input()
	result=''
	for i in input:
		if i.lower() not in vowels:
			result+='.'+i.lower()

	print result

if __name__=='__main__':
	main()