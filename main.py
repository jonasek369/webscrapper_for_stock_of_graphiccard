
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from time import strftime



#your PATH for webdriver
PATH = ""

#the url of the product for me its the 3070
url = "https://www.czc.cz/asus-geforce-rog-strix-rtx3070-o8g-gaming-8gb-gddr6/297936/produkt"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
def request():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find(class_="preorder-label").get_text()
    if price != "Neznámá cena":
        wb = webdriver.Chrome(PATH)
        wb.get("https://login.szn.cz/")
        login = wb.find_element_by_id("login-username").send_keys("your email")
        password = wb.find_element_by_id("login-password").send_keys("password")
        submit = wb.find_element_by_xpath("/html/body/div[1]/section[1]/div/form[1]/button").click()
        time.sleep(2)
        send_email = wb.find_element_by_xpath("/html/body/div/nav/div/div/a[2]").click()
        whOMEGALUL=wb.find_element_by_xpath("/html/body/section/div[2]/dl/div[2]/dd/div/input").send_keys("websrapperemail@email.cz")
        predmet = wb.find_element_by_xpath("/html/body/section/div[2]/dl/div[5]/dd/input").send_keys("3070 is now on stock :) buy it ffs")
        thetime = time.strftime("%c")
        predmet_more = wb.find_element_by_xpath("/html/body/section/div[2]/div[2]/div[1]/div[1]").send_keys(f"mhhhh yes its on stock on czc :) send on {thetime} "
                                                                                                            " https://www.czc.cz/asus-geforce-rog-strix-rtx3070-o8g-gaming-8gb-gddr6/297936/produkt")

        send_it = wb.find_element_by_xpath("/html/body/section/div[3]/button[1]").click()
    else:
        time.sleep(3600)
request()
