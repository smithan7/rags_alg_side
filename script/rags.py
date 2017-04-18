#!/usr/bin/env python

import rospy
from custom_messages.msg import Edge_Costs, Nav_Goal, Query_RAGS, Scan_Goals

import time
import sys
import math
import numpy as np

class RAGS:

	def __init__( self, map_num ):
		if map_num == 0:
			v = open("vertices0.txt", "r" )
			e = open("edges0.txT", "r" )
