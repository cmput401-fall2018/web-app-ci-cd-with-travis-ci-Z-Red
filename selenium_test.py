from selenium import webdriver
from selenium.webdriver.common import keys

def test_home():
    driver = webdriver.Chrome()
    driver.get("http://162.246.157.229")

    elem = driver.find_element_by_id("name")
    assert elem != None

    elem = driver.find_element_by_id("about")
    assert elem != None

    elem = driver.find_element_by_id("skills")
    assert elem != None

    elem = driver.find_element_by_id("education")
    assert elem != None

    elem = driver.find_element_by_id("work")
    assert elem != None

    elem = driver.find_element_by_id("contact")
    assert elem != None
