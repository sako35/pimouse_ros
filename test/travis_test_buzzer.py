#!/usr/bin/env python
#encoding: utf8
#***import*******************************************
#rospy:ROSをpythonで書くよー unittest:pythonのテストフレームワーク
#rostest:ROS用のテストフレームワーク
import rospy, unittest, rostest
import rosnode
import time
from std_msgs.msg import UInt16
#***End import***************************************

#新たなクラスを作成する
#unittest.TestCaseの属性をBuzzerTestでも使えるようにしている
#                   ~~~~ 属性：メソッドや変数のこと
class BuzzerTest(unittest.TestCase):
    #test_node_exist関数を作成
    #self:自分自身
    def test_node_exist(self):
        #今立ち上がっているノードのリストを取得する
        nodes = rosnode.get_node_names()
        #ノードリストの中にブザーノードがあるか確かめる
        #(リストに含まれるべき値、リスト、値がないときに出力する文字列)
        self.assertIn('/buzzer', nodes, "node does not exist")
        
    def test_put_value(self):
        #パブリッシャの作成(トピック、型)
        pub = rospy.Publisher('/buzzer', UInt16)
        for i in range(10):
            #トピックに何を送るか
            pub.publish(1234)
            time.sleep(0.1)

        with open("/dev/rtbuzzer0","r") as f:
            data = f.readline()
            #1234って入ってるか確認
            self.assertEqual(data, "1234\n", "value does not written to rtbuzzer0"

#このプログラムをこのファイルから実行したときのみ行う
if __name__ == '__main__':
    #テスト対象のノードが立ち上がるのを待つ。3秒
    time.sleep(3)
    #ノードを立ち上げる
    rospy.init_node('travis_test_buzzer')
    #テストを走らせる
    #(パッケージ名、テスト名、テストを記述したクラス名)
    rostest.rosrun('pimouse_ros', 'travis_test_buzzer', BuzzerTest)
