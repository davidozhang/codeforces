#!/usr/bin/python

def main():
	n=int(raw_input())
	for i in range (0, n):
		w=raw_input()
		if len(w)>10:
			print w[0]+str(len(w)-2)+w[-1:]
		else:
			print w

if __name__=='__main__':
	main()