#!/usr/bin/python

def main():
	success=True
	for i in range(0,3):
		_dict={}
		_input=''.join(raw_input().split())
		for j in _input:
			if j not in _dict:
				_dict[j]=1
			else:
				_dict[j]+=1
		vowel_count=0
		vowel_count=_dict.get('a',0)+_dict.get('e',0)+_dict.get('i',0)+_dict.get('o',0)+_dict.get('u',0)
		if (i%2==0 and vowel_count!=5) or (i%2==1 and vowel_count!=7):
			success=False

	if success:
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()