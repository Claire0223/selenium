#coding:utf-8
import BaseModel
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

#登录模块
class LoginDouban(BaseModel.Page):

    url='/'

    #定位器
    login_type=(By.XPATH,'/html/body/div[1]/div[1]/ul[1]/li[2]')
    username_loc=(By.XPATH,'//*[@id="username"]')
    passwd_loc=(By.XPATH,'//*[@id="password"]')
    submit_loc=(By.CLASS_NAME,'登录豆瓣')

    #Action
    def changeType(self):
        self.find_element(*self.login_type).click()

    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self,passwd):
        self.find_element(*self.passwd_loc).send_keys(passwd)
    
    def clicksub(self):
        self.find_element(*self.submit_loc).click()
    
    #测试帐号密码是否能够成功登录
def test_login(driver,username,passwd):
    login_page=LoginDouban(driver)
    login_page.open()
    login_page.changeType()
    login_page.input_username(username)
    login_page.input_password(passwd)
    login_page.clicksub()

def main():
    try:
        driver=webdriver.Chrome()
        username=''
        passwd=''
        test_login(driver,username,passwd)
        time.sleep(5)
        text=driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]').text
        assert (text=='是个难人的帐号'),'用户名不匹配，登录失败'
        
    finally:
        driver.close()

if __name__== '__main__':
    main()
        
    



