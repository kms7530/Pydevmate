#-*- coding: utf-8 -*-
import requests, json, sys

custommer_id = sys.argv[1]
item_id = sys.argv[2]

# 라이센스 구입
url = "https://public-api.devmate.com/v2/customers/{0}/licenses".format(custommer_id)
api_key = {'Authorization': 'Token c98bf7b164323f4cb535d88384511e5d39532c64427c4bf2fef73f4f7fee702d'}
datas = {'data' : {'license_type_id' : item_id}}

r = requests.post(url, data = json.dumps(datas), headers = api_key)
json_content = r.json()

print json_content['data']['activation_key']