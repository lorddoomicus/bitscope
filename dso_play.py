#!env python
#
# dso_play.py: 
# (c) 2016 Derrik Walker v2.0
#
# Play audio from data 'recorded' from the Bitscope DSO program using dso_data class from bitscope.py. 
# This requires the numpy and pygame packages for python3 to be installed
#
# usage:
#
#	dso_play.py [-c <channel>] -f <file>.csv
#	
#	Where <file.csv> is a "recorded" output from the Bitscope DSO program
#
# This is the scipt goes with the blog post:
#
# http://www.doomd.net/2016/10/the-bitscope-linux-and-python.html 
#
# This is licensed for use under the GNU General Pulbic License v2
#
# 2016-10-11	DW2	Initial Version
# 2016-10-12	DW2	Initial release and cleaned up code a bit
#

import getopt, sys, time
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

rate = dso.rate( channel )
sig = dso.sig( channel )

if rate == None:
	print( "It appears that channel", channel, "has no data!" )
	sys.exit()

# the data has to be signed 16-bit ints:
temp = []
for sample in sig:
	temp.append( np.int16( sample * float(0x7fff) ))

samples = np.array( temp, np.int16 )

# set up the mixer and sndarray and play the sound

pg.mixer.init( int( rate ), size=-16, channels=1, buffer=4096)
sound = pg.sndarray.make_sound( samples )

sound.play()

time.sleep( len(samples) / rate )	# gotta give it time to play!!
