#Code by Tashinga Musanhu
#Started on 1 April 2020
#Purpose used to automate human interaction on instagram

#--------------Establish a login using a web server

from selenium import webdriver
import time 

print ("Starting")

driver = webdriver.Firefox()

"""

Note you may get some errors saying: Message: 'geckodriver.exe' executable needs to be in PATH. 
make sure geckdriver.exe is in usr/local/bin
"""

def login(username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(3)

    #go to the loginpage and find the login section. Clear it and send the uername to that field
    username_field = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input") 
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(2)
    
    print("Reached the middle")

    password_field = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(3)

    #click the login button 
    login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
    login.click()
    time.sleep(3)

print("Reached the end")


