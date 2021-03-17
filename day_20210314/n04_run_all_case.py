import unittest
from day_20210314.n03_request_0314 import test_request
import os
#方式1
# suite=unittest.TestSuite()
# suite.addTest(test_request('test01'))
# unittest.main(verbosity=1,defaultTest='suite')
#方式2 discover遍历目录加载用例
case_path=os.path.dirname(__file__)
print(case_path)
discover=unittest.defaultTestLoader.discover(start_dir=case_path,
                                             pattern='n03*.py',
                                             )
suite=unittest.TestSuite()
suite.addTest(discover)
unittest.main(verbosity=2,defaultTest='suite')