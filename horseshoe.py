#!/usr/bin/python

def main():
	result={}
	output=0

	for i in map(int, raw_input().split()):
		if i not in result:
			result[i]=1
		else:
			result[i]+=1

	for key, val in result.iteritems():
		if val>1:
			output+=val-1

	print output

if __name__=='__main__':
	main()