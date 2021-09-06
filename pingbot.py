import os
import requests
import time
import sys

def telegram_bot_sendtext(bot_message):
    bot_token = os.getenv('BOT_TOKEN') #'1983495325:AAH8McX0qWHbrLHmcMVlowInKX-tt8v3JAY'
    bot_chatID = os.getenv('BOT_ID') #'1282108405'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

if __name__=="__main__":
    last_response = None

    try:
        while True:
            hostname = sys.argv[1]
            response = os.system("ping -c 1 " + hostname)
            if response != last_response or not last_response:
                last_response = response
                test = telegram_bot_sendtext(hostname + ' is up!' if response == 0 else hostname + ' is down!')
                print("sends via telegram ", hostname + ' is up!' if response == 0 else hostname + ' is down!')
            time.sleep(30)
    except KeyboardInterrupt:
        pass