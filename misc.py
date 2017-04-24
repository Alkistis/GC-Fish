""" 
	This is a library for calculations Fisher matrices for GC.

	These is for miscellaneous functions that have nothing to do with cosmology.

	Markovic & Pourtsidou, 2016
"""

import time, datetime

# Generate a string timestamp
def get_timestamp():
	# Calculate the number of seconds since the Brexit referrendum polls closed
	t_Brexit = '23/06/2016 21:00' # GMT/UTC, 22:00 BST
	t_Brexit = time.mktime(datetime.datetime.strptime(t_Brexit, "%d/%m/%Y %H:%M").timetuple())
	return '-'+str(int(time.time() - t_Brexit))
