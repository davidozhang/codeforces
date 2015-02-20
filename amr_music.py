#!/usr/bin/python

'''
Problem 507A: http://codeforces.com/problemset/problem/507/A
Solved on: 2015-02-15
Result: Accepted 46 ms 8 KB
'''

def main():
	result={}
	output=0
	output_list=''
	n,k=map(int, raw_input().split())
	lst=map(int, raw_input().split())

	for i in range(0, n):
		if lst[i] not in result:
			result[lst[i]]=1
		else:
			result[lst[i]]+=1

	for key in sorted(result):
		while k-key>=0 and result[key]>0:
			k-=key
			result[key]-=1
			output+=1
			output_list+=str(lst.index(key)+1)+' '
			lst[lst.index(key)]=''
	print output
	if output_list!='':
		print output_list.strip()

if __name__=='__main__':
	main()