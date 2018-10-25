#!/usr/bin python3.5
import argparse
import view
import logger


def getparser():
	parser =  argparse.ArgumentParser(description='Comand line argument parser')
	parser.add_argument('filename', action='store', help='Name of 1cv77 log file')
	return parser.parse_args()


viewer = view.Viewer()
logger = logger.Logger()
try:
	args = getparser()
	viewer.print(args.filename)
except:
	viewer.print('Some Error')
