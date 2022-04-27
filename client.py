import requests
data ="""{"name":"Shoukat","country":"India"}"""
url = "http://127.0.0.1:5000/invokeEngine"
response = requests.post(url,json={"run_id":300,"name":"Shoukat","country":"India"})
print(response)
response = requests.post(url,json={"run_id":400,"name":"Shoukat","country":"India"})
print(response)
response = requests.post(url,json={"run_id":500,"name":"Shoukat","country":"India"})
print(response)