from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

def NavToBlog():
    #Click on hamburger button
    doc = browser.find_element_by_xpath("(//span[contains(@class, 'navbar-toggler-icon')])")
    doc.click()
    #Click on Home link
    doc = browser.find_element_by_xpath("(//a[contains(@class, 'nav-link')])[2]")
    doc.click()
    return browser.find_element_by_xpath("//h1")

def NavToHome():
    #Click on hamburger button
    doc = browser.find_element_by_xpath("(//span[contains(@class, 'navbar-toggler-icon')])")
    doc.click()
    #Click on Blog link
    doc = browser.find_element_by_xpath("(//a[contains(@class, 'nav-link')])[1]")
    doc.click()
    return browser.find_element_by_xpath("(//h1)[1]")

def NavToComment():
    return browser.find_element_by_xpath("//textarea").get_attribute("placeholder")

def NavToBlogPages():
    #Click into a blog
    doc = browser.find_element_by_xpath("(//h2//a)[2]")
    doc.click()
    return browser.find_element_by_xpath("//h1")

def NavToProjectPages():
    #Click into a Project
    doc = browser.find_element_by_xpath("(//div//div//div//a)[1]")
    doc.click()
    return browser.find_element_by_xpath("(//h5)[1]")

def ViewSelfIntro():
    #Click on hamburger button
    doc = browser.find_element_by_xpath("(//span[contains(@class, 'navbar-toggler-icon')])")
    doc.click()
    #Click home link
    doc = browser.find_element_by_xpath("(//a[contains(@class, 'nav-link')])[2]")
    doc.click()
    #Click into a SelfIntro
    doc = browser.find_element_by_xpath("(//h2//a)[1]")
    doc.click()
    return browser.find_element_by_xpath("//h1")

def ViewHobbies():
    return browser.find_element_by_xpath("(//h1)[2]")

def ViewCCA():
    return browser.find_element_by_xpath("(//h1)[3]")

def CreateComment():
    doc = browser.find_element_by_xpath("//input[contains(@name, 'author')]").send_keys("John Low")
    doc = browser.find_element_by_xpath("//textarea").send_keys("Your Resume is interesting")
    doc = browser.find_element_by_xpath("//button[contains(@type, 'submit')]")
    doc.click()
    return browser.find_element_by_xpath("//*[contains(text(), 'John Low')]")



browser = webdriver.Chrome()
browser.get('http://localhost:8000/projects/')

#Related to Home page (Blog index)
NavToBlog()
NavToBlogPages()
NavToComment()
CreateComment()
ViewSelfIntro()

#Related to Projects
NavToHome()
ViewHobbies()
ViewCCA()
NavToProjectPages()

browser.close()








    



