import requests
import json

url = 'https://api.random.org/json-rpc/2/invoke'

data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": "ba113d12-ab6a-4504-876b-176bb0ac879d",
        "n": '6',
        "min": '1',
        "max": '6',
    },
    "id": '42'
}

response = requests.post(url=url, data=json.dumps(data)).status_code
print(response)