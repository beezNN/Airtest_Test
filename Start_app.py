
__author__ = "Administrator"
from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# 通过ADB连接本地Android设备
# vivo x21
connect_device("Android:b3c4dc01")
# 三星s9+
# connect_device("Android:31555034434b3098")
start_app("com.ddread")

