from time import sleep
from selenium import webdriver

browser = webdriver.Chrome('C:\driver\chromedriver.exe')

browser.get('http://localhost/.atest/index.php')

idk=browser.find_element_by_name("id")
imie=browser.find_element_by_name("imie")
nazwisko=browser.find_element_by_name("nazwisko")
miasto=browser.find_element_by_name("miasto")

idk.send_keys('ABC13')
imie.send_keys('Piotr')
nazwisko.send_keys('AAAAAB')
miasto.send_keys('Lublin')
sleep(2)
button1=browser.find_element_by_id("s1")
button1.click()

browser.save_screenshot('C:\ekrany\zapis.png')
sleep(2)
browser.find_element_by_xpath ("//a [@href='edit.php?id=ABC13']").click()

miasto2=browser.find_element_by_name("miasto")

miasto2.clear();
sleep(2)
miasto2.send_keys('Warszawa');
sleep(2)
browser.find_element_by_xpath ("//input [@value='zapisz']").click()
sleep(2)
browser.find_element_by_xpath ("//a [@href='index.php']").click()

browser.save_screenshot('C:\ekrany\edycja.png');
sleep(2)
browser.find_element_by_xpath ("//a [@href='usun.php?id=ABC13']").click()
sleep(2)
browser.find_element_by_xpath ("//a [@href='index.php']").click()

browser.save_screenshot('C:\ekrany\del.png')
sleep(2)
browser.close()
