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

    pics = [element.get_attribute('href') for element in href_found if '.com/p' in element.get_attribute('href') ]

    for element in pics:
        driver.get(element)
        time.sleep(5)

        like = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button")
        
        like.click()
        time.sleep(5)





login()
like("foodie")


print("Reached the end")


