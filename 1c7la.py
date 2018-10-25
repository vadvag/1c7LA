#!/usr/bin python3.5
import argparse


def getparser():
	parser =  argparse.ArgumentParser(description='Comand line argument parser')
	parser.add_argument('filename', action='store', help='Name of 1cv77 log file')
	return parser.parse_args()


try:
	args = getparser()
	print(args.filename)
except:
	print('Some Error')
