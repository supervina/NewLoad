#coding=utf-8
from selenium import webdriver
import time,os
'''
ActionChains类继承自object类，但是需要为其传入一个driver对象，即ActionChains(driver)
此类常用于模拟鼠标键盘操作
'''
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

class UI_auto_test():
    
    def __init__(self):        
        self.t = time.strftime("%Y-%m-%d",time.localtime())  
         
    
    #这是一个专门用来定位元素的函数，通过接收方法和位置，来判断元素是否存在，如果存在，就把得到的元素返回给调用它的地方
    def position_test(self,method,position):
#         driver = self.driver
        try:
            if method == u"link_text":
                ele = driver.find_element_by_link_text(position)
            elif method == u"id":
                ele = driver.find_element_by_id(position)
            elif method == u"xpath":
                ele = driver.find_element_by_xpath(position)
            elif method == u"css":
                ele = driver.find_element_by_css_selector(position)
            elif method == u"name":
                ele = driver.find_element_by_name(position)
        except Exception:
            print("没有这个元素")
            path = os.path.abspath('../report/')
            name = path+self.t+".png"
            driver.get_screenshot_as_file(name)
        else:
            return ele
                
    
    #这是一个打开网站的函数，通过data来接收url的值
    def open_test(self,data):
        #driver = self.driver
        #最大化窗口 
        driver.maximize_window()
        #设置隐形等待时间
        driver.implicitly_wait(10)
        #打开网站
        driver.get(data)   
        
    def click_test(self,method,position):
        ele = self.position_test(method, position)
        ele.click()
        
    def input_test(self,method, position, data):
        ele = self.position_test(method, position)
        ele.clear()
        ele.send_keys(data)
        
    def q_input_test(self,method, position, data):
#         driver = self.driver
    #     data = data.encode("utf-8")      如果页面出现中文编码问题，就将excel中的unicode重新编码成utf-8
        ele = self.position_test(method, position)
        action = ActionChains(driver)
        #
        action.move_to_element(ele).click().send_keys(data).perform()
        
    def frame_test(self,method,position,data):
#         driver = self.driver
        if int(data) == 1:
            ele = self.position_test(method,position)
            driver.switch_to.frame(ele)    
        elif int(data) == 0:
            driver.switch_to_default_content()
        elif int(data) == 2:
            driver.switch_to.parent_frame()
    
    def window_test(self):
#         driver = self.driver
        handle = driver.window_handles
        driver.switch_to.window(handle[-1])
        
    def drag_test(self,method,position,data):
#         driver = self.driver
        s = self.position_test(method,position)
        offset = str(data).split(",")
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(s, int(offset[0]), int(offset[1])).perform()
        
    def check_test(self,method,position,data):
        data = int(data)
        if data == 1:
            ele = self.position_test(method,position)
            if ele == None:
                raise Exception  #raise是由用户来手动的主动的抛出错误信息
        elif data == 0:
            ele = self.position_test(method,position)
            if ele != None:
                raise Exception 
            
    def wait_test(self,data):
        time.sleep(int(data))
    
    def select_test(self,method,position,data):
        ele = self.position_test(method, position)
        s = Select(ele)
        s.select_by_visible_text(data)
        
    def move_test(self,method,position):
        ele = self.position_test(method, position)
        action = ActionChains(driver)
        action.click_and_hold().move_to_element(ele).release().perform()
    
    def keys_test(self,method,position,data):
        ele = self.position_test(method, position)
        if data == u'下箭头':
            ele.send_keys(Keys.ARROW_DOWN)
        elif data == u'回车':
            ele.send_keys(Keys.ENTER)
        elif data == u'HOME':
            ele.send_keys(Keys.HOME)
    
    def js_alert_test(self,data):
#         driver = self.driver
        alert = driver.switch_to_alert()
        data = int(data)
        if data == 1:
            alert.accept()
        elif data == 0:
            alert.dismiss()

    def close_window(self):
        dr=driver.close()
    
    