from selenium import webdriver
import getpass

print("please enter your username and password for facebook login")
username = input("enter you username: ")
password = getpass.getpass("enter your password it would be hidden: ")
# Enter your password and it's safe and hidden


driver = webdriver.Chrome()  # To open the web browser(google chrome)


def fb_login(username, password):
    driver.get('https://www.facebook.com')  # To hit the URL(facebook)
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()

fb_login(username, password)
