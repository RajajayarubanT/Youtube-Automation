from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import win32clipboard

def sleep_for_period_of_time():
    limit = random.randint(7,10)
    time.sleep(limit)


def main():
    options = webdriver.ChromeOptions()
    
    # options.add_argument("--lang=en") #default
    
    userdatadir = "C:/Users/rajaj/AppData/Local/Google/Chrome/User Data" #existing chrome account
    options.add_argument(f"--user-data-dir={userdatadir}")
    
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    browser.get("https://www.youtube.com")
    time.sleep(2)    

    search_input_xpath = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"
    search_value = "trading community in coimbatore"
    
    
    search_input = browser.find_element(By.XPATH, search_input_xpath)
    search_input.send_keys(search_value)
    search_input.send_keys(Keys.RETURN)
    sleep_for_period_of_time()
    

    limit = 10
    
    username_stack = []
    email_stack = []
    
    for i in range(limit):
        
        username_xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[" + str(i+1) + "]/div[1]/div/div[2]/ytd-channel-name/div/div/yt-formatted-string/a"
        
        username = browser.find_element(By.XPATH, username_xpath)
        channel_link = username.get_attribute('href')
        username_stack.append(channel_link)
        
        username.click()
        time.sleep(1)
    
        user_about = browser.current_url+ "/about"
        
        browser.get(user_about)
        sleep_for_period_of_time()
        
        try:
            print( '\n', 'Stage 0', '\n')
            verify_email_xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[1]/div[4]/table/tbody/tr[1]/td[3]/ytd-button-renderer/yt-button-shape/button"

            verify_email = browser.find_element(By.XPATH, verify_email_xpath)
            
            verify_email.click()
            time.sleep(2)
            
            print( '\n', 'Stage 1', '\n')
            
            verify_human_xpath = "/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]"
            verify_human = browser.find_element(By.XPATH, verify_human_xpath)
            verify_human.click()
            time.sleep(2)
            
            print( '\n', 'Stage 2', '\n')


            submit_verify_xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[1]/div[4]/table/tbody/tr[1]/td[4]/button"
            submit_verify = browser.find_element(By.XPATH, submit_verify_xpath)
            submit_verify.click()
            time.sleep(2)
            
            print( '\n', 'Stage 3', '\n')

            email_xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[1]/div[4]/table/tbody/tr[1]/td[6]/a"  
            email = browser.find_element(By.XPATH, email_xpath)
            
            print( '\n', 'Stage 4', '\n')

            email_stack.append({
                "channel": channel_link,
                "email": email.text
            })
                        
        except:
            print(user_about, "No Email Found")
            
        browser.back()
        
        
    print(email_stack)
  

if __name__ == "__main__":
    main()
