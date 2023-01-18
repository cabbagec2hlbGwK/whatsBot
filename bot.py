# Import the Selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
# //*[@id="pane-side"]/div[2]/div/div/div[1]
# //*[@id="pane-side"]/div[2]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span
# //*[@id="pane-side"]/div[1]/div/div/div[4]
# *//*[@id="pane-side"]/div[1]/div/div/div[4]
# *//*[@id="pane-side"]/div[1]/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/span
# *//*[@id="pane-side"]/div[1]/div/div/div[1]
# *//*[@id="pane-side"]/div[1]/div/div/div[8]/div/div/div/div[2]/div[1]/div[1]/span
# *//*[@id="pane-side"]/div[1]/div/div/div[14]0
# *//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button
# *//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div


class wBot:
    try:
        def __del__(self):
            self.driver.quit()

        def __init__(self) -> None:
            self. whatsapp_url = "https://web.whatsapp.com/"
            self.driver = webdriver.Chrome()
            self.contact = []
            self.driver.get(self.whatsapp_url)
            input("Press Enter after you have scanned the QR code and logged in...")

        def searchContact(self, name):
            search = self.driver.find_element(
                By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
            search.clear()
            search.send_keys(name)
            time.sleep(3)

        def selectContact(self, name):
            self.searchContact(name)
            count = 0
            div_object = None
            while True:
                count = count + 1
                print(count)
                try:
                    result = self.driver.find_element(
                        By.XPATH, f'//*[@id="pane-side"]/div[1]/div/div/div[{count}]/div/div/div/div[2]/div[1]/div[1]/span')
                    print(result.text)
                    print(result.text in name)
                    if name in result.text:
                        div_object = self.driver.find_element(
                            By.XPATH, f'//*[@id="pane-side"]/div[1]/div/div/div[{count}]')
                        break
                except Exception as e:
                    print(e.args)
                    continue
            if div_object == None:
                return False
            print(div_object.text)
            div_object.click()
            time.sleep(1)
            return True

        def getChat(self, name):
            if not self.selectContact(name):
                return 1
            textBox = self.driver.find_element(
                By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
            return textBox

        def addContact(self, detail):
            if self.getChat(detail) == 1:
                print("The contact was not found")
                input("breakpoint")
                return
            self.contact.append(detail)

        def sendMessage(self, name, message):
            try:
                if name not in self.contact:
                    print("This user is not in the list, Pleace add them before using")
                else:
                    chat = self.getChat(name)
                    print(chat)
                    print("sdffffffffffffffffffffffff")
                    if chat == 1:
                        print("Some thing went wrong, the user was not found")
                        return 1
                    chat.send_keys(message)
                    sendButton = self.driver.find_element(
                        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
                    # sendButton = self.driver.find_Element(
                    # By.XPATH, "//button[@aria-label='Send']")
                    sendButton.click()
            except Exception as e:
                print(e)
                os._exit(0)

        def getCotacts(self):
            return self.contact

        def checkContact(self, name):
            return name in self.contact

    # in case something goes bad
    except Exception as e:
        print(" the bot creshed ):")
        print(e.args)
        os._exit(1000)


bot = wBot()
name = "Deji"
bot.addContact(name)
print(bot.getCotacts())
for a in range(100):
    time.sleep(1)
    bot.sendMessage(name, "Message is test")
input(breakpoint)
