#!/usr/bin/python

def main():
	output=0
	output_list=[]
	result={1:0,2:0,3:0}
	n=int(raw_input())
	_input=map(int, raw_input().split())

	for i in _input:
		result[i]+=1

	while result[1]>0 and result[2]>0 and result[3]>0:
		result[1],result[2],result[3],output=result[1]-1,result[2]-1,result[3]-1,output+1
		output_list.append(str(_input.index(1)+1)+' '+str(_input.index(2)+1)+' '+str(_input.index(3)+1))
		_input[_input.index(1)],_input[_input.index(2)],_input[_input.index(3)]=0,0,0

	print output
	for i in output_list:
		print i

if __name__=='__main__':
	main()