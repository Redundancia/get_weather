from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

weather = []

weather_class_name = ".ik.dailyForecastCol"

driver.get("https://www.idokep.hu/30napos/Budapest")

try:
    content = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
    (By.CSS_SELECTOR, weather_class_name)))
    for index,element in enumerate(content):
        date= element.find_element(By.CSS_SELECTOR, ".ik.d-block.w-100.ik.interact").get_attribute("data-original-title").split("<br>")[1]
        max = int(element.find_element(By.CSS_SELECTOR, ".ik.max").text)
        min = int(element.find_element(By.CSS_SELECTOR, ".ik.min").text)
        try:
            rain = element.find_element(By.CSS_SELECTOR, ".ik.rainlevel-container").text
        except NoSuchElementException:
            rain = "No data"
        weather.append((min,max,rain,date))
finally:
    driver.quit()

json_output = json.dumps(weather, indent=4, ensure_ascii=False)
print(json_output)