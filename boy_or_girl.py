#!/usr/bin/python

def main():
	letters={}
	name=raw_input()
	for i in name:
		letters[i]=1

	if len(letters)%2==0:
		print 'CHAT WITH HER!'
	else:
		print 'IGNORE HIM!'

if __name__=='__main__':
	main()
		