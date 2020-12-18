# setup=[{"server":"  YIMO master yi mains","channel":"channels-581649043743178783"},
#

""" setup= [{"server":"  YIMO master yi mains","channel":"meditation-chat (text channel)"}, {"server":"  🆂🆀🆄🅸🆁🆁🅴🅻🐿","channel":"𝑏𝑒-𝑢𝑟𝑠𝑒𝑙𝑓🧡 (text channel)"},
        {"server":"  🆂🆀🆄🅸🆁🆁🅴🅻🐿", "channel": "𝔀𝓮𝓮𝓫🍣 (text channel)"}, {"server":"  🆂🆀🆄🅸🆁🆁🅴🅻🐿", "channel": "🅒🅞🅜🅟🅤🅛🅢🅘🅥🅔🎰 (text channel)"},
        {"server":"  🆂🆀🆄🅸🆁🆁🅴🅻🐿", "channel": "🔞𝑚𝑒𝑚𝑒s-𝑒𝑟𝑜𝑠😳 (text channel)"}] #u can spam at multiple servers by expanding this list """

setup = ["'Taverna di League of Legends ☢️'", "'⚜️ 𝑶𝒍𝒊𝒎𝒑𝒊𝒂 𝑮𝒓𝒐𝒖𝒑 ⚜️'", "'SCOPAZZI'",
         "'League of Legends Italia - WeMug.it'"]

list_file_text = ["cazzate.txt", "computers.txt", "frasi.txt", "poesiecanzoni.txt"]

import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import time
import random


# def meditation_channel(channel_id):
#     try:
#         message = ":Meditate:"
#         channel_element = driver.find_element_by_xpath("//a[@aria-label='"+channel_id+"']") #this does not work when used on the RL Insider server
#         driver.execute_script("arguments[0].click();", channel_element)
#         #input("prompt")
#         text_element = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
#         text_element.click()
#         #text_element.clear()
#         for c in message:
#             text_element.send_keys(c)
#         text_element.send_keys(Keys.ENTER)
#         time.sleep(random.randint(1,1000))
#         #input("prompt")
#     except selenium.common.exceptions.NoSuchElementException:
#         print("not found by id xpath")

# def squirrel_channel(channel_id):
#     try:
#         owo_actions = ["hug", "cuddle", "insult" "kiss" "lick" "nom" "pat" "poke" "slap" "stare"
#                        "highfive" "bite" "greet" "punch" "handholding" "tickle" "kill" "hold" "pats" "wave" "boop"]
#         users_list = ["@cocco minorenne", "@Niniel#2909 ", "@PVC#2909 ", "@giuseppe#2593 ", "@SanCrispian#8948 ",
#                        "@Memmolo#7578 ", "@Dalton#7440 ", "@glioneCO#8561 ", "@Muccino#1040 ", "@Gigliola#6686 ",
#                        "@tsunasawada#0022 ", "@,,iLL#1617 ", "@Mnemosyne#9142", "@elix#9735"]
#         message = "owo" + " " + random.choice(owo_actions) + " " + random.choice(users_list)
#         #message = random.choice(list_message)
#         channel_element = driver.find_element_by_xpath("//a[@aria-label='"+channel_id+"']") #this does not work when used on the RL Insider server
#         driver.execute_script("arguments[0].click();", channel_element)
#         #input("prompt")
#         text_element = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
#         text_element.click()
#         #text_element.clear()

#         for c in message:
#             text_element.send_keys(c)
#         text_element.send_keys(Keys.ENTER)
#         time.sleep(random.randint(1,1000))

#     except selenium.common.exceptions.NoSuchElementException:
#         print("not found by id xpath")

# def weeb_channel(channel_id):
#     try:
#         listMessage = ["!sg", "!sg 1", "!sg 2", "!sg 3", "!sg 4", "!sg 5", "!sga op"]
#         message = random.choice(listMessage)
#         channel_element = driver.find_element_by_xpath("//a[@aria-label='"+channel_id+"']") #this does not work when used on the RL Insider server
#         driver.execute_script("arguments[0].click();", channel_element)
#         #input("prompt")
#         text_element = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
#         text_element.click()
#         #text_element.clear()

