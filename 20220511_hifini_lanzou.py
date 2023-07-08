import time
from selenium import webdriver

# 想法是输入hifini的通用格式，下载到特定文件夹
# 比如：链接: https://www.lanzoui.com/i9zgwhe 提取码: i492
# 下载到 E:\Music_Temp

print("Started")
print("please check if ChromeDriver version is correct")
print("please check if links.txt is correct")
# use try catch to avoid error for error version next time

driver = webdriver.Edge(
    "D:/apps/Music/Script/edgedriver_win64/msedgedriver.exe"
)  # Driver location 浏览器下载位置
# driver.get("https://www.lanzoui.com")
# check

file1 = open("links.txt", "rb")  # links放在文本中，例子格式：
# 链接: https://hifini.lanzoui.com/iIVmKk4m54f 提取码: cbbk
Lines = file1.readlines()
count = 0
while 1:
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))

        # val = input("Enter link: ")
        # print(val)
        link = line.split()
        print(link[1].decode())
        print(link[3].decode())

        driver.get(link[1].decode())

        driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(link[3].decode())

        driver.find_element_by_xpath('//*[@id="passwddiv"]/div/div[3]/div').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="downajax"]/a').click()

    time.sleep(20000000)
