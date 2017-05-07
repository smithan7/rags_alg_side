#!/usr/bin/env python

import rospy
from custom_messages.msg import Edge_Costs, Nav_Goal, Query_RAGS, Scan_Goals

import time
import sys
import math
import numpy as np
import random

class ASTAR:

	lats = []
	lons = []

	edges_to_scan_publisher = rospy.Publisher("/edges_to_scan", Scan_Goals, queue_size=10)
	nav_goal_publisher = rospy.Publisher("/waypoint_to_travel", Nav_Goal, queue_size=10)

	def __init__( self, map_name ):
		print "Running A* on " , map_name
		rospy.Subscriber("/edge_cost", Edge_Costs, self.edge_costs_callback)
		rospy.Subscriber("/waiting_on_RAGS", Query_RAGS, self.waiting_on_RAGS_callback)		

		print "loading path for map ", map_name
		f = open("/home/nvidia/catkin_ws/src/rags_alg_side/graphs/" + map_name, "r")
		lines = f.readlines()
		print lines
		for line in lines:
			print line
			[lon, lat] = line.split(",")
			self.lats.append( float( lat ) )
			self.lons.append( float( lon ) )
		print "loaded A* path"

	def edge_costs_callback( self, edge_costs ):
		print "recieved edge costs: " , edge_costs
		# get current vertice and iterate to next in path
		
	def waiting_on_RAGS_callback( self, query ):
			
			if query.request_type == 0:
				print "recieved RAGS scan goals request while in A Star"
				# requesting edges to scan, send empty list
				sg = Scan_Goals()
				print "sending no scan vertices"
				self.edges_to_scan_publisher.publish( sg )
				return
			
			if query.request_type == 1:
				print "recieved RAGS nav goal request"
				# requesting a nav goal
				# get current vertice and iterate to next in path
				c_index = query.my_vertex_index + 1
				print "sending new travel vertice # " , c_index, " of " , len( self.lats )
				if c_index < len( self.lats ):
					ng = Nav_Goal()
					ng.goal_lat = self.lats[c_index]
					ng.goal_lon = self.lons[c_index]
					ng.goal_index = c_index
					# publish nav_goal
					self.nav_goal_publisher.publish( ng )
				return				
		

