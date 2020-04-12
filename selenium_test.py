from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = "harshadchavan141@gmail.com"
password = "Flatronw1941s#$"

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")

element = driver.find_element_by_id("email")
element.send_keys(username)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element = driver.find_element_by_id("contentarea")
element.send_keys(Keys.END)
element.clear()


# echo setx path "%PATH%;C:\Users\Harshad\Downloads\geckodriver-v0.26.0-win64"