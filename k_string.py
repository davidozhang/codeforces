#!/usr/bin/python

def main():
	result={}
	output=''
	success=True
	k=int(raw_input())
	_input=raw_input()

	for i in _input:
		if i not in result:
			result[i]=1
		else:
			result[i]+=1

	for key in sorted(result):
		if result[key]%k==0:
			output+=key*(result[key]/k)
		else:
			success=False
			break

	if success:
		print output*k
	else:
		print '-1'

if __name__=='__main__':
	main()