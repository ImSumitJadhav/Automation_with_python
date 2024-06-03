# #Note: 
# '''1.TO SOLVE PROBLEM OF CROME DRIVER: Download driver from given link and placed this chrome driver to 
# same directory which contains your scrapping python file.'''

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# url = 'https://www.moneycontrol.com/'

# # Headless mode
# options = Options()
# options.headless = True
# driver = webdriver.Chrome()
# driver.get(url)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
web = 'https://www.thesun.co.uk/sport/football/'

# Open a website with windows and frames
driver.get(web)

# Store the current window handle
main_window_handle = driver.current_window_handle

# Find and click on a link that opens a new window
new_window_link = driver.find_element(By.XPATH, "/html/body/div[5]/div/a[3]")
new_window_link.click()

# Wait for a new window to open
WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) == 2)

# Switch to the new window
for window_handle in driver.window_handles:
    if window_handle != main_window_handle:
        driver.switch_to.window(window_handle)
        break

# Now you can interact with elements in the new window
# For example, you can find an element by its XPath and interact with it
element_in_new_window = driver.find_element(By.XPATH, "/html/body/div[5]/div/a[8]")

# Close the new window
driver.close()

# Switch back to the main window
driver.switch_to.window(main_window_handle)

# Switch back to the main content
driver.switch_to.default_content()

# Close the browser
driver.quit()
