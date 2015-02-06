#!/usr/bin/python

def main():
	word=raw_input().strip()
	if len(word)>0:
		if ord(word[0])-97>=0:
			print word[0].upper()+word[1:]
		else:
			print word
	else:
		print word

if __name__=='__main__':
	main()