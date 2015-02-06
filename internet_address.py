#!/usr/bin/python

def main():
	counter=0
	_input=raw_input()

	protocol=_input[:_input.index('p')+1]
	domain=_input[_input.index('p')+1:_input.index('ru', counter)]
	context=''
	while domain=='':
		domain=_input[_input.index('p')+1:_input.index('ru',counter)]
		counter+=1
	if _input.index('ru',counter)+1!=len(_input)-1:
		context=_input[_input.index('ru',counter)+2:]

	output=protocol+'://'+domain+'.ru'
	if context!='':
		output+='/'+context
	print output

if __name__=='__main__':
	main()