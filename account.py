#-*- coding: utf-8 -*-
import requests, json, sys

api_key = {'Authorization': 'Token lala'}

# 인자값 없을시
if len(sys.argv) == 1 :
	r = requests.get('https://public-api.devmate.com/v2/customers/', 
		headers = api_key)
	json_content = r.json()

	print str(json_content)
	exit()

first_name = sys.argv[1]
last_name = sys.argv[2]
email = sys.argv[3]

url = 'https://public-api.devmate.com/v2/customers/?filter[first_name]={0}&filter[last_name]={1}&filter[email]={2}'.format(first_name, last_name, email)

r = requests.get(url, headers = api_key)
json_content = r.json()

total = json_content['meta']['total']

if str(total) == '1' :
	# 성공
	print str(json_content['data'][-1]['id'])
	pass

elif str(total) == '0' :
	# 개정 생성
	datas = {'data' : {'email' : email, 'first_name' : first_name, 'last_name' : last_name, 'note' : ''}}

	r = requests.post('https://public-api.devmate.com/v2/customers/', 
		data =json.dumps(datas),
		headers = api_key)
	json_content = r.json()

	print json_content['data']['id']
	pass
else :
	print '-2419'