from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

class Test_Mes():
    
    def __init__ (self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 
   
    def login(self,test_url): # 登录操作
        try:
            self.driver.get(test_url)
            self.driver.maximize_window()
            self.driver.find_element_by_id('userName').clear()
            self.driver.find_element_by_id('userName').send_keys('cs')
            self.driver.find_element_by_id('password').clear()
            self.driver.find_element_by_id('password').send_keys('123456')
            self.driver.find_element_by_id('DengLu').click()
        except Exception as e:
            print('登录error:',e)
            self.driver.quit()
            os._exit(1)
        else:    
            print('登录成功')
    
    def PC (self):# 排程相关操作
        try:    
            #self.driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[2]/a").click() #生产计划
            self.driver.find_element_by_xpath('//li/a[@data-text="生产计划"]').click()
            self.driver.find_element_by_xpath('//a[@data-text="生产排程"]').click() #生产排程
            time.sleep(3)
            # self.find_element_by_xpath('//*[@id="ShowAndHide"]').click()
           
            self.driver.switch_to.frame(1)
            self.driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[4]').click()#周视图
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[3]').click()#月视图
            time.sleep(2)
            # 11 | click | id=ShowAndHide |  | 
            self.driver.find_element_by_id("ShowAndHide").click()# 隐藏创建排程
            time.sleep(2)
            self.driver.find_element_by_id("ShowAndHide").click()# 显示创建排程
            time.sleep(2)
            # 12 | click | id=nearPlan |  | 
            self.driver.find_element_by_id("nearPlan").click()# 近期发货计划查看
            time.sleep(3)    
            # 13 | click | css=.btn-info:nth-child(1) |  | 
            self.driver.find_element_by_css_selector(".btn-info:nth-child(1)").click()# 关闭近期发货计划
            time.sleep(3)
            # 14 | selectFrame | relative=parent |  | 
            
            # self.driver.find_elements_by_link_text('导入计划').click()
            #创建排程
            def Add_PC(self):
                self.driver.find_element_by_id('s2id_BlankName')#定位到配方名称
                self.driver.find_element_by_xpath('//*[@id="BlankName"]/option[2]').click()#选择配方
                self.driver.find_element_by_id('ProductNumber').send_keys(1000)
                js = 'document.getElementById("ProductTimeStart").removeAttribute("readonly")'#js代码不能直接处理，先作为字符串
                self.driver.execute_script(js)#执行js代码，修改readonly属性
                self.driver.find_element_by_id('ProductTimeStart').send_keys('2020-01-16 09:30')#直接输入时间
                
                self.driver.find_element_by_xpath('//*[@id="event_add"]').send_keys("\n")
                self.driver.find_element_by_xpath('//*[@id="event_add"]').click()
                time.sleep(5)
            self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div[3]/ul/li/button").click()# 导出当月计划
            time.sleep(5)
            self.driver.find_element_by_link_text('导出表头').click() # 导出表头
            time.sleep(3)
            Add_PC(self)   
            
        except Exception as e:
            print("排程error:",e)
            time.sleep(3)
            self.driver.switch_to_alert().accept()
            ''' 
            捕获到alert异常，处理为（switch_to_alert() 　　#定位弹出对话
                            text() 　　                  #获取对话框文本值
                            accept()                     #相当于点击"确认"
                            dismiss()                    #相当于点击"取消"
                            send_keys()                  # 输入值，这个alert和confirm没有输入对话框，所以这里就不能用了，所以这里只能使用在prompt这里。）
            '''
            time.sleep(3)

        else:
            print('操作成功')
    
    def TC (self):# 退出操作
        try:    
            self.driver.switch_to.default_content()
            # 15 | click | linkText=退出 |  | 
            self.driver.find_element_by_link_text("退出").click()
            time.sleep(3)
            #self.driver.quit()
        except Exception as e:
            print('退出error:',e)
            self.driver.quit()
            os._exit(1)
        else:    
            print('退出成功')

if __name__ == "__main__":
    
    test_url = 'http://120.224.50.57:8093/'#'http://localhost:52760'
    Chrome_browser = Test_Mes()
    Chrome_browser.login(test_url) # 登录
    Chrome_browser.PC()# 排程
    Chrome_browser.TC()# 退出
