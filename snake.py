#!/usr/bin/python

def main():
	n, m=map(int, raw_input().split())
	body='#'*m
	trans1='.'*(m-1)+'#'
	trans2='#'+'.'*(m-1)
	bodyFlag=True
	transFlag=True
	counter=0
	while counter<=n-1:
		if bodyFlag:
			print body
			bodyFlag=False
		else:
			bodyFlag=True
			if transFlag:
				print trans1
			elif not transFlag:
				print trans2
			transFlag=transFlag^1
		counter+=1

if __name__=='__main__':
	main()