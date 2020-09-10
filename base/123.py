import http.client

conn = http.client.HTTPSConnection("s3.radarlab.org:5005")

payload = "{\n    \"method\": \"ledger\",\n    \"params\": [\n        {\n            \"ledger_index\":\"validated\"\n        }\n    ]\n}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "78bbeac2-1b96-1b89-6794-6cfcc13877fc"
    }

conn.request("POST", "/", payload, headers,verify=False)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))