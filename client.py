import requests

url = "http://65.0.200.84/tikz"

with open("sample-tex", 'r') as f:
    payload = f.read()

headers = {
    'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data = payload)

with open('sample.png', 'wb') as f:
    f.write(response.content)
