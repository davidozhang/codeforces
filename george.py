#!/usr/bin/python

def main():
	n=int(raw_input())
	output=0
	for i in range(0, n):
		occ,cap=map(int, raw_input().split())
		if cap-occ>=2:
			output+=1

	print output

if __name__=='__main__':
	main()