#!/usr/bin/python

def main():
	for i in range(0,5):
		n=raw_input()
		if '1' in n:
			result=str(abs(int(n.replace(' ','').index('1'))-2)+abs(i-2))
	print result
			
if __name__=='__main__':
	main()