#         for c in message:
#             text_element.send_keys(c)
#         text_element.send_keys(Keys.ENTER)
#         time.sleep(random.randint(1,1000))

#     except selenium.common.exceptions.NoSuchElementException:
#         print("not found by id xpath")

# def compulsive_channel(channel_id):
#     try:
#         listMessage = ["owo owo", "owo daily", "+vote", "+daily", "+work", "+cooldowns"]
#         message = random.choice(listMessage)
#         channel_element = driver.find_element_by_xpath("//a[@aria-label='"+channel_id+"']") #this does not work when used on the RL Insider server
#         driver.execute_script("arguments[0].click();", channel_element)
#         #input("prompt")
#         text_element = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
#         text_element.click()
#         #text_element.clear()

#         for c in message:
#             text_element.send_keys(c)
#         text_element.send_keys(Keys.ENTER)
#         time.sleep(random.randint(1,1000))

#     except selenium.common.exceptions.NoSuchElementException:
# print("not found by id xpath")

# def eros_channel(channel_id):
#     try:
#         listMessage = ["!sg harem", "!sg ecchi", "!sg yaoi", "!sg yuri", "!sg 5"
#                        "!sga"]
#         message = random.choice(listMessage)
#         channel_element = driver.find_element_by_xpath("//a[@aria-label='"+channel_id+"']") #this does not work when used on the RL Insider server
#         driver.execute_script("arguments[0].click();", channel_element)
#         confirm_NSFW_channel_element = driver.find_element_by_xpath("//button[@class='action-yrVND8 button-38aScr lookFilled-1Gx00P actionRed-gYn8D3 sizeLarge-1vSeWK grow-q77ONN']")
#         confirm_NSFW_channel_element.click()
#         #confirm_NSFW_channel_element.clear()
#         #input("prompt")
#         text_element = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
#         text_element.click()
#         #text_element.clear()

#         for c in message:
#             text_element.send_keys(c)
#         text_element.send_keys(Keys.ENTER)
#         time.sleep(random.randint(1,1000))

#     except selenium.common.exceptions.NoSuchElementException:
#         print("not found by id xpath")

# def six():
#     return "June"

# def seven():
#     return "July"

# def eight():
#     return "August"

# def nine():
#     return "September"

# def ten():
#     return "October"

# def eleven():
#     return "November"

# def twelve():
#     return "December"


# def case_channels(argument):
#     switcher = {
#         "meditation-chat (text channel)": meditation_channel,
#         "𝑏𝑒-𝑢𝑟𝑠𝑒𝑙𝑓🧡 (text channel)": squirrel_channel,
#         "𝔀𝓮𝓮𝓫🍣 (text channel)": weeb_channel,
#         "🅒🅞🅜🅟🅤🅛🅢🅘🅥🅔🎰 (text channel)": compulsive_channel,
#         "🔞𝑚𝑒𝑚𝑒s-𝑒𝑟𝑜𝑠😳 (text channel)": eros_channel,
#         6: six,
#         7: seven,
#         8: eight,
#         9: nine,
#         10: ten,
#         11: eleven,
#         12: twelve
#     }
#     # Get the function from switcher dictionary
#     func = switcher.get(argument, lambda: "Unable to find channel")
#     # Execute the function
#     func(argument)

