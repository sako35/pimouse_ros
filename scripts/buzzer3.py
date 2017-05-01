#!/usr/bin/env python
#encoding: utf8     #日本語使うときはこれ

#*** import **************************************
import rospy        #rospy:ROSでpythonを使う
#『std_msgs.msg』というモジュール・パッケージから『UInt16』を使用
#~~~~~~~~~~~~~~ stg_msgの中のmsgパッケージ
from std_msgs.msg import UInt16
#*** END import **********************************

#この関数はhzという変数をつかう
#write_freq()と使ったときhz=0となる
def write_freq(hz=0):
    bfile = "/dev/rtbuzzer0"
    try:
        #f = open("/dev/rtbuzzer0", "w")
        #ファイルを書き込み用に開く
        #withだとこのインデント範囲を出るときに勝手にファイルを閉じてくれる
        with open(bfile, "w") as f:
            #str:
            f.write(str(hz) + "\n")
    #ファイルに書き込めなかったときの例外処理
    except IOError:
        #ログを書き出す
        rospy.logerr("can't write to " + bfile )

def recv_buzzer(data):
    write_freq(data.data)

if __name__ == '__main__':
    rospy.init_node('buzzer')   #ノードを初期化する ノードがROSに登録される
    #ブザーの周波数をを他のノードから受けるための受け口になる
    #(トピック名、トピックの型、購読したときに起動する関数(コールバック関数))
    rospy.Subscriber("buzzer", UInt16, recv_buzzer)
    rospy.spin()        #ノードを待機状態にする

