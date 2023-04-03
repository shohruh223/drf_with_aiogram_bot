import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api/v1'


def product_list():
    url = f"{BASE_URL}/product"
    data = requests.get(url=url).text
    result = json.loads(data)
    return result

# print(product_list())


def create_product(title, photo, description, price):
    url = f"{BASE_URL}/product"
    data = requests.post(url=url, data={"title":title,
                                        "photo":photo,
                                        "description":description,
                                        "price":price})
    return "malumot saqlandi"

