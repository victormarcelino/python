#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fatorial(n):
	"""fatorial
	Computa o fatorial de um número inteiro positivo.
	"""
	fat = 1
	for i in range(1, n+1):
		fat = fat * i
	return fat
