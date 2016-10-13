#
# dso.awk 
# (c) 2014 Derrik Walker v2.0
#
# An GNU awk script to extract the channel data from a csv file created by the Bitscope-dso program
#
# The data file is oringized as a CSV with A few fields then starting on the 10th, data until NF for the record. We also need 
# the channel which is specified on the command line, and the rate, which is field 8, from any of the channel matching records.
#
# run with:
#	gawk -f dso.awk -v chan={0,1} < file.csv | graph -T tek
#	
#	file.csv is "recorded" from the Bitscope DSO program, chan=0 for channel A and chan=1 for Channel B.
#	graph is part of plotutils, but the output could be saved to a file, or sent to another program.
#
# Output is ascii text for each data point extracted:
#
#	time_in_sec voltage
#
# Then some useful information is printed to STDERR so it's not in the output stream of the actual data you want to graph 
# or analyze
# 
# This is the scipt goes with the blog post:
#
# http://www.doomd.net/2016/10/the-bitscope-linux-and-python.html 
#
# This is licensed for use under the GNU General Pulbic License v2
#
# 2014-10-04	DW2	Initial Version
# 2016-06-28	DW2	Fixed the output
# 2016-10-12	DW2	Initial release
#

BEGIN {
	FS = ","
	count = 0
	# chan = 0

	if (  ! ( chan == 0 || chan == 1 ) ) {
	 	print "chan MUST be 0 or 1, not", chan > "/dev/stderr"
		err=1
	 	exit 1
	}
}

{
	dp=10
	rate=$8

	if( $3 == chan ) 
		for( i=dp; i <= NF; i++ ) {
			print count/rate, $i 
			count ++
		}

}

END {
	if ( err != 1 ) {
		print "chan =", chan > "/dev/stderr"
		print "rate =", rate > "/dev/stderr"
		print "samples =", count > "/dev/stderr"
		print "time =", count/rate, "seconds" > "/dev/stderr"
	}
}
