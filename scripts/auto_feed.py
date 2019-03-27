#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Charles on 19-3-15
# Function: 


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def auto_feed(inputs):
    """
    养号任务实现
    :param account: Account类的实例，其中包含了账号相关的属性信息
    :param mode: 养号模式，0-代表自动模式，程序将会根据账号历史操作情况自动决定养号流程， 1-仅浏览 2-发状态 3-随机点赞 4-随机聊天
    :return: （code, result) code: 0-代表失败，1-代表成功， result： 处理结果描述
    """
    account_num = inputs['account']
    password = inputs['password']
    print('script runing:{},{}'.format(account_num, password))

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.facebook.com/')
    driver.implicitly_wait(10)
    # return True

    try:
        # email_box = driver.find_element_by_name('email')
        email_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        email_box.send_keys(account_num)
        time.sleep(0.5)
        password_box = driver.find_element_by_name('pass')
        password_box.send_keys(password)

        driver.get_screenshot_as_file('login.png')

        time.sleep(1)
        # login_btn = driver.find_element_by_id('u_0_2')
        login_btn = driver.find_element_by_css_selector('input[type="submit"]')
        print(login_btn)
        login_btn.click()

        time.sleep(3)

        driver.get_screenshot_as_file('home1.png')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        for i in range(50):
            ActionChains(driver).key_down(Keys.DOWN).perform()
            time.sleep(0.5)

        for i in range(50):
            ActionChains(driver).key_down(Keys.UP).perform()
            time.sleep(0.5)

        driver.get_screenshot_as_file('home2.png')


        # 跳去个人页面
        # profile = driver.find_element_by_css_selector('a[href^="https://www.facebook.com/profile"')
        # profile = driver.find_element_by_css_selector('a[href^="https://www.facebook.com/"')
        # profile = driver.find_element_by_css_selector('a[title^="Profile"')#也有可能叫个人主页
        # profile_url = profile.get_attribute("href")
        # print("profile url: ", profile_url)
        # driver.get(profile_url)

        time.sleep(5)
        print("111")


        # 搜索
        # search = driver.find_element_by_css_selector("input[name='q'")
        # search.send_keys("kobe bryant")
        # search.send_keys(Keys.ENTER)


        # posts = driver.find_element_by_css_selector("div[aria-autocomplete='list'")
        # time.sleep(2)
        # posts.send_keys("You make a better world by make yourself a better person.")

        time.sleep(1)

        driver.get_screenshot_as_file("post.png")

        time.sleep(1)

        driver.get_screenshot_as_file("post.png")
        # post_btn = driver.find_element_by_css_selector("button[type='submit'")
        #
        # post_btn.click()
        # if to_post:
        #     posts.send_keys(Keys.CONTROL+Keys.ENTER)
        # else:
        #     posts.send_keys(Keys.CANCEL)

        # ptn = driver.find_element_by_link_text("Post")
        # ptn.click()

        time.sleep(3)
        driver.get_screenshot_as_file("afterpost.png")
        time.sleep(500)
    except Exception as e:
        print("login failed, e={}".format(e))
        return 'failed', str(e)
    finally:
        driver.quit()

    return 'succeed', 'success feed'


def post(driver, content='love and peace!'):
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(1)
    # editer = driver.find_element_by_class_name('_1mf _1mj')
    # editer = driver.find_elements_by_css_selector("[class='_1mf _1mj'")
    editer = driver.find_element_by_name('xhpc_message')
    if not editer:
        print("cant find editer")
    else:
        # editer.click()
        editer.send_keys(Keys.ENTER)
        time.sleep(6)

        res = EC.alert_is_present()(driver)
        if res:
            print(res.text)
            res.accept()
        else:
            print("no alert")

        post = driver.find_elements_by_css_selector("div ._1mf _1mj")
        # post = driver.find_elements_by_css_selector("[class='_1mwp navigationFocus _395 _1mwq _4c_p _5bu_ _3t-3 _34nd _21mu _5yk1'")
        # post = driver.find_element_by_class_name('_1mwp navigationFocus _395 _1mwq _4c_p _5bu_ _3t-3 _34nd _21mu _5yk1')
        if post:
            post.send_keys(content)
        else:
            print("cant find post ")
    time.sleep(10)


if __name__ == '__main__':
    # auto_feed(inputs={'account':"codynr4nzxh@outlook.com", 'password':"qVhgldHmgp"})
    # from pyvirtualdisplay import Display
    from selenium import webdriver

    # display = Display(visible=1, size=(1600, 902))
    # display.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.delete_all_cookies()
    driver.set_window_size(800, 800)
    driver.set_window_position(0, 0)
    print('arguments done')
    driver.get('http://stubhub.com')