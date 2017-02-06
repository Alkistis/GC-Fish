""" 
	This is a library of functions used to calculate Fisher matrices for Euclid GC.

	These are the miscellaneous functions that have nothing to do with cosmology.
"""

import time, datetime

# Generate a string timestamp
def get_timestamp():
	# Calculate the number of seconds since the Brexit referrendum polls closed
	t_Brexit = '23/06/2016 21:00' # GMT/UTC, 22:00 BST
	t_Brexit = time.mktime(datetime.datetime.strptime(t_Brexit, "%d/%m/%Y %H:%M").timetuple())
	return '-'+str(int(time.time() - t_Brexit))

if __name__=='__main__':
	print get_timestamp()