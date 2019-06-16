# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re
import os
import time
from time import sleep
from HTMLTestRunner import HTMLTestRunner


class TestSignIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(100)
        self.base_url = "http://127.0.0.1:1080/WebTours/index.htm"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()

    def tearDown(self):
        # sleep(1)
        self.driver.quit()

    def test_signin(self):
        driver = self.driver
        # driver.get(self.base_url)
        driver.switch_to.frame("body")
        driver.switch_to.frame("info")
        # 点击进入注册页面
        driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/blockquote/a/b").click()
        # 输入注册信息
        # driver.switch_to.frame("body")
        # driver.switch_to.frame("info")
        sleep(1)
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr/td[2]/input").clear()
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr/td[2]/input").send_keys("test88")
        sleep(1)
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[2]/td[2]/input").clear()
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[2]/td[2]/input").send_keys("123456")
        sleep(1)
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[3]/td[2]/input").clear()
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[3]/td[2]/input").send_keys("123456")
        sleep(1)
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[5]/td[2]/input").clear()
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[5]/td[2]/input").send_keys("Michael")
        sleep(1)
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[6]/td[2]/input").clear()
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[6]/td[2]/input").send_keys("Smith")
        sleep(1)
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[7]/td[2]/input").clear()
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[7]/td[2]/input").send_keys(
            "The first avenue")
        sleep(1)
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[8]/td[2]/input").clear()
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[8]/td[2]/input").send_keys("Washington")
        sleep(1)

        # 点击注册
        driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[10]/td/input").click()
        sleep(1)

        try:
            # 添加检查点，验证是否注册成功
            # driver.switch_to.frame("body")
            # driver.switch_to.frame("info")
            text_value = driver.find_element_by_xpath("/html/body/blockquote/b").text
            sleep(1)
            self.assertEqual("test88", text_value)
            sleep(1)
            print('\n注册成功:')
            print('预期值:' + "test88")
            print('实际值:' + text_value)
            driver.get_screenshot_as_file(path + time + "_注册成功" + ".jpg")
            sleep(1)
        except:
            print("\n注册失败")
            driver.get_screenshot_as_file(path + time + "_注册失败" + ".jpg")
            sleep(1)

        # 刷新页面
        driver.refresh()
        sleep(1)
        # 关闭浏览器
        driver.quit()


if __name__ == "__main__":
    report_title = u'WebTours注册功能'  # 定义脚本标题，加u为了防止中文乱码
    desc = u'注册功能测试报告详情：'  # 定义脚本内容，加u为了防止中文乱码
    time = time.strftime("%Y-%m-%d %H_%M_%S")  # 定义date为日期，time为时间
    path = 'C:\\Users\\Administrator\\Desktop\\WebTours\\Version_2.0\\signin\\'  # 定义path为文件路径，目录级别，可根据实际情况自定义修改
    report_path = path + time + "_report.html"  # 定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    testunit = unittest.TestSuite()
    testunit.addTest(TestSignIn("test_signin"))
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(stream=fp, title=report_title, description=desc)
    runner.run(testunit)
    fp.close()
