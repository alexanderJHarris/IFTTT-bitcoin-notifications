import requests
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
response = requests.get(bitcoin_api_url)
response_json = response.json()
type(response_json) #Return a list from the API

response_json[0]
print(response_json)