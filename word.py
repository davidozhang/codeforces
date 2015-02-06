#!/usr/bin/python

def main():
	word=raw_input()
	upper=0
	lower=0
	for i in word:
		if i.isupper():
			upper+=1
		elif i.islower():
			lower+=1

	if upper>lower:
		print word.upper()
	elif upper<=lower:
		print word.lower()

if __name__=='__main__':
	main()