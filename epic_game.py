#!/usr/bin/python

class Game:
	def __init__(self,a,b,n):
		self.bool=1
		self.a=a
		self.b=b
		self.n=n

	def check(self):
		return gcd(self.a,self.n) if self.bool else gcd(self.b,self.n)

def gcd(a,b):
	return a if b==0 else gcd(b, a%b)

def main():
	a,b,n=map(int, raw_input().split())
	g=Game(a,b,n)

	while g.n>=g.check():
		g.n-=g.check()
		g.bool=g.bool^1

	print g.bool

if __name__=='__main__':
	main()