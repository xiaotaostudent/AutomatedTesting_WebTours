# -*- coding: utf-8 -*-
import csv  # 导入scv库，可以读取csv文件
import unittest
import time
import os
from selenium import webdriver
from time import sleep
from HTMLTestRunner import HTMLTestRunner  # 导入HTMLTestRunner库，这句也可以放在脚本开头

dr = webdriver.Firefox()


class TestLoginPara(unittest.TestCase):
    def setUp(self):
        dr.get('http://127.0.0.1:1080/WebTours/index.htm')
        dr.implicitly_wait(10000)
        dr.maximize_window()

    def test_login(self):
        '''登陆测试'''
        # 要读取的csv文件路径
        my_file = 'C:\\PyCharm_project\\webTours\\Version_2\\data_login.csv'
        # csv.reader()读取csv文件，
        # Python3.X用open，Python2.X用file，'r'为读取
        # open(file,'r')中'r'为读取权限，w为写入，还有rb，wd等涉及到编码的读写属性
        data = csv.reader(open(my_file, 'r'))
        # for循环将读取到的csv文件的内容一行行循环，这里定义了user变量(可自定义)
        # user[0]表示csv文件的第一列，user[1]表示第二列，user[N]表示第N列
        # for循环有个缺点，就是一旦遇到错误，循环就停止，所以用try，except保证循环执行完
        for user in data:
            dr.switch_to.frame("body")
            dr.switch_to.frame("navbar")
            dr.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]/input").clear()
            dr.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]/input").send_keys(user[0])
            sleep(1)
            dr.find_element_by_xpath("/html/body/form/table/tbody/tr[6]/td[2]/input").clear()
            dr.find_element_by_xpath("/html/body/form/table/tbody/tr[6]/td[2]/input").send_keys(user[1])
            sleep(1)
            dr.find_element_by_xpath("/html/body/form/table/tbody/tr[8]/td[2]/input").click()
            sleep(1)
            dr.get_screenshot_as_file(path + user[3] + ".jpg")
            sleep(1)

            print('\n' + '测试项：' + user[2])

            try:
                title = dr.title
                self.assertEqual(title, user[4])
                print('提示信息正确！预期值与实际值一致:')
                print('预期值：' + user[4])
                print('实际值:' + title)
            except:
                print('提示信息错误！预期值与实际值不符：')
                print('预期值：' + user[4])
                print('实际值:' + 'error_message')
                # except:
                #     print('提示信息类型错误,请确认元素名称是否正确！')

    def tearDown(self):
        dr.refresh()


if __name__ == '__main__':
    report_title = u'参数化登陆模块测试报告'  # 定义脚本标题，加u为了防止中文乱码
    desc = u'登陆模块测试报告详情：'  # 定义脚本内容，加u为了防止中文乱码
    time = time.strftime("%Y-%m-%d %H_%M_%S")  # 定义date为日期，time为时间
    path = 'C:\\Users\\Administrator\\Desktop\\WebTours\\Version_2.0\\login\\'  # 定义path为文件路径，目录级别，可根据实际情况自定义修改
    report_path = path + time + "_report.html"  # 定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html

    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    testsuite = unittest.TestSuite()  # 定义一个测试容器
    testsuite.addTest(TestLoginPara("test_login"))  # 将测试用例添加到容器

    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)

    report.close()  # 关闭report，脚本结束
    dr.quit()  # 关闭浏览器
