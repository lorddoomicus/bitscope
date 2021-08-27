#!/usr/bin/python3
#
# dso_fft.py: 
# (c) 2016 Derrik Walker v2.0
#
# Generate an fft plot data 'recorded' from the Bitscope DSO program and the dso_data class from bitscope.py. 
#
# usage:
#
#	dso_fft.py [-c <channel>] -f <file>.csv
#	
#	Where <file.csv> is a "recorded" output from the Bitscope DSO program
#
# This is the scipt goes with the blog post:
#
# http://www.doomd.net/2016/10/the-bitscope-linux-and-python.html 
#
# This is licensed for use under the GNU General Pulbic License v2
#
# 2016-06-15	DW2	Initial Version
# 2016-07-04	DW2	Added cmd line support for specifying the channel
# 2016-08-10	DW2	Moved bitscope spacific funtions to bitscope.py
# 2016-10-12	DW2	Initial release
#

import getopt, sys
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt

import bitscope

def usage():
	print( "Usage: dso_fft [-c <channel> ] -f <file.csv>, where <file.csv> is the recorded output from the Bitscope's DSO" )
	exit(1)

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

dso = bitscope.dso_data( file )

data = dso.data( channel )	# raw data as Python array
rate = dso.rate( channel )	# just the rate
sig = dso.sig( channel )	# a numpy array of the data

if rate == None:
	print( "It appears that channel", channel, "has no data!" )
	exit()

time = [ x/rate for x in range( 0, len(data) ) ]

fft = abs( rfft( sig ) ) / (  len(sig)/2 ) 
freq = abs( rfftfreq( sig.size, d=1/rate ) )

plt.subplot( 211 )
plt.xlabel( "Time (sec)" )
plt.ylabel( "Voltage" )
plt.title( "Original Signal" )
if channel == 0:
	plt.plot( time, dso.data0 )
else:
	plt.plot( time, dso.data1 )

plt.subplot( 212 )
plt.xlabel( "Frequency (Hz) " )
plt.ylabel( "Magnitude" )
plt.title( "FFT of Signal" )
plt.plot( freq, fft ) 
 
plt.tight_layout()
plt.show()
