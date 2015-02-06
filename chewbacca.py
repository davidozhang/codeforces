#!/usr/bin/python

def main():
	result=''
	n=raw_input()
	counter=0
	for i in n:
		num=int(i)
		if 9-num<num and len(n)>1:
			result+=str(9-num)
			if int(result)<=0:
				result=result[:-1]+str(num)
		else:
			result+=str(num)
		counter+=1
	print result

if __name__=='__main__':
	main()