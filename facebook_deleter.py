from selenium import webdriver
import time


def main():
    # Step 0: Set variables
    #username_str = "temp@gmail.com"
    username_str = ""
    #password_str = "password"
    password_str = ""
    #facebook_profile_page_str = "https://www.facebook.com/user.info/"
    facebook_profile_page_str = ""

    # Step 1: Open Firefox
    browser = webdriver.Firefox(executable_path='./geckodriver')

    # Step 2: Navigate to Facebook
    browser.get('https://www.facebook.com/')
    time.sleep(5)

    # Step 3: Search and Enter the Email and Password
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    submit   = browser.find_element_by_id("u_0_b")
    username.send_keys(username_str)
    password.send_keys(password_str)

    # Step 4) Click Login
    submit.click()
    time.sleep(5)

    # Step 5) Go to photos page
    browser.get(facebook_profile_page_str + 'photos_all')
    time.sleep(5)

    # Loop through all photos
    no_exception = 0
    while no_exception == 0:
        try:
            # Step 6) Expand edit menu
            edit_icon = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[3]/div[1]/div/div/a/div/div")
            edit_icon.click()
            time.sleep(2)

            # Step 7) Click delete button
            delete_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]")
            delete_button.click()
            time.sleep(2)
    
            # Step 8) Click confirm delete
            confirm = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]")
            confirm.click()
            time.sleep(5)
        except:
            no_exception = 1
            pass

    print("Photos Deleted")

    # Step 9) Go to photos of you page
    browser.get(facebook_profile_page_str+'photos_of')
    time.sleep(5)

    # Loop through all taggeds
    no_exception = 0
    while no_exception == 0:
        try:
            # Step 10) Expand edit menu
            edit_icon = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[3]/div[1]/div/div/a/div/div")
            edit_icon.click()
            time.sleep(2)

            # Step 11) Click remove tag button
            remove_tag_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[1]")
            remove_tag_button.click()
            time.sleep(2)
    
            # Step 12) Click confirm remove tag
            confirm = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]")
            confirm.click()
            time.sleep(5)

            # Step 13) Refresh photos of you page
            browser.get(facebook_profile_page_str+'photos_of')
            time.sleep(5)
        except:
            no_exception = 1
            pass

    print("Tags Deleted")

    print("Completed")


if __name__ == '__main__':
    main()


