import requests
import json





def radr():

    i =0
    a =0
    list=[]
    for i in range(5):

        url = "https://s3.radarlab.org:5005/"

        payload = "{\n    \"method\": \"ledger\",\n    \"params\": [\n        {\n            \"ledger_index\":\"validated\"\n        }\n    ]\n}"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "8a4f77d2-77f8-62ba-449e-764b492303f2"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        # r=requests.post()

        dict_date=json.loads(response.text)
        height=dict_date['result']['ledger']['ledger_index']
        print(height)
        # list.append(height)
        # if i>=1:
        #     if list[i]<list[i-1]:
        #         a=a+1
        #         print('a='+a)
        # i = i+1

radr()