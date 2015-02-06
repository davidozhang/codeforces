#!/usr/bin/python

def main():
	n=int(raw_input())
	soldiers=map(int, raw_input().split())
	maximum=max(soldiers)
	for i in range(0, n):
		if soldiers[i]==maximum:
			max_index=i
			break
	minimum=min(soldiers)
	for j in reversed(range(0, n)):
		if soldiers[j]==minimum:
			min_index=j
			break
			
	result=max_index+abs(min_index-(n-1))
	if min_index<max_index:
		print result-1
	else:
		print result

if __name__=='__main__':
	main()