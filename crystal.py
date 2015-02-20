#!/usr/bin/python
import math

'''
Problem 454A: http://codeforces.com/problemset/problem/454/A
Solved on: 2015-02-09
Result: Accepted 46 ms 4 KB
'''

class Crystal:
	def __init__(self, n):
		self.n=n
		self.init_val=int(math.floor(n/2))
		self.lower_half=False
		self.start, self.end=self.init_val, self.init_val

	def draw(self):
		output=''
		for i in range(0, self.n):
			if i>=self.start and i<=self.end:
				output+='D'
			else:
				output+='*'
		if self.start==0 or self.lower_half:
			self.lower_half=True
			self.start+=1
			self.end-=1
		if not self.lower_half:
			self.start-=1
			self.end+=1
		print output

def main():
	n=int(raw_input())
	c=Crystal(n)
	for i in range(0, n):
		c.draw()

if __name__=='__main__':
	main()