
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




def gmeet(mail_address, password,url):

    browser=webdriver.Chrome(r'C:\Users\hp\chromedriver_win32 (1)\chromedriver')
    wait=WebDriverWait(browser,600) 

    # Login Page
    browser.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
 
    # input Gmail
    browser.find_element_by_id("identifierId").send_keys(mail_address)
    browser.find_element_by_id("identifierNext").click()
    browser.implicitly_wait(10)
 
    # input Password
    browser.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    browser.implicitly_wait(10)
    browser.find_element_by_id("passwordNext").click()
    browser.implicitly_wait(10)
    browser.get('https://google.com/')
    browser.implicitly_wait(100)
    
    browser.get(url)
    
    x_arg = '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div'
    target=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))# wait untill the the contact is found
    target.click()

    # turn off camera
    x_arg = '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div'
    target  = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
    target.click()
    
    while(True):
        pass









# mail_address = 'anshika.dubey@cumminscollege.in'
# password = 'Manansfan@08'   
# Glogin(mail_address, password)
# browser.get('https://meet.google.com/xby-zehb-ncf')
# joinNow()
# turnOffMicCam()
