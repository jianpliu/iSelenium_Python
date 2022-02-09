# -*- coding: utf-8 -*-
import allure
import configparser
import os
import time
import unittest
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


@allure.feature('Test Baidu WebUI')
class Iselenium(unittest.TestCase):
    #读入配置文件
    # def get_config(self):
    #     config=configparser.ConfigParser()
    #     config.read(os.path.join(os.environ['HOME'],'iselenum.ini'))#linux中
    #     # config.read(os.path.abspath('..') + '\iselenium.ini')#windows中
    #     # os.environ['HOME']  在linux中cd ~   ,在windows中例如c:\users\username
    #
    #     return config

    def tearDown(self):
        self.driver.quit()

    def setUp(self):

        # config=self.get_config()

        # 控制是否采用无界面形式运行自动化测试
        # try:
        #     using_headless=os.environ["using_headless"]
        # except KeyError:
        #     using_headless=None
        #     print('没有配置环境变量 using_headless,按照有界面方式运行自动化测试')

        chrome_options=Options()

        # if using_headless is not None and using_headless.lower()=='true':
        #     print("使用无界面方式运行")
        #     chrome_options.add_argument("--headless")



        # self.driver = webdriver.Chrome(executable_path=config.get('driver','chrome_driver'),
        #                                options=chrome_options)
        self.driver = webdriver.Remote("http://192.168.224.137:5002/wd/hub", options=chrome_options)




    @allure.story('The key word 今日头条')
    def test_webui_1(self):

        """测试用例1,验证'今日头条'关键词在百度上的搜索结果"""

        self._test_baidu('今日头条','test_webui_1')

    @allure.story('The key word 王者荣耀')
    def test_webui_2(self):
        """测试用例1,验证'今日头条'关键词在百度上的搜索结果"""

        self._test_baidu('王者荣耀', 'test_webui_2')

    def _test_baidu(self,search_keyword,testcase_name):
        """测试百度搜索子函数
        :param search_keyword:  搜索关键词（str）
        :param testcase_name:  搜索关键词（str）
        """

        self.driver.get("http://www.baidu.com")
        print('打开浏览器，访问 www.baidu.com')
        time.sleep(5)
        assert f'百度一下' in self.driver.title

        elem=self.driver.find_element_by_name("wd")
        # elem=self.driver.find_element(By.NAME,"wd")
        print(len(elem))
        print(elem)
        elem.send_keys(f'{search_keyword}{Keys.RETURN}')
        print(f'搜索关键词~{search_keyword}')
        time.sleep(5)
        self.assertTrue(f'{search_keyword}' in self.driver.title,msg=f'{testcase_name}校验点 pass')
