import json
from collections import Counter

with open ('data.json') as f:
    data=json.load(f)
a=[]
for item in data['events_data']:
	client=item['client_id']
	cat=item['category']
	if cat=='page':
		a.append(client)

list=Counter(a).keys()
print('Количество уникальных клиентов: ' + str(len(list)))

