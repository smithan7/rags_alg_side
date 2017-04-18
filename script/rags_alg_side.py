#!/usr/bin/env python

import rospy
from aStar import ASTAR
from rags import RAGS

if __name__ == '__main__':
	rospy.init_node('rags_alg_side', anonymous=True)
	
	use_rags = rospy.get_param( '~use_rags' )
	map_name = rospy.get_param( '~map_name' )

	if use_rags:
		rags = RAGS( map_name )
	else:
		astar = ASTAR( map_name )

	rospy.spin()
