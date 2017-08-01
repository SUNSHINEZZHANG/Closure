#!/usr/bin/env python
#-*-coding:utf-8 -*-
#闭包
def count():
	fs=[]
	for j in range(1,4):
		def f(j):
			def g():
				return j*j
			return g
		fs.append(f(j))
	return fs

f1,f2,f3 = count()
print f1(),f2(),f3()