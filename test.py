import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url':'https://user-images.githubusercontent.com/20444505/144915447-cfaae0f4-ca78-4828-b20b-eae04b093d2c.png'}

result = requests.post(url, json=data).json()
print(result)