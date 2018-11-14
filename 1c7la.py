#!/usr/bin python3.5
import argparse
import view
import logger
import Hoster


def getparser():
    parser =  argparse.ArgumentParser(description='Comand line argument parser')
    parser.add_argument('-imp', action='store', dest='filename', help='Import Name of 1cv77 log file')
    parser.add_argument('-usr', action='store', dest='u_date', help='Date for show user-chart')
    parser.add_argument('-err', action='store', dest='e_date', help='Date for show errors-chart')
    return parser.parse_args()

viewer = view.Viewer()
db = Hoster.DB()
logger = logger.Logger(db)
try:
    args = getparser()
    print(args)
    if args.filename != None:
        logger.read(args.filename)
        print(args.filename)#temporary
    elif args.e_date != None:
        print(args.e_date)#temporary
    elif args.u_date != None:
        print(args.u_date)#temporary


except ValueError as err:
	viewer.print('Some Error',  err)
