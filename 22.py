from selenium import webdriver
import urllib.request
import time


driver = webdriver.Chrome()
driver.get("https://erp.iitkgp.ac.in/IIT_ERP3/showmenu.htm")
driver.maximize_window()
assert "Welcome to ERP" in driver.title
a = driver.title
print(a)

user = driver.find_element_by_id("user_id")
user.send_keys("*****")

psswd = driver.find_element_by_id("password")
psswd.send_keys("***")

time.sleep(1)

question = driver.find_element_by_id("question")


answer = driver.find_element_by_id("answer")

q = question.text
q = q.lower()

if (q.find("teacher") != -1):
    answer.send_keys("***")
elif(q.find("book") != -1):
    answer.send_keys("***")
elif(q.find("game") != -1):
    answer.send_keys("***")

aca = driver.find_element_by_class_name("btn-primary").click()

time.sleep(2)

driver.find_element_by_id("skiplink").click()

time.sleep(1)

aca = driver.find_elements_by_tag_name('a')
aca[8].click()

time.sleep(1)

fed = driver.find_elements_by_tag_name('a')
for el in fed:
    if (el.text.find("Feedback") != -1):
        el.click()
        time.sleep(.5)
        fed2 = driver.find_elements_by_tag_name('a')
        for el2 in fed2:
            if (el2.text.find("FeedBack Form") != -1):
                el2.click()
                time.sleep(.5)
                break
        break

frame=driver.switch_to.frame(driver.find_element_by_id('myframe'))
fed4=driver.find_elements_by_tag_name("a")
for el in fed4:
    el.click()
    time.sleep(.5)
    fed5 = driver.find_elements_by_css_selector("input[type='radio']")
    for el2 in fed5:
        el2.click()

        fed6 = driver.find_elements_by_css_selector("font[color='red']")
        for el3 in fed6:
            print(el3.text)

        break
    break
