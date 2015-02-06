#!/usr/bin/python

def main():
	caps=True
	word=raw_input()
	if len(word)>1:
		for i in word[1:]:
			if i.islower():
				caps=False
				break
	if word[0].islower() and caps:
		print word[0].upper()+word[1:].lower()
	elif word[0].isupper() and caps:
		print word.lower()
	else:
		print word

if __name__=='__main__':
	main()