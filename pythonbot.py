#Code by Tashinga Musanhu
#Started on 1 April 2020
#Purpose used to automate human interaction on instagram

#--------------Establish a login using a web server

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import random

print ("Starting")

driver = webdriver.Firefox()

"""
I noticed that, you may get some errors saying: Message: 'geckodriver.exe' executable needs to be in PATH. 
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
    

    password_field = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(3)

    #click the login button 
    login = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
    login.click()
    time.sleep(3)


#explore hashtag pages and like some random pictures 

def like(hashtag):
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(5)

    #scroll down seven times
    for i in range(7):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    #look for the tag name, in this case each post is under the element a
    href_found = driver.find_elements_by_tag_name("a")

    #pcitures from that search get stored in an array 
    pics = [element.get_attribute('href') for element in href_found if '.com/p' in element.get_attribute('href') ]


    #note that this likes an infinite number of pictures. 
    #tune it to like a certain amount

    for element in pics:
        driver.get(element)
        time.sleep(5)

        like = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button")
        
        like.click()
        time.sleep(5)


#define comment, go to a certain hashtag and comment on a pic within that hashtag
def comment(hashtag): 
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(5)

    #scroll down seven times
    for i in range(7):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    #look for the tag name, in this case each post is under the element a
    href_found = driver.find_elements_by_tag_name("a")

    pics = [element.get_attribute('href') for element in href_found if '.com/p' in element.get_attribute('href') ]

    #now we can define a set of random comments to target specific group 
    #arr = ["hi, thats a lovely pic", "You should check out our page!"]
    

    #choose a random comment from the list
    #comment = arr[randomNum(arr)]
    comment = "that looks good!"

    for x in pics: 
        driver.get(x)
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    
        commentBox = lambda: driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea")
        commentBox().click()
        

        for word in comment: 
            commentBox().send_keys(word)
            time.sleep(random.randint(1,7)/30)

        #click enter
        commentBox().send_keys(Keys.ENTER)

#if the user supplies a list greater than 1 element then find a random number
#else default val = 0
def randomNum(arr): 
    if arr.size()> 1:
        num = random.randint(0,(arr.size()-1))
    else:
        num = 0
    return num
    


login("tastyrush", "HandCream123")
#like("foodie")

comment("foodie")