def send_message_to_channel(channel_id):
    try:
        # list_message = ["!sg", "!sg 1", "!sg 2", "!sg 3", "!sg 4", "!sg 5", "!sga op"]
        file_text = random.choice(list_file_text)
        text = open(file_text).readlines()
        random.shuffle(text)
        open(file_text, 'w').writelines(text)
        # channel_element = driver.find_element_by_xpath("//textarea[@class='form-control im_message_field no_outline ng-untouched ng-valid ng-empty ng-dirty ng-valid-parse']") #this does not work when used on the RL Insider server
        # driver.execute_script("arguments[0].click();", channel_element)
        # input("prompt")
        wait = WebDriverWait(driver, 10)
        # //span[contains(text(),'Taverna di League of Legends ☢️')]
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@placeholder='Scrivi un messaggio...']")))
        text_element = driver.find_element_by_xpath("//div[@placeholder='Scrivi un messaggio...']")
        text_element.click()
        # text_element.clear()

        # t_end = time.time() + 60 *
        # while time.time() < t_end:
        message = random.choice(text)
        for c in message:
            text_element.send_keys(c)
            # time.sleep(120)
            print("Message " + message + " sent in the channel " + channel_id)
            # time.sleep(5)
        text_element.send_keys(Keys.ENTER)
        time.sleep(random.randint(1, 100))

    except selenium.common.exceptions.NoSuchElementException:
        print("not found by id xpath")


def taverna_channel(channel_id):
    send_message_to_channel(channel_id)


def olimpia_channel(channel_id):
    send_message_to_channel(channel_id)


def scopazzi_channel(channel_id):
    send_message_to_channel(channel_id)


def lolgroupitalia_channel(channel_id):
    send_message_to_channel(channel_id)


# password = getpass("Enter your discord password: ") #enter there your password

def login(number):
    number_element = driver.find_element_by_xpath("//input[@name='phone_number']")
    number_element.click()
    # number_element.clear()
    for c in number:
        number_element.send_keys(c)
    next_element = driver.find_element_by_xpath("//my-i18n[@msgid='modal_next']").click()
    # next_element.click()
    # next_element.clear()
    driver.find_element_by_xpath("//span[@my-i18n='modal_ok']").click()

    number_code = input("Insert telegram code here")

    code_element = driver.find_element_by_xpath("//input[@name='phone_code']")
    code_element.click()
    # code_element.clear()
    for c in number_code:
        code_element.send_keys(c)

    # next_element = driver.find_element_by_xpath("//my-i18n[@msgid='modal_next']").click()
    # next_element.click()
    # next_element.clear()
    # driver.find_element_by_xpath("//span[@my-i18n='modal_ok']").click()


driver = webdriver.Chrome(ChromeDriverManager().install())
number = input("Enter your phone number: ")
# driver.get("https://discord.com/channels/@me")
driver.get("https://web.telegram.org/#/im?p=@TavernaLoLGroup")

# login
print(driver.title)
# login(email, password)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='phone_number']")))
login(number)
time.sleep(5)  # wait discord page to get loaded


# string = input("input anything when logged in")  #uncomment this if you want custom message


def case_channels(argument):
    switcher = {
        "'Taverna di League of Legends ☢️'": taverna_channel,
        "'⚜️ 𝑶𝒍𝒊𝒎𝒑𝒊𝒂 𝑮𝒓𝒐𝒖𝒑 ⚜️'": olimpia_channel,
        "'SCOPAZZI'": scopazzi_channel,
        "'League of Legends Italia - WeMug.it'": lolgroupitalia_channel
        # "🔞𝑚𝑒𝑚𝑒s-𝑒𝑟𝑜𝑠😳 (text channel)": eros_channel,
        # 6: six,
        # 7: seven,
        # 8: eight,
        # 9: nine,
        # 10: ten,
        # 11: eleven,
        # 12: twelve
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Unable to find channel")
    # Execute the function
    func(argument)


def go_to_channel(server):
    # //span[@my-peer-link='dialogMessage.peerID'][contains(text(),'Taverna di League of Legends ☢️')]
    # //span[contains(text(),'Taverna di League of Legends ☢️')]
    wait = WebDriverWait(driver, 10)
    # //span[contains(text(),'Taverna di League of Legends ☢️')]
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text()," + server + ")]")))
    server_element = driver.find_element_by_xpath("//span[contains(text()," + server + ")]")
    server_element.click()
    # driver.execute_script("arguments[0].click();", server_element)
    # input("prompt")
    print(driver.current_url)
    case_channels(server)
    # case_channels(channel_id)


while True:
    length = len(setup)
    for i in range(length):
        go_to_channel(setup[i])
        # a = 0

driver.close()


