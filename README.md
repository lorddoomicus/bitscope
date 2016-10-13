# The Bitscope, Linux and the Python

These scripts and support files provide examples of how to use python in a UNIXish way to parse and process
data files "recorded" from the Bitscope DSO program.

More information can be found at this blog post:

http://www.doomd.net/2016/10/the-bitscope-linux-and-python.html

__NOTE__: the AWK scripts must be run with gawk.  The Python scrips all require numpy, some may also require pygame and/or matplotlib.

## What's Here


- dso.awk
	- pretty much a proof of concept just to work out parsing the CSV files from the DSO program.

- fft.awk
	- An fft in awk? Not yet, but maybe someday!

- bitscope.py
	- Python library that parses the "saved" output file from the DSO program and creates a numpy array and other data
	  This, and all programs that use it,  requires to have numpy installed.

- dso_test.py
	- Python program to test the bitscope library.  It just prints out the parsed output, and some information about it.

- dso_fft.py
	- Python Program that displays the original waveform and it's spectrgraph created using an FFT of the waveform.
	  Uses the above bitscope.py library.

- dso_play.py
	- Python Program that converts the data from the DSO saved output file and plays it as a sound.  This required
	  to have pygame installed in addition to numpy.

- square.csv
	- A 5 Hz square wave of a blinking LED sampled at 440 samples a second that was created using blink.ano and an Arduino UNO.
	  This was generated with the demo progam for blinking and CA of the Bitscope was connected to pin 13 of the Arduino.

- tone.csv
	- A 1000 Hz sine wave created using the 'tone' feature of the waveform generator on in the DSO program.

## License

All files are covered under the GNU General Public License v2.

(c) 2016 Derrik Walker v2.0, dwalker@doomd.net
