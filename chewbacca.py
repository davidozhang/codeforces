#!/usr/bin/python

'''
Problem 514A: http://codeforces.com/problemset/problem/514/A
Solved on: 2015-02-15
Result: Accepted 62 ms 8 KB
'''

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