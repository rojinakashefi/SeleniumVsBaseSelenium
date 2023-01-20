# Selenium

Implemented google map automated test using selenium.

### Requirements

1. Install chrome webdriver based on your chrome version

2. Locate it on the code

3. ```
   pip install -r requirements.txt
   ```

4. Output
   
   ![oxford.png](https://github.com/rojinakashefi/SeleniumVsBaseSelenium/blob/main/pictures/oxford.png)
   
   

5. Good resources : [first](https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html#selenium.webdriver.remote.webdriver.WebDriver.find_element), [second](https://stackoverflow.com/questions/71097378/selenium-common-exceptions-invalidargumentexception-message-invalid-argument), [third](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html#module-selenium.webdriver.common.by)

# Base Selenium

Implemented two projects:

    First project : Purchesing coffess online and add it to shopping cart.

    Second project : Check login 

### Requirements

1. - ```
     pip install -r requirements.txt
     ```

2. Output
   
   First project :
   https://github.com/rojinakashefi/SeleniumVsBaseSelenium/blob/main/pictures/first.gif
   
   Second project:
   https://github.com/rojinakashefi/SeleniumVsBaseSelenium/blob/main/pictures/second.gif

3. Good resources : [first](https://seleniumbase.io/)

----

## Difference between Selenium and Base selenium

1.  SeleniumBase uses default timeout values when not set:  
   `self.click("button")` 
   With raw Selenium, methods would fail instantly (*by default*) if an element needed more time to load: 
   `self.driver.find_element(by="css selector", value="button").click()`  
   (Reliable code is better than unreliable code.)

2.  SeleniumBase lets you change the explicit timeout values of methods:  
   `self.click("button",timeout=10)` 
   With raw Selenium, that requires more code: 
   `WebDriverWait(driver,10).until(EC.element_to_be_clickable("css selector", "button")).click()`  
   (Simple code is better than complex code.)
