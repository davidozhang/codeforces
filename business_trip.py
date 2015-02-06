#!/usr/bin/python

def main():
	result={}
	output=0
	_sum=0
	_break=False
	k=int(raw_input())
	months=map(int, raw_input().split())

	for i in months:
		_sum+=i
		if i not in result:
			result[i]=1
		else:
			result[i]+=1
	if _sum<k:
		print '-1'
	else:
		for key in reversed(sorted(result)):
			while k!=0 and result[key]>0:
				result[key]-=1
				k-=key
				output+=1
				if k<=0:
					_break=True
					break
			if _break:
				break
		print output

if __name__=='__main__':
	main()