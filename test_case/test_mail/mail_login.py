import unittest
import sys
sys.path.append("../../")
from base.base import Base


class MailLogin(unittest.TestCase):

	def setUp(self):

		self.base=Base("chrome")
		self.base.open("http://mail.163.com")
		self.base.max_window()

	def test_login(self):
		'''邮箱登录'''

		self.base.switch_frame("id=>x-URS-iframe")
		self.base.sendkeys("name=>email", "ju_xiaona")
		self.base.sendkeys("name=>password","jxn0124")
		self.base.click_element("id=>dologin")


	def tearDown(self):

		self.base.quit()

if __name__ == '__main__':

	unittest.main()

	'''
	suite=unittest.TestSuite()
	suite.addTest(MailLogin('test_login'))

	now=time.strftime('%Y-%m-%d_%H_%M_')
	filename="../../report/"+now+"report.html"
	fp=open(filename,"wb")
	runner=HTMLTestRunner(stream=fp,title="测试报告",description="用例执行情况")
	runner.run(suite)
	fp.close
	'''