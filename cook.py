#! /usr/bin/env python

#
#  cook.py
#
#  Main file for the utility
#

print '*************************\n* Welcome to ofoamCook! *\n*************************\n'

import bounds.fileParser

print bounds.fileParser.parseBound('constant/polyMesh/boundary')

print 'Tomas je kral '
