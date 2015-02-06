#!/usr/bin/python

def main():
	n=int(raw_input())
	cell=raw_input()
	if cell[0]=='1':
		result=0
		for i in cell:
			if i=='1':
				result+=1
			elif i=='0':
				result+=1
				break
		print result
	else:
		print '1'

if __name__=='__main__':
	main()