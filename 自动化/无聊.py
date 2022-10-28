import requests
import json

url='https://saying.api.azwcl.com/saying/get'

response=requests.get(url)
data=response.content.decode('utf8')
#print(data)
#print(type(data))
data=json.loads(data)
#print(data)
#print(type(data))
print('作者：',data['data']['author'])
print('内容：',data['data']['content'])