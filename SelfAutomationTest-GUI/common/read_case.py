
from runnner.func_test import *
import os
import xlrd

def do_case(sheetname):
    #定义一个对象，来自于函数集合的那一个类
    web = UI_auto_test()

    filepath = os.path.abspath('../data')
    #先定义文件位置
    filename = filepath + "/autotest.xlsx"
    
    #使用xlrd来打开文件
    excel = xlrd.open_workbook(filename)
    
    #打开文档中的某一个sheet页
    sheet = excel.sheet_by_name(sheetname)
    
    #获取数据行数
    r_num = sheet.nrows
    
    #读取每一行的数据
    for r in range(1,r_num):
        row_info = sheet.row_values(r)
        operate,method,position,data = row_info[2],row_info[3],row_info[4],row_info[5]
        
        #根据operate定义的内容，来调用不同的函数
        if operate == u'打开':
            web.open_test(data)
        elif operate == u'点击':
            web.click_test(method,position)
        elif operate == u'框架':
            web.frame_test(method,position,data)
        elif operate == u'窗口':
            web.window_test()
        elif operate == u'滑动':
            web.drag_test(method,position,data)
        elif operate == u'输入':
            web.input_test(method, position, data)
        elif operate == u'q输入':
            web.q_input_test(method, position, data)
        elif operate == u'校验':
            web.check_test(method, position, data)
        elif operate == u'等待':
            web.wait_test(data)
        elif operate == u'下拉框':
            web.select_test(method, position, data)
        elif operate == u'拖动':
            web.move_test(method, position)
        elif operate == u'键盘':
            web.keys_test(method, position, data)
        elif operate == u'js弹框':
            web.js_alert_test(data)
        elif operate == u'退出':
            web.close_window()
            
            
    
     
     
    
    
    