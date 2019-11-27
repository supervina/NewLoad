#coding=utf-8
from  common.HTMLTestRunner import HTMLTestRunner
import unittest,os,time
from common.read_case import *
from common.config import BASE_PATH

class UI_runner(unittest.TestCase):
    def setUp(self):
        print("测试开始")
    
    # def test_tmall(self):
    #     do_case('tmall')
    #
    # def test_163mail(self):
    #     do_case('163mail')
    #
    # def test_login(self):
    #     do_case('login')
    
    def test_agileone(self):
        do_case('woniusales')

    def test_ituring(self):
        do_case("ituring")
        
    def tearDown(self):
        print("测试结束")


if __name__ == '__main__':
    # 定义脚本标题，加u是支持utf8
    report_title = u'Agileone登录模块测试报告：'

    # 定义详情内容
    desc = u'Agileone登录模块测试报告详情：'

    # 定义一个日期时间戳
    date = time.strftime('%Y%m%d')
    time = time.strftime('%Y%m%d%H%M%S')

    current_path = BASE_PATH
    print(current_path)
    path = current_path + '/report/' + date + '/login/' + time + '/'
    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    report_path = path + 'report.html'

    # 定义一个测试容器
    suite = unittest.TestSuite()  # 初始化一个测试套
    loader = unittest.TestLoader()  # 初始化用例加载
    suite.addTests(loader.loadTestsFromTestCase(UI_runner))

    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)
    # 关闭report，脚本结束
    report.close()






