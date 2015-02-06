#!/usr/bin/python

class OS:
	def __init__(self):
		self.path=['/']
	def pwd(self):
		output=''
		for i in self.path:
			output+=i
		print output
	def cd(self, lst):
		for i in lst:
			self.path.pop() if i=='..' else self.path.append(i+'/')	

def main():
	os=OS()
	for i in range(int(raw_input())):
		_input=raw_input()
		if _input=='pwd':
			os.pwd()
		else:
			if _input.split()[1].split('/')[0]=='':
				os=OS()
				os.cd(_input.split()[1].split('/')[1:])
			else:
				os.cd(_input.split()[1].split('/'))

if __name__=='__main__':
	main()