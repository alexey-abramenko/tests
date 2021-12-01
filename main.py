from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button1 = browser.find_element_by_id('book')
    button1.click()

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_id('solve')

#     button = browser.find_element_by_css_selector('.btn')
    button.click()

#     button1 = browser.find_element_by_css_selector('.trollface')
#     button1.click()
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)

#     confirm = browser.switch_to.alert
#     confirm.accept()
#     input1 = browser.find_element_by_name('firstname')
#     input1.send_keys('t')
#     input2 = browser.find_element_by_name('lastname')
#     input2.send_keys('t')
#     input3 = browser.find_element_by_name('email')
#     input3.send_keys('test@mail.ru')
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, 'test.txt')
#     upload = browser.find_element_by_id('file')
#     upload.send_keys(file_path)
#     num = int(browser.find_element_by_id('input_value').text)
#     result = calc(num)
#     input1 = browser.find_element_by_id('answer')
#     input1.send_keys(result)
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     count = int(first.text) + int(second.text)
#     browser.find_element_by_tag_name("select").click()
#     browser.find_element_by_css_selector(select).click()
#     x = x_element.get_attribute('valuex')
#     y = calc(x)
#     input1 = browser.find_element_by_id('answer')
#     input1.send_keys(y)
#     option1 = browser.find_element_by_id("robotCheckbox")
#     option1.click()
#     option2 = browser.find_element_by_id('robotsRule')
#     option2.click()
#     input1 = browser.find_element_by_name("first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
# #     button = browser.find_element_by_css_selector('//button.btn[text()="Submit"]')
#     button = browser.find_element_by_xpath('//button[text()="Submit"]')
#     button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла