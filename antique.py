#!/usr/bin/python

def main():
	n, v=map(int, raw_input().split())
	nums=[]
	result=0
	for i in range(0, n):
		deal=False
		seller=map(int, raw_input().split())
		for j in range(1, seller[0]+1):
			if seller[j]<v:
				deal=True
				nums.append(i+1)
				break
		if deal:
			result+=1
	print result
	if result!=0:
		output=''
		for i in map(str, nums):
			output+=i+' '
		print output.strip()

if __name__=='__main__':
	main()