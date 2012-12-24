#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Foo(object):

	def __init__(self, bar=23):
		self.bar = bar

	@property
	def bar(self):
		return self._bar

	@bar.setter
	def bar(self, bar):
		self._bar = int(bar)
