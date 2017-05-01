#!/usr/bin/env python
#encoding: utf8     #日本語使うときはこれ

#*** import **************************************
import rospy        #rospy:ROSでpythonを使う
#『std_msgs.msg』というモジュール・パッケージから『UInt16』を使用
#~~~~~~~~~~~~~~ stg_msgの中のmsgパッケージ
from std_msgs.msg import UInt16
#*** END import **********************************

def recv_buzzer(data):
    #ログ出力
    rospy.loginfo(type(data))
    #data.dataは受け取った値
    rospy.loginfo(data.data)

if __name__ == '__main__':
    rospy.init_node('buzzer')   #ノードを初期化する ノードがROSに登録される
    #ブザーの周波数をを他のノードから受けるための受け口になる
    #(トピック名、トピックの型、購読したときに起動する関数(コールバック関数))
    rospy.Subscriber("buzzer", UInt16, recv_buzzer)
    rospy.spin()        #ノードを待機状態にする

