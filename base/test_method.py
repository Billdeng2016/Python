# coding:utf-8
import json
import unittest
from base.demo import RunMain
import HTMLTestRunner
import mock
from base.mock_demo import mock_test


class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('类执行之前的方法')

    @classmethod
    def tearDownClass(cls):
        print('类执行之后的方法')

    def setUp(self):
        self.run = RunMain()

    def tearDown(self):
        pass

    def test_01(self):
        data = {
            'managerName': 'admin',
            'managerPwd': 'lian1202',
            'captchaId': '23551219',
            'captcha': 'xqvz'
        }
        url = 'https://www.imooc.com/index/getstarlist'
        #mock_data = mock.Mock(return_value=data)
        #self.run.run_main = mock_data
        res = mock_test(self.run.run_main, data, url, 'GET', data)
        #res = self.run.run_main(url,'GET', data)
        self.assertEqual(res["managerName"], "admin", "pass")

    @unittest.skip('test_02')
    def test_02(self):
        # mock.Mock()
        print('test2')


if __name__ == '__main__':
    filepath = "d:/WebProject/report.html"
    fp = open(filepath,'wb')

    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is report')
    runner.run(suite)
    fp.close()
