import requests 

base_url = "https://api.spacexdata.com"

def get_spacex_facts(): 
    url = f"{base_url}/v5/launches/latest"
    response = requests.get(url)
    data = response.json()
    return data 

spacex_data = get_spacex_facts()

for key, value in spacex_data.items(): 
    print(key)

print(spacex_data["rocket"]) #5e9d0d95eda69973a809d1ec refers to "Falcon 9"