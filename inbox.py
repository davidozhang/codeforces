#!/usr/bin/python

def traverse(lst):
	count, check=0, False
	for i in range(len(lst)):
		if lst[i]==1:
			check=True
			count+=1
		else:
			if check and i+1<=len(lst)-1 and lst[i+1]==1:
				count+=1
	return count

def main():
	n=int(raw_input())
	print traverse(map(int, raw_input().split()))

if __name__=='__main__':
	main()