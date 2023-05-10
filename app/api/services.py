import requests
import time
url = "https://workout-planner1.p.rapidapi.com/"

querystring = {"time":"30","muscle":"biceps","location":"gym","equipment":"dumbbells"}

headers = {
	"X-RapidAPI-Key": "28dfc0e2a6mshfd18a7f7d3c3901p173983jsncd5d692debd5",
	"X-RapidAPI-Host": "workout-planner1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

def get_exercise(products):
    url= f'https://fakestoreapi.com/products/{products}'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        product = {
        'product_id' : data["id"],
        'product_name' : data["title"],
        'price' : data["price"],
        'description' : data["description"],
        'category': data["category"],
        'product_image' : data["image"]
        }
        return product
    else:
        return None

# print(get_products(1))