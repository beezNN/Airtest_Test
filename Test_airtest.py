import cv2
from comtypes.safearray import numpy as np

__author__ = "Administrator"
import unittest
from Start_app import *

auto_setup(__file__)


class Turn_page(unittest.TestCase):
    @staticmethod
    def test_turn():
        try:
            for i in range(10000):
                if i < 9999:
                    touch([950, 1100])
                    sleep(0.5)
                else:
                    touch([580, 1086])
                    poco("com.ddread:id/id_img_toolbar_back").click()
                    exists(poco("com.ddread:id/id_tv_positive").click())
        except Exception as e:
            pass

    # def string_2_img(self):
    #     nparr = np.fromstring(self, np.uint8)
    #     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #     return img


if __name__ == '__main__':
    unittest.main()
