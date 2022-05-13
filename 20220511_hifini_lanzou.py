import time
from selenium import webdriver

#想法是输入hifini/lanzou的通用格式，下载到特定文件夹
#比如：链接: https://www.lanzoui.com/i9zgwhe 提取码: i492
#下载到download

print("Started")
print("please check if ChromeDriver version is correct")

driver = webdriver.Chrome('xxxxxxxxxxxxxxx') #ChromeDriver location
driver.get("https://www.lanzoui.com") 
#check
while 1:
    val = input("Enter link: ")
    print(val)
    link=val.split()
    print(link[1])
    print(link[3])
    
    driver.get(link[1])
    
    driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(link[3])
    

    driver.find_element_by_xpath('//*[@id="passwddiv"]/div/div[3]/div').click()
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="downajax"]/a').click()

