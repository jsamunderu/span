#!/usr/bin/python

import unittest
import sys
import os.path
from os import path
from cStringIO import StringIO

import score

class TestScore(unittest.TestCase):
	def test_getScore(self):
		# positive test
		self.assertEqual(score.getScore("Lions 3"), 3)

	def test_getName(self):
		# positive test
		want = 'Lions'
		got = score.getName("Lions 3")
		self.assertEqual(got, want)

	def test_add(self):
		# positive test
		row = ['Lions 3', ' Snakes 3']
		got = {}
		want = {'Lions': 1}
		score.add(got, score.getName(row[0]), score.getScore(row[0]) - score.getScore(row[1]))
		value = {k: want[k] for k in want if k in got and want[k] == got[k]}
		self.assertEqual(len(value), 1)

		# negative test
		got = {}
		want = {'Tarantulas': 1}
		score.add(got, score.getName(row[0]), score.getScore(row[0]) - score.getScore(row[1]))
		value = {k: want[k] for k in want if k in got and want[k] == got[k]}
		self.assertEqual(len(value), 0)

	def test_readFile(self):
		str = ("Lions 3, Snakes 3\n"
		"Tarantulas 1, FC Awesome 0\n")
		
		inputfile = StringIO(str)
		want = {'Tarantulas': 3, 'FC Awesome': 0, 'Lions': 1, 'Snakes': 1}
		got = score.readFile(inputfile)
		value = {k: want[k] for k in want if k in got and want[k] == got[k]}
		self.assertEqual(len(value), 4)

	def test_processFile(self):
		if path.exists('input.txt'):
			want = {'Tarantulas': 6, 'FC Awesome': 1, 'Lions': 5, 'Snakes': 1, 'Grouches': 0}
			got = score.processFile('input.txt')
			value = {k: want[k] for k in want if k in got and want[k] == got[k]}
			self.assertEqual(len(value), 5)

		str = ("Lions 3, Snakes 3\n"
		"Tarantulas 1, FC Awesome 0\n"
		"Lions 1, FC Awesome 1\n"
		"Tarantulas 3, Snakes 1\n"
		"Lions 4, Grouches 0\n")
		sys.stdin = StringIO(str)
		want = {'Tarantulas': 6, 'FC Awesome': 1, 'Lions': 5, 'Snakes': 1, 'Grouches': 0}
		got = score.processFile(None)
		value = {k: want[k] for k in want if k in got and want[k] == got[k]}
		self.assertEqual(len(value), 5)

if __name__ == '__main__':
	unittest.main()
