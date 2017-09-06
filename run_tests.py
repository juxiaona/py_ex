import unittest
import time
from base.HTMLTestRunner import HTMLTestRunner
from base.sendmail import SendMail

discover=unittest.defaultTestLoader.discover("./test_case",pattern="*.py")

if __name__ == '__main__':

	'''运行测试用例并生成测试报告'''
	now=time.strftime('%Y-%m-%d_%H_%M_')
	filename="./report/"+now+"report.html"
	fp=open(filename,"wb")
	runner=HTMLTestRunner(stream=fp,title="测试报告",description="用例执行情况")
	runner.run(discover)
	fp.close()

	'''发送邮件'''
	mail=SendMail('smtp.163.com', 'ju_xiaona@163.com', 'jxn461028', 'juxiaona@xxkuaipao.com')
	mail.sendmail(filename)

