import time
import math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
# На новой форме решить капчу для роботов, чтобы получить число с ответом
    value = browser.find_element_by_id("input_value")    
    x = value.text
    y = (str(math.log(abs(12*math.sin(int(x))))))
# Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)    
# Нажать на кнопку "Submit".
    button2 = browser.find_element_by_id("solve")
    button2.click()       
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    #  пустая строка
