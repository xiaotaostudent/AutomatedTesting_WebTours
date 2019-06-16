from selenium import webdriver
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver import ActionChains
import random
import unittest
import os
import time
import csv

dr = webdriver.Firefox()


class TestBookingQuery(unittest.TestCase):
    def setUp(self):
        dr.get('http://127.0.0.1:1080/WebTours/index.htm')
        # dr.implicitly_wait(10000)
        dr.maximize_window()

    def tearDown(self):
        # sleep(1)
        dr.refresh()

    def test_booking_query(self):
        '''订票查询测试'''
        dr.switch_to.frame("body")
        dr.switch_to.frame("navbar")

        # 输入 Username
        dr.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]/input").clear()
        dr.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]/input").send_keys('test001')
        sleep(1)

        # 输入 Password
        dr.find_element_by_xpath("/html/body/form/table/tbody/tr[6]/td[2]/input").clear()
        dr.find_element_by_xpath("/html/body/form/table/tbody/tr[6]/td[2]/input").send_keys('123456')
        sleep(1)

        # 点击 Login 登录
        dr.find_element_by_xpath("/html/body/form/table/tbody/tr[8]/td[2]/input").click()
        sleep(1)

        # 点击 Itinerary 进入航班查询页面
        dr.switch_to.frame("body")
        dr.switch_to.frame("navbar")
        dr.find_element_by_xpath("/html/body/center/center/a[2]").click()
        sleep(1)

        # 机票数量统计
        dr.switch_to.frame("body")
        dr.switch_to.frame("info")
        # text = dr.find_element_by_xpath(
        #     "/html/body/blockquote/form/center/table/tbody/tr[5+(num-1)*3]/td/b").text  # tr[5+(n-1)*3]
        try:
            # 通过 css_selector 属性定位 由于css样式相同 故无法定位准确
            # text = dr.find_element_by_css_selector("html body blockquote form center table tbody tr td b").text
            # 当标签属性很少，不足以唯一区别元素时，但是标签中间中间存在唯一的文本值，也可以定位，其具体格式
            content_before = dr.find_element_by_xpath("//b[contains(text(),'A total of ')]").text
            total_before = int(str(content_before)[11])
            sleep(1)
            # print(total_before)
        except:
            print("error")

        # 取消最新订机票
        dr.find_element_by_name("%d" % total_before).click()
        sleep(1)
        dr.find_element_by_name("removeFlights").click()
        sleep(1)

        # 断言取消订票是否成功
        try:
            if total_before > 1:
                content_after = dr.find_element_by_xpath("//b[contains(text(),'A total of ')]").text
                total_after = int(str(content_after)[11])
                self.assertEqual(total_after, total_before - 1)
                # sleep(1)
                print('\n取消航班成功！')
                print('预期值：%d' % total_after)
                print('实际值: %d' % (total_before - 1))
                dr.get_screenshot_as_file(path + time + "_取消订票成功" + ".jpg")
                sleep(1)
            else:
                content_no = dr.find_element_by_xpath("/html/body/blockquote/form/center/h3").text
                self.assertEqual('No flights have been reserved.', content_no)
                print('\n取消航班成功！')
                print('待起飞航班数为：0')
                dr.get_screenshot_as_file(path + time + "_取消订票成功" + ".jpg")
                sleep(1)

        except:
            print('\n取消航班失败！')
            print('预期值：%d' % total_after)
            print('实际值: %d' % total_before - 1)
            dr.get_screenshot_as_file(path + time + "_取消订票失败" + ".jpg")
            sleep(1)

        # 点击 Home 回到主页
        dr.switch_to.parent_frame()
        dr.switch_to.frame("navbar")
        dr.find_element_by_xpath("/html/body/center/center/a[3]").click()
        sleep(1)

        # 点击 Sign Off 退出
        dr.switch_to.frame("body")
        dr.switch_to.frame("navbar")
        dr.find_element_by_xpath("/html/body/center/center/a[4]").click()
        sleep(1)


if __name__ == "__main__":

    report_title = u'订票查询测试报告'  # 定义脚本标题，加u为了防止中文乱码
    desc = u'订票查询测试报告详情：'  # 定义脚本内容，加u为了防止中文乱码
    time = time.strftime("%Y-%m-%d %H_%M_%S")  # 定义date为日期，time为时间
    path = 'C:\\Users\\Administrator\\Desktop\\WebTours\\Version_2.0\\bookingquery\\'  # 定义path为文件路径，目录级别，可根据实际情况自定义修改
    report_path = path + time + "_report.html"  # 定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    testunit = unittest.TestSuite()
    testunit.addTest(TestBookingQuery("test_booking_query"))
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(stream=fp, title=report_title, description=desc)
    runner.run(testunit)
    fp.close()
    dr.quit()
