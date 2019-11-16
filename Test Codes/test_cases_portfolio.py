import pytest
from SRC.pytest_portfolio import *

def test_NavToHome():
    assert "Blog Index"

def test_NavToBlog():
    assert "Projects I Have Done"

def test_NavToComment():
    assert "Leave a comment!"

def test_NavToBlogPages():
    #One of the blog page will be Resume
    assert "Resume"

def test_NavToProjectPages():
    assert "About the project"
    
def test_ViewResume():
    assert "Resume"

def test_ViewSelfIntro():
    assert "Self-Intro"

def test_ViewHobbies():
    assert "Hobbies"

def test_ViewCCA():
    assert "CCAs"

def test_CreateComment():
    assert "John Low"

