#!/usr/bin/env python
#encoding: utf8     #日本語使うときはこれ
import rospy        #rospy:ROSでpythonを使う
rospy.init_node('buzzer')   #ノードを初期化する ノードがROSに登録される
rospy.spin()        #ノードを待機状態にする

