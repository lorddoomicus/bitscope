#!env python
#
# dso_test.py: 
# (c) 2016 Derrik Walker v2.0
#
# Prints data from 'recorded' from the Bitscope DSO program to test dso_data class from bitscope.py. 
#
# usage:
#
#	dso_test.py [-c <channel>] -f <file>.csv
#	
#	Where <file.csv> is a "recorded" output from the Bitscope DSO program
#
# This is the scipt goes with the blog post:
#
# http://www.doomd.net/2016/10/the-bitscope-linux-and-python.html 
#
# This is licensed for use under the GNU General Pulbic License v2
#
# 2016-08-11	DW2	Initial Version
# 2016-10-12	DW2	Initial release
#

import getopt, sys
import numpy as np
import pygame as pg

from bitscope import dso_data as bs

def usage():
	print( "Usage: dso_play [-c <channel> ] -f <file.csv>, where <file.csv> is the recorded output from the Bitscope's DSO" )
	sys.exit(1)

file = None
channel = 0 

try:
	opts, args = getopt.getopt( sys.argv[1:], "hc:f:", ["help", "channel=", "file=" ] )

except getopt.GetoptError as err:
	print(err) 
	usage()

for o, a in opts:

	if  o in ( "-c", "--channel" ):
		channel = int( a ) 

	elif o in ("-h", "--help"):
		usage()

	elif o in ("-f", "--file"):
		file =  a
	else:
		assert False, "ERRRR"	

if not file:
	usage()

if channel > 1 or channel < 0:
	print( "channel out of range!" )
	usage()

dso = bs( file )

data = dso.data( channel )
rate = dso.rate( channel )
# sig = dso.sig( channel )

if rate == None:
	print( "It appears that channel", channel, "has no data!" )
	sys.exit()

for i in data:
	print( i )

print( "rate =", rate )
print( "count =", len(data) )

## time = [ x/rate for x in range( 0, len(data) ) ]
