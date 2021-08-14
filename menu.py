import requests
import json



#CREATE
def menu_create_default():
    URL = 'http://127.0.0.1:8000/menu/create/'
    post_data = {
        'description': 'Hamburger', 
        'price':10, 
        'quantity': 100,
        'modifiers': {
            'Burger Toppings': [
                'Tomato', 
                'Pickles', 
                'Mayo'
            ],
            'Bun Choice': [
                'Sesame', 
                'Whole Wheat', 
                'Keto'
            ]
            
        }, 
    }
    print(requests.post(URL, json=post_data).content)

    URL = 'http://127.0.0.1:8000/menu/create/'
    post_data = {
        'description': 'Pizza', 
        'price':20, 
        'quantity': 40,
        'modifiers': {
            'Pizza Toppings': [
                'Pepperoni', 
                'Green Pepper', 
                'Mushrooms'
            ],
            'Crust Choice': [
                'Thin', 
                'Thick', 
                'Oven-tossed'
            ]
            
        }, 
    }
    print(requests.post(URL, json=post_data).content)
   
def menu_update():
    URL = 'http://127.0.0.1:8000/menu/update/1/'
    post_data = {
        'description': 'Hamburger', 
        'price':10, 
        'quantity': 100,
        'modifiers': {
            'Burger Toppings': [
                'Tomato', 
                'Pickles', 
                'Mayo',
                'BBQ Sauce'
            ],
            'Bun Choice': [
                'Sesame', 
                'Whole Wheat', 
                'Keto'
            ]
        }, 
    }
    return requests.put(url=URL, json=post_data)

def menu_delete(id):
    URL = f'http://127.0.0.1:8000/menu/delete/{id}/'
    return requests.delete(URL)

def menu_list():
    URL = 'http://127.0.0.1:8000/menu/'
    return requests.get(URL)

def menu_get(id:str):
    URL = 'http://127.0.0.1:8000/menu/' + id
    return requests.get(URL)



menu_create_default()  #add 100 burgers, 40 pizzas

#response = menu_get("1")
#response = menu_list()
#response = menu_delete(2)
#response = menu_update()
#print(response.content)
