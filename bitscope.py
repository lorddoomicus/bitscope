#!/usr/bin/python3
#
# bitscope.py: 
# (c) 2016 Derrik Walker v2.0
#
# Python Library for bitscope functions
#
# This is the Library goes with the blog post:
#
# http://www.doomd.net/2016/10/the-bitscope-linux-and-python.html 
#
# This is licensed for use under the GNU General Pulbic License v2
#
# 2016-08-10	DW2	Initial Version
# 2016-09-08	DW2	Fixed a bug in the file parsing
# 2016-10-12	DW2	Initial release
#

import sys, csv
import numpy as np

class dso_data:

	channel0 = 0
	channel1 = 1

	sig0 = []
	sig1 = []

	rate0 = None
	rate1 = None

	count0 = None
	count1 = None

	data0 = []
	data1 = []

	def __init__( self, fname ):

		try:
    			f = open(fname, 'r')

		except IOError:
    			print ( "Error reading file:", fname )
    			sys.exit()

		with f:
			reader = csv.reader( f )
			next ( reader )	# skip the header

			for row in reader:
				if int( row[2] ) == dso_data.channel0:
					self.rate0 = int ( row[7] )
					self.count0 = int( row[8] )
					self.data0.extend( [ float( x ) for x in row[9:len(row)] ])
					
				if int( row[2] ) == self.channel1:
					self.rate1 = int ( row[7] )
					self.count1 = int( row[8] )
					self.data1.extend( [ float( x ) for x in row[9:len(row)] ])

		self.sig0 = np.array( self.data0 )
		self.sig1 = np.array( self.data1 )

	def data( self, channel ):
		# returns the raw data
		
		if( channel == 0 ):
			return self.data0

		elif ( channel == 1 ):
			return self.data0

		else:
			return None

	def sig( self, channel ):
		# returns the numpy array of data
		
		if( channel == 0 ):
			return self.sig0

		elif ( channel == 1 ):
			return self.sig1

		else:
			return None

	def rate( self, channel ):
		# returns the sampling rate

		if( channel == 0 ):
			return self.rate0

		elif( channel == 1 ):
			return self.rate1

		else:
			return None
