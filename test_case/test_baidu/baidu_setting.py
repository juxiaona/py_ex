import sys
sys.path.append('../../')
from base.base import Base
from base.HTMLTestRunner import HTMLTestRunner
import unittest
import time

class BaiduSet(unittest.TestCase):

	def setUp(self):

		self.base=Base("chrome")
		self.base.open("http://www.baidu.com")
		self.base.max_window()

	def test_setting(self):
		'''设置功能'''
		self.base.move_to_element("link_text=>设置")
		self.base.click_element("link_text=>搜索设置")
		self.base.select_element('id=>nr', '50')
		self.base.click_element('class=>prefpanelgo')

	def tearDown(self):
		self.base.quit()

if __name__ == '__main__':

	unittest.main()

	'''
	suite=unittest.TestSuite()
	suite.addTest(BaiduSet('test_setting'))

	now=time.strftime("%Y-%m-%d-%H_%M_")

	filename="../../report/"+now+"report.html"
	fp=open(filename,"wb")
	runner=HTMLTestRunner(stream=fp,title="测试报告",description="用例执行情况")
	runner.run(suite)
	fp.close()
	'''
