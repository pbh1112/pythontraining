from selenium import webdriver

def get_chrome_driver():
    chrome_options = webdriver.ChromeOptions() 
    
    # Keeps the browser open
    chrome_options.add_experimental_option("detach", True)
    
    return webdriver.Chrome(options = chrome_options)



# Gets our chrome driver and opens our site
chrome_driver = get_chrome_driver()
chrome_driver.get("https://www.google.com/")
print('The browser should not close after you see this message')
chrome_driver.service.stop()