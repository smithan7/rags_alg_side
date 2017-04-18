#!/usr/bin/env python

import rospy
from aStar import ASTAR
from rags import RAGS

if __name__ == '__main__':
	rospy.init_node('rags_alg_side', anonymous=True)
	
	use_rags = rospy.get_param( '~use_rags' )
	map_num = rospy.get_param( '~map_num' )

	if use_rags:
		rags = RAGS( map_num )
	else:
		astar = ASTAR( map_num )

	rospy.spin()
