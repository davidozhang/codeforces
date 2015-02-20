#!/usr/bin/python

'''
Problem 151B: http://codeforces.com/problemset/problem/151/B
Solved on: 2015-02-18
Result: Accepted 124 ms 84 KB
'''

def _max(_dict, key):
	return max([_dict[i][key] for i in _dict])

def sentence(_dict, lst):
	result, iterate=['','',''], ['taxi','pizza','girl']
	for i in range(3):
		for j in lst:
			if _dict[j][iterate[i]]==_max(_dict, iterate[i]): result[i]+=j+', '
	return [k.strip()[:-1]+'.' for k in result]

def same(item):
	for i in range(1, len(item)):
		if item[i]!=item[i-1]:
			return False
	return True

def decreasing(item):
	for i in range(1, len(item)):
		if item[i]>=item[i-1]:
			return False
	return True

def main():
	order, _dict, iterate=[], {}, ['call a taxi','order a pizza','go to a cafe with a wonderful girl']
	for i in range(int(raw_input())):
		tally={'taxi':0, 'pizza':0, 'girl':0}
		numbers, name=raw_input().split()
		for j in range(int(numbers)):
			phone=''.join(raw_input().split('-'))
			if same(phone): tally['taxi']+=1
			elif decreasing(phone): tally['pizza']+=1
			else: tally['girl']+=1
		_dict[name]=tally
		order.append(name)
	_list=sentence(_dict, order)
	for k in range(3):
		print ('If you want to {0}, you should call: '+_list[k]).format(iterate[k])

if __name__=='__main__':
	main()