import requests 
import time
from datetime import datetime

BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
#IFTTT_WEBHOOKS_URL = <Add your IFTTT Webhook URL here>
BITCOIN_PRICE_THRESHOLD = 4500 #Warn user if price rises or falls below this threshold current high as of April 4th, 2019

def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()

    return float(response_json[0]['price_usd'])

def post_ifttt_webhook(event, value):
    data1 = {'value1': value}
    #Add other values here for the output in notifications. Each 'value' corresponds to an IFTTT JSON payload
   
    # Uncomment the following lines when you add your personal IFTTT webhook URL above 
    # ifttt_event_url= IFTTT_WEBHOOKS_URL.format(event)
    # requests.post(ifttt_event_url, json=data1)

def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        if (price < BITCOIN_PRICE_THRESHOLD):
            post_ifttt_webhook('bitcoin_price_emergency', price)

        if len(bitcoin_history) == 5:
            post_ifttt_webhook('bitcoin_price_update', bitcoin_history)
        bitcoin_history = []

    time.sleep(30 * 60) #sleep every 30 minutes to be less annoying. Adjust if necessary

if __name__ == '__main__':
    main()
