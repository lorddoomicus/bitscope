#
# fft.awk 
# (c) 2016 Derrik Walker v2.0
#
# An awk script to perform an FFT on the data extracted from dso.awk 
#
# run with:
#	awk -f dso.awk -v chan={0,1} < file.csv | awk -f fft.awk > file.fft
#	gnuplot fft.plt
#	
#	file.csv is "recorded" from the Bitscope DSO program, chan=0 for channel A and chan=1 for Channel B.
# 
# This is the scipt goes with the blog post:
#
# http://www.doomd.net/2016/10/the-bitscope-linux-and-python.html 
#
# This is licensed for use under the GNU General Pulbic License v2
#
# 2016-06-27	DW2	Initial Version
# 2016-10-12	DW2	Initial release
#

BEGIN {
	print "Sorry, no fft in awk YET"
}
