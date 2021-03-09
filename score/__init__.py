#!/usr/bin/python

import sys
import csv
import re
from optparse import OptionParser

def add(scores, key, value):
	score = scores.get(key)
	if score is None:
		score = 0
	if value > 0:
		score += 3
	if value == 0:
		score += 1
	scores[key] = score

def getScore(field):
	value = re.search(" \d$", field)
	if value is None:
		return 0
	return int(value.group(0), 10)

def getName(field):
	key = re.split(" \d$", field)
	if len(key) < 1:
		return ' '
	return key[0].strip()

def readFile(inputfile):
	scores = {}
	reader = csv.reader(inputfile)
	for row in reader:
		if len(row) == 2:
			add(scores, getName(row[0]), getScore(row[0]) - getScore(row[1]))
			add(scores, getName(row[1]), getScore(row[1]) - getScore(row[0]))
	return scores

def processFile(inputfile):
	if inputfile is None:
		return readFile(sys.stdin)
	with open(inputfile) as newfile:
		return readFile(newfile)

def cmpFunc(a, b):
	k1, v1 = a
	k2, v2 = b
	return v1 - v2

def showResults(data):
	list = []
	for key in data:
		list.append((key, data[key]))
	list = sorted(list, key=lambda tup: tup[0])
	list = sorted(list, key=lambda tup: tup[1], reverse=True)
	for entry in list:
		key, value = entry
		print '{}, {} pts'.format(key, value)

