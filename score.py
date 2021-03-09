#!/usr/bin/python

from optparse import OptionParser

import score

def main():
	parser = OptionParser()
	parser.add_option("-f", "--file", dest="filename",
		help="Read from FILE", metavar="FILE")
	opts, args = parser.parse_args()
	scores = score.processFile(opts.filename)
	score.showResults(scores)

if __name__ == '__main__':
	main()
