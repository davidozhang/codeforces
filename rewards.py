#!/usr/bin/python
import math

def main():
	fc, sc, tc=map(int, raw_input().split())
	fm, sm, tm=map(int, raw_input().split())

	cup_shelves=int(math.ceil((fc+sc+tc)/5.0))
	medal_shelves=int(math.ceil((fm+sm+tm)/10.0))

	if (cup_shelves+medal_shelves)<=int(raw_input()):
		print 'YES'
	else:
		print 'NO'

if __name__=='__main__':
	main()