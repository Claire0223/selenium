#-*-coding=utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By #支持定位器的各个分类
import time

class Page(object):
    "定义基类"

    login_url='https://www.douban.com/' #基本的url

    #定义基类
    def __init__(self,selenium_dirver,base_url=login_url):
        self.base_url=base_url
        self.driver=selenium_dirver
        self.timeout=30

    #校验页面加载是否正确
    def on_page(self):
        return self.driver.current_url==(self.base_url+self.url)

    def _open(self,url):
        url=self.base_url + url
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(3)
        assert self.on_page(),'did not land on %s'% url

    def open(self):
        self._open(self.url)

    #元素定位
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    
  



