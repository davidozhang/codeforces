#!/usr/bin/python

def main():
	result={}
	n=int(raw_input())
	for i in range(0, n):
		team=raw_input()
		if team not in result:
			result[team]=1
		else:
			result[team]+=1
	print result.keys()[result.values().index(max(result.values()))]

if __name__=='__main__':
	main()