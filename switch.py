import getpass
import pyautogui, time, pyperclip, random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
import time
def display_banner():
    banner_text = r'''
      ___ _ __   __ _ _ __ ___   
 / __| '_ \ / _` | '_ ` _ \  
 \__ \ |_) | (_| | | | | | | 
 |___/ .__/ \__,_|_| |_| |_| 
     | |                     
     |_|                                          
                                                                    
    Tool spam 1.0
    Coded by Nguyen Phuoc Thanh
    Duy Tan University 
    thanhnguyenphuoc97@gmail.com

    '''
    print(banner_text)
def spam():
    msg = input("nhập nội dung cần spam: ").split(" || ")
    n = int(input("Nhập số lần spam : "))
    m =  float(input("Nhập time delay: "))
    print("chuẩn bị")
    for i in range(5,0,-1):
        print(i, end="..",flush="True")
    print("Bắt đầu")
    for i in range (n):
        pyperclip.copy(random.choice(msg))
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        time.sleep(m)
def login():
    usernamefacebook = input("nhập tài khoản facebook: ")
    passwordfacebook = getpass.getpass("nhập mật khẩu facebook: ")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://www.facebook.com/")
    browser.find_element_by_id("email").send_keys(usernamefacebook)
    browser.find_element_by_id("pass").send_keys(passwordfacebook)
    browser.find_element_by_id('u_0_b').click()
def main():
    username = input("nhap username: ")
    password = getpass.getpass("nhap password: ")
    print("")
    if username=="thanh" and password=="123":
        while True:
            print("1.spam")
            print("2.login facebook")
            print("3.exit \n")
            choice = input("Lựa chọn chức nào sau đây: ")
            if  choice =="1": 
                spam()
            elif choice =="2":
                login()
            elif choice =="3":
                print(exit)
                break
    else:
        print("Đăng nhập sai")
if __name__ == "__main__":
        display_banner()
        main()

