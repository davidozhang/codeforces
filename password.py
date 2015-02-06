#!/usr/bin/python

def slice(s):
	_list=[]
	i=0
	while i<80:
		_list.append(s[i:i+10])
		i+=10
	return _list

def main():
	_dict={}
	output=''
	pwd_list=slice(raw_input())
	
	for i in range(0, 10):
		_dict[raw_input()]=str(i)

	for j in pwd_list:
		output+=_dict[j]

	print output

if __name__=='__main__':
	main()