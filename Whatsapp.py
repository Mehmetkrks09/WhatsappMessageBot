from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()

browser.get("https://web.whatsapp.com/")
print("Mehmet Karakaş Tarafından Yapılmıştır.\n \n ")
input("Merhaba Öncelikle Bir Sohbete girin ve Enter a basın")
m=1
#person=browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[10]/div/div/div/div[2]/div[1]/div[1]/span")
time.sleep(2)
print("Başlıyoruz")
#person.click()
#time.sleep(5)
#print("Bekleme Bitti")

#message_area=browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]")
while (m >0):
    print("Devam için 1 e basın")
    option= int(input("Seçiniz :"))
    if(option==1):
        message_area=browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]")
        Mesaj=input("Mesajınız : ")
        sayi = int(input("Sayi :"))
        message_area.click()
        for j in range(0,sayi):
            for i in Mesaj:
                message_area.send_keys(i)
            message_area.send_keys(Keys.ENTER)
    else:
        print("Çıkılıyor..")
        time.sleep(5)
        browser.close
        break
          
  





















