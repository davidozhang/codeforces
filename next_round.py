#!/usr/bin/python

def main():
	c=0
	n,l=map(int, raw_input().split())
	nums=map(int, raw_input().split())
	j=nums[l-1]
	for i in nums:
		if i>=j and i>0:
			c+=1
	print c

if __name__=='__main__':
	main()