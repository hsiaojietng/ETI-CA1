from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def NavToBlog():
    #Click on hamburger button
    try:
        doc = browser.find_element_by_xpath("(//span[contains(@class, 'navbar-toggler-icon')])")
        doc.click()
    except:
        pass
    #Click on Home link
    doc = browser.find_element_by_xpath("(//a[contains(@class, 'nav-link')])[2]")
    doc.click()
    return browser.find_element_by_xpath("//h1")

def NavToHome():
    #Click on hamburger button
    try:
        doc = browser.find_element_by_xpath("(//span[contains(@class, 'navbar-toggler-icon')])")
        doc.click()
    except:
        pass
    #Click on Blog link
    doc = browser.find_element_by_xpath("(//a[contains(@class, 'nav-link')])[1]")
    doc.click()
    return browser.find_element_by_xpath("(//h1)[1]")

def NavToComment():
    return browser.find_element_by_xpath("//textarea").get_attribute("placeholder")

def NavToBlogPages():
    #Click into a blog
    doc = browser.find_element_by_xpath("(//a[contains(@href, '/blog/3/')])")
    doc.click()
    return browser.find_element_by_xpath("//h1")

def NavToProjectPages():
    #Click into a Project
    doc = browser.find_element_by_xpath("(//a[contains(@href, '/projects/1/')])")
    doc.click()
    return browser.find_element_by_xpath("(//h5)[1]")

def ViewSelfIntro():
    #Click on hamburger button
    try:
        doc = browser.find_element_by_xpath("(//span[contains(@class, 'navbar-toggler-icon')])")
        doc.click()
    except:
        pass
    #Click home link
    doc = browser.find_element_by_xpath("(//a[contains(@class, 'nav-link')])[2]")
    doc.click()
    #Click into a SelfIntro
    doc = browser.find_element_by_xpath("(//a[contains(@href, '/blog/4/')])")
    doc.click()
    return browser.find_element_by_xpath("//h1")

def ViewHobbies():
    return browser.find_element_by_xpath("(//h1)[2]")

def ViewCCA():
    return browser.find_element_by_xpath("(//h1)[3]")



browser = webdriver.Chrome()
browser.get('http://localhost:8000/projects/')

#Related to Home page (Blog index)
NavToBlog()
NavToBlogPages()
NavToComment()
ViewSelfIntro()

#Related to Projects
NavToHome()
ViewHobbies()
ViewCCA()
NavToProjectPages()








    



