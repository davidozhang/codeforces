#!/usr/bin/python

def main():
	result={}
	lst=raw_input().split()
	alien=True
	undetermined=False

	for i in lst:
		if i not in result:
			result[i]=1
		else:
			result[i]+=1
	rem=[]
	for key, val in result.iteritems():
		if val==4:
			alien=False
			undetermined=True
		elif val==5:
			alien=False
			print 'Bear'
			break
		elif val==6:
			alien=False
			print 'Elephant'
			break
		else:
			rem.append(key)

	if alien:
		print 'Alien'
	if undetermined:
		if len(rem)<=1:
			print 'Elephant'
		else:
			print 'Bear'

if __name__=='__main__':
	main()