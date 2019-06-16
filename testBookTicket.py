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


class TestBookTicket(unittest.TestCase):
    def setUp(self):
        dr.get('http://127.0.0.1:1080/WebTours/index.htm')
        dr.implicitly_wait(10000)
        dr.maximize_window()

    def tearDown(self):
        dr.refresh()
        sleep(1)

    def test_book_ticket(self):
        '''订票测试'''
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

        # 点击 Flights 进入订票页面
        dr.switch_to.frame("body")
        dr.switch_to.frame("navbar")
        dr.find_element_by_xpath("/html/body/center/center/a").click()
        sleep(1)

        # Departure City 选择
        dr.switch_to.frame("body")
        dr.switch_to.frame("info")
        dr.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr/td[2]/select").click()
        sleep(1)

        '''将CSV文件中Departure City数据转换成列表并进行随机读取 '''
        depart_city = open('C:\\PyCharm_project\\webTours\\Version_2\\data_departurecity.csv')  # 打开csv文件
        depart_city_lines = csv.reader(depart_city)  # 逐行读取csv文件
        list_depart = []  # 创建列表准备接收csv各行数据
        for one_line in depart_city_lines:  # 将csv文件转换成列表
            list_depart.append(one_line)  # 将读取的csv分行数据按行存入列表中
            depart_city_xpath = random.choice(list_depart)[0]

        above = dr.find_element_by_xpath("%s" % depart_city_xpath)  # Departure City:
        ActionChains(dr).double_click(above).perform()
        sleep(1)

        # Arrival City 选择
        dr.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[2]/td[2]/select").click()
        sleep(1)

        '''将CSV文件中Arrival City数据转换成列表并进行随机读取 '''
        arrival_city = open('C:\\PyCharm_project\\webTours\\Version_2\\data_arrivalcity.csv')  # 打开csv文件
        arrival_city_lines = csv.reader(arrival_city)  # 逐行读取csv文件
        list_arrival = []  # 创建列表准备接收csv各行数据
        for one_line in arrival_city_lines:  # 将csv文件转换成列表
            list_arrival.append(one_line)  # 将读取的csv分行数据按行存入列表中
            arrival_city_xpath = random.choice(list_arrival)[0]

        above = dr.find_element_by_xpath("%s" % arrival_city_xpath)  # Departure City:
        ActionChains(dr).double_click(above).perform()
        sleep(1)

        # Departure Date:
        dr.find_element_by_name("departDate").clear()
        sleep(1)
        dr.find_element_by_name("departDate").send_keys("05/01/2019")
        sleep(1)

        # Return Date:
        dr.find_element_by_name("returnDate").clear()
        sleep(1)
        dr.find_element_by_name("returnDate").send_keys("05/03/2019")
        sleep(1)

        # No. of Passengers:
        dr.find_element_by_name("numPassengers").clear()
        sleep(1)
        dr.find_element_by_name("numPassengers").send_keys("1")
        sleep(1)

        # Roundtrip ticket:
        # dr.find_element_by_name("roundtrip").click()
        # time.sleep(1)

        # Seating Preference
        dr.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[5]/td/label[2]/input").click()
        sleep(1)

        # Type of Seat
        dr.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[5]/td[3]/label/input").click()
        sleep(1)

        # continue
        dr.find_element_by_name("findFlights").click()
        sleep(2)

        # 航班选择
        dr.find_element_by_xpath("/html/body/blockquote/form/center/table/tbody/tr[4]/td/input").click()
        sleep(2)

        # continue
        dr.find_element_by_name("reserveFlights").click()
        sleep(1)

        # Payment Details
        # First Name
        dr.find_element_by_name("firstName").clear()
        sleep(1)
        dr.find_element_by_name("firstName").send_keys("Swift")
        sleep(1)

        # Last Name
        dr.find_element_by_name("lastName").clear()
        sleep(1)
        dr.find_element_by_name("lastName").send_keys("Taylor")
        sleep(1)

        # Street Address
        dr.find_element_by_name("address1").clear()
        sleep(1)
        dr.find_element_by_name("address1").send_keys("the First Avenue")
        sleep(1)

        # City/State/Zip
        dr.find_element_by_name("address2").clear()
        sleep(1)
        dr.find_element_by_name("address2").send_keys("Venice")
        sleep(1)

        # Passenger Names
        dr.find_element_by_name("pass1").clear()
        sleep(1)
        dr.find_element_by_name("pass1").send_keys("Edward")
        sleep(1)

        # Credit Card
        dr.find_element_by_name("creditCard").clear()
        sleep(1)
        dr.find_element_by_name("creditCard").send_keys("4567890")
        sleep(1)

        # Exp Date
        dr.find_element_by_name("expDate").clear()
        sleep(1)
        dr.find_element_by_name("expDate").send_keys("05/25")
        sleep(1)

        # Save this Credit Card Information （如果没点上再点下）
        dr.find_element_by_name("saveCC").click()
        sleep(1)

        # continue
        dr.find_element_by_name("buyFlights").click()
        sleep(1)

        try:
            title = dr.title
            self.assertEqual(title, "Web Tours")
            sleep(1)
            print('\n订票成功:')
            print('预期值:' + "Web Tours")
            print('实际值:' + title)
            dr.get_screenshot_as_file(path + time + "_订票成功" + ".jpg")
            sleep(1)
        except:
            print('订票失败：')
            print('预期值：' + "Web Tours")
            print('实际值:' + 'error_message')
            dr.get_screenshot_as_file(path + time + "_订票失败" + ".jpg")
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
    report_title = u'参数化订票模块测试报告'  # 定义脚本标题，加u为了防止中文乱码
    desc = u'订票模块测试报告详情：'  # 定义脚本内容，加u为了防止中文乱码
    time = time.strftime("%Y-%m-%d %H_%M_%S")  # 定义date为日期，time为时间
    path = 'C:\\Users\\Administrator\\Desktop\\WebTours\\Version_2.0\\bookticket\\'  # 定义path为文件路径，目录级别，可根据实际情况自定义修改
    report_path = path + time + "_report.html"  # 定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    testunit = unittest.TestSuite()
    testunit.addTest(TestBookTicket("test_book_ticket"))
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(stream=fp, title=report_title, description=desc)
    runner.run(testunit)
    fp.close()
    dr.quit()
