from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

def CreateCategory():
    browser.get("http://localhost:8000/admin/blog/category/add/")
    doc = browser.find_element_by_xpath("//input[contains(@type, 'text')]").send_keys('Facts')
    doc =  browser.find_element_by_xpath("//input[contains(@value, 'Save')][1]")
    doc.click()
    return browser.find_element_by_xpath("//li[contains(@class, 'success')]").get_attribute("class")

def DeleteCategory():
    browser.get("http://localhost:8000/admin/blog/category/")
    doc = browser.find_element_by_xpath("(//th//a)[1]")
    doc.click()
    doc = browser.find_element_by_xpath("//p//a")
    doc.click()
    doc = browser.find_element_by_xpath("//input[contains(@type, 'submit')]")
    doc.click()
    return browser.find_element_by_xpath("//li[contains(@class, 'success')]").get_attribute("class")

def EditCategory():
    doc = browser.find_element_by_xpath("(//th//a)[1]")
    doc.click()
    browser.find_element_by_xpath("//input[contains(@type, 'text')]").clear()
    doc = browser.find_element_by_xpath("//input[contains(@type, 'text')]").send_keys('Additional Facts')
    doc = browser.find_element_by_xpath("//input[contains(@name, '_save')]")
    doc.click()
    return browser.find_element_by_xpath("//li[contains(@class, 'success')]").get_attribute("class")

def CreateBlog():
    browser.get("http://localhost:8000/admin/blog/post/add/")
    doc = browser.find_element_by_xpath("//input[contains(@name, 'title')]").send_keys('Interesting Facts')
    doc = browser.find_element_by_xpath("//textarea[contains(@name, 'body')]").send_keys("IT is the largest growing industry")
    doc = browser.find_element_by_xpath("//option[1]")
    doc.click()
    doc =  browser.find_element_by_xpath("//input[contains(@value, 'Save')][1]")
    doc.click()
    return browser.find_element_by_xpath("//li[contains(@class, 'success')]").get_attribute("class")

def DeleteBlog():
    browser.get("http://localhost:8000/admin/blog/post/")
    doc = browser.find_element_by_xpath("(//th//a)[1]")
    doc.click()
    doc = browser.find_element_by_xpath("//a[contains(@class, 'deletelink')]")
    doc.click()
    doc = browser.find_element_by_xpath("//input[contains(@type, 'submit')]")
    doc.click()
    return browser.find_element_by_xpath("//li[contains(@class, 'success')]").get_attribute("class")

def EditBlog():
    browser.get("http://localhost:8000/admin/blog/post/")
    doc = browser.find_element_by_xpath("(//th//a)[1]")
    doc.click()
    browser.find_element_by_xpath("//input[contains(@type, 'text')]").clear()
    browser.find_element_by_xpath("//textarea[contains(@name, 'body')]").clear()
    doc = browser.find_element_by_xpath("//input[contains(@type, 'text')]").send_keys('An Additional Fact')
    doc = browser.find_element_by_xpath("//textarea[contains(@name, 'body')]").send_keys('This fact should be about me!')
    doc = browser.find_element_by_xpath("(//select//option)[3]")
    doc.click()
    doc = browser.find_element_by_xpath("//input[contains(@name, '_save')]")
    doc.click()
    return browser.find_element_by_xpath("//li[contains(@class, 'success')]").get_attribute("class")

def CreateUser():
    browser.get("http://localhost:8000/admin/auth/user/")
    doc = browser.find_element_by_xpath("//a[contains(@class, 'addlink')]")
    doc.click()
    browser.find_element_by_xpath("//input[contains(@name, 'username')]").send_keys('JohnnyDoe')
    browser.find_element_by_xpath("//input[contains(@name, 'password1')]").send_keys('DjangoProject@1')
    browser.find_element_by_xpath("//input[contains(@name, 'password2')]").send_keys('DjangoProject@1')
    doc = browser.find_element_by_xpath("//input[contains(@name, '_save')]")
    doc.click()
    return browser.find_element_by_xpath("//li[contains(@class, 'success')]").get_attribute("class")

def DeleteUser():
    browser.get("http://localhost:8000/admin/auth/user/")
    doc = browser.find_element_by_xpath("(//th[contains(@class, 'field-username')]//a)[1]")
    doc.click()
    doc = browser.find_element_by_xpath("//p//a[contains(@class, 'deletelink')]")
    doc.click()
    doc = browser.find_element_by_xpath("//div//input[contains(@type, 'submit')]")
    doc.click()
    return browser.find_element_by_xpath("//li[contains(@class, 'success')]").get_attribute("class")
    



browser = webdriver.Chrome()
browser.get('http://localhost:8000/admin/')
browser.find_element_by_xpath("//input[contains(@name, 'username')]").send_keys("nghsiaojiet")
browser.find_element_by_xpath("//input[contains(@name, 'password')]").send_keys("04D68p99")
doc = browser.find_element_by_xpath("//input[contains(@type, 'submit')]")
doc.click()

CreateCategory()
EditCategory()

CreateBlog()
EditBlog()
DeleteBlog()

DeleteCategory()

CreateUser()
DeleteUser()

browser.close()





    



