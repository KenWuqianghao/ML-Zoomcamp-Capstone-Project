import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
image = 'https://media.wired.com/photos/5e8cebbda231050008136013/master/pass/animal-crossing-history-wired.jpg'
data = {'url':image}
result = requests.post(url, json=data).json()

print(result)