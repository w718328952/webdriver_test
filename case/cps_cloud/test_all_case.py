
import sys
# sys.path.append('..\case')
from case.cps_cloud.case1_cps_cloud_repeat_login import *
from case.cps_cloud.case2_cps_cloud_default_config import *
from case.cps_cloud.case3_cps_cloud_compare_profiles import *
from case.cps_cloud.case4_ps_cloud_config_version import *
from case.cps_cloud.case5_cps_cloud_repeat_download import *

import unittest
import case.cps_cloud.HTMLTestRunner

suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(case1_cps_cloud_repeat_login))
# suite.addTest(unittest.makeSuite(case2_cps_cloud_default_config))
# suite.addTest(unittest.makeSuite(case3_cps_cloud_compare_profiles))
# suite.addTest(unittest.makeSuite(case4_ps_cloud_config_version))
# suite.addTest(unittest.makeSuite(case5_cps_cloud_repeat_download))
