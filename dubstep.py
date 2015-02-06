#!/usr/bin/python

def main():
	n=raw_input()
	result=n.split('WUB')
	output=''
	for i in result:
		output+=i+' '
	print output.replace('  ',' ').strip()

if __name__=='__main__':
	main()