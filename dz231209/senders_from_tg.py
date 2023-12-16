import requests
import time

TOKEN = '5835620638:AAGhnoz9i5tSekQKMq9ztk50zHAgbmRBD2U'
CHANNEL_NAME = 'Жизнь чмоней'
f = open('for_usernames.txt','w')

def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)
    # print(response.json())
    return response.json()

def extract_promocode(message):
    # здесь вы можете реализовать извлечение промокода из текста сообщения
    return message

k = 0
for i in range(15):
    updates = get_updates()['result']
    if k!=updates:
        k = updates
        if updates:
            #print(updates[-1])
            last_message = updates[-1]['channel_post']
            #print(last_message)

            if last_message['sender_chat']['title'] == CHANNEL_NAME:
                print(last_message)
                promocode = extract_promocode(last_message['author_signature'])
                f.write(promocode)
                print(promocode)
    time.sleep(2)
f.close()

