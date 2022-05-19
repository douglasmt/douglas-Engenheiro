import requests
url = "https://icanhazdadjoke.com/" # the url to call

print("\n --- REPONSE DATA (Accept application/json )---\n")
response = requests.get(url, headers={"Accept": "application/json"})
print(response)
'''
print("\n --- REPONSE DATA (Accept text/plain )---\n")
response = requests.get(url, headers={"Accept": "text/plain"})
# give me the plain text
'''
print("\n --- REPONSE DATA (response.json() )---\n")
data = response.json()
print(data)

print("\n --- REPONSE DATA (joke )---\n")
print(data["joke"])
print(f"status: {data['status']}")



