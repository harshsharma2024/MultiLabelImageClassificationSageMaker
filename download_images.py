from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Set the path to your webdriver executable (e.g., chromedriver.exe)
# Download from: https://sites.google.com/chromium.org/driver/
webdriver_path = '/usr/local/bin/chromedriver'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run in headless mode

# Set up the webdriver with the specified executable path and options
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the webpage with the download button
webpage_url = 'https://airtable.com/appsklPHcvUmDxDF9/tblh5I94k3MTaJT3t/rec4PkGsR3krFPOH4/flduEXiImPewv6zc5/attrsO5aZCDGDawvv'

try:
    # Open the webpage
    driver.get(webpage_url)
    print(driver.page_source)

    # Wait for some time to ensure the page is fully loaded (you may need to adjust the time)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Download")]')))

    # Wait for the download button to be clickable
    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download")]'))
    )

    # Click on the download button
    download_button.click()

    # Wait for some time to allow the download to complete (you may need to adjust the time)
    time.sleep(10)

finally:
    # Close the webdriver
    driver.quit()
