import unittest
import os
from API_Test_Fromwork.common import HTMLTestReportCN
current_path = os.path.dirname(__file__)
case_path = os.path.join(current_path,'test_case')
html_report_path = os.path.join(current_path,'html_reports/')
print(case_path)

discover_cases=unittest.defaultTestLoader.discover(start_dir=case_path,
                                                   pattern='test*.py')

api_case_suite=unittest.TestSuite()
api_case_suite.addTest(discover_cases)
# unittest.main(verbosity=2,defaultTest='api_case_suite')
#创建测试报告路劲对象
html_report_path_obj = HTMLTestReportCN.ReportDirectory(html_report_path)
html_report_path_obj.create_dir('WX_API_TEST_') # 创建测试报告路径
#获取测试报告网页路径
html_report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
html_report_file_obj=open(html_report_file_path,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=html_report_file_obj,
                                         tester='阿信',
                                         title='微信公众平台接口测试项目',
                                         description='实战')
runner.run(api_case_suite)