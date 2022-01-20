# Import statements
import requests 
from bs4 import BeautifulSoup 
import time 
import smtplib
from datetime import datetime

# Simple and easy script. Requests a web page with dedicated header input, gets the whole page and search specific word.
# If the specified word does not exists; It sends a message to a specific Telegram Bot to inform users.

# Don't forget to update bot_token, bot_chatID, url and aaabbb values.
    
def telegram_bot_sendtext(bot_message):
    bot_token = 'xxx:yyy'
    bot_chatID = 'zzz'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    print(response)
    return response.json()
  
# while this is true continue running, 
while True: 
    # Specify a url
    url = "https://www.google.com/" 
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 
    
    # download the web page, If an error occurs, message it via Telegram Bot
    try:
        response = requests.get(url, headers=headers)
    except e:
        telegram_bot_sendtext(e)
        
    # parse the web page 
    soup = BeautifulSoup(response.text, "lxml") 
    
    # if the number of times the specified word "aaabbb" occurs on the page is less than 1,
    if str(soup).find("aaabbb") == -1:
        telegram_bot_sendtext("Change Detected!")
        
        # wait 60 seconds, 
        time.sleep(60) 
        continue 
         
    # but if the word "aaabbb" occurs any other number of times print with formatted current time, 
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("No change detected",current_time)
        time.sleep(30)
