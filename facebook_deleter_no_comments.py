from selenium import webdriver
import time


def main():
    username_str = "temp@gmail.com"
    password_str = "password"
    facebook_profile_page_str = "https://www.facebook.com/user.info/"
    browser = webdriver.Firefox(executable_path='./geckodriver')
    browser.get('https://www.facebook.com/')
    time.sleep(5)
    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    submit   = browser.find_element_by_id("u_0_b")
    username.send_keys(username_str)
    password.send_keys(password_str)
    submit.click()
    time.sleep(5)
    browser.get(facebook_profile_page_str + 'photos_all')
    time.sleep(5)
    no_exception = 0
    while no_exception == 0:
        try:
            edit_icon = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[3]/div[1]/div/div/a/div/div")
            edit_icon.click()
            time.sleep(2)
            delete_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]")
            delete_button.click()
            time.sleep(2)
            confirm = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]")
            confirm.click()
            time.sleep(5)
        except:
            no_exception = 1
            pass

    print("Photos Deleted")
    browser.get(facebook_profile_page_str+'photos_of')
    time.sleep(5)
    no_exception = 0
    while no_exception == 0:
        try:
            edit_icon = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[3]/div[1]/div/div/a/div/div")
            edit_icon.click()
            time.sleep(2)
            remove_tag_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[1]")
            remove_tag_button.click()
            time.sleep(2)
            confirm = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]")
            confirm.click()
            time.sleep(5)
            browser.get(facebook_profile_page_str+'photos_of')
            time.sleep(5)
        except:
            no_exception = 1
            pass

    print("Tags Deleted")

    print("Completed")


if __name__ == '__main__':
    main()


