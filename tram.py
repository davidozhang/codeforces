#!/usr/bin/python

def main():
	n=int(raw_input())
	num=0
	max=0
	for i in range(0, n):
		off, on = map(int, raw_input().split())
		num=num+on-off
		if num>max:
			max=num

	print max

if __name__=='__main__':
	main()