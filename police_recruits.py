#!/usr/bin/python

def main():
	n=int(raw_input())
	events=raw_input().split()
	crimes=0
	officers=0
	for i in range(0,n):
		if events[i]=='-1' and officers==0:
			crimes+=1
		elif events[i]=='-1' and officers>0:
			officers-=1
		else:
			officers+=int(events[i])

	print crimes

if __name__=='__main__':
	main()