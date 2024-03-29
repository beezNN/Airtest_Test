__author__ = "Administrator"
import unittest
from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# 通过ADB连接本地Android设备
# vivo x21
# connect_device("Android:b3c4dc01")
# 三星s9+
connect_device("Android:31555034434b3098")
start_app("com.ddread")


class Turn_page(unittest.TestCase):

    @staticmethod
    def test_turn():
        try:
            for i in range(10000):
                if (i < 9999):
                    touch([950, 1100])
                    sleep(0.5)
                else:
                    touch([580, 1086])
                    poco("com.ddread:id/id_img_toolbar_back").click()
                    exists(poco("com.ddread:id/id_tv_positive").click())
        except Exception as e:
            pass


if __name__ == '__main__':
    unittest.main()
