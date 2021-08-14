import requests
import json

def order_create_invalid():
    URL = 'http://127.0.0.1:8000/order/create/'
    post_data = {
        'items':[
            {
                'id': 1,
                'quantity': 3,
                'modifiers': [
                    {
                        'Burger': [
                            'Tomato', 
                            'Mayo'
                        ]
                    },
                    {
                        'Bun Choice': [
                            'Sesame'
                        ]
                    }, 
                ],
            },
            {
                'id': 1,
                'quantity': 1,
                'modifiers': [
                        'Burger',
                        'Bun Choice',
                ],
            },
        ],
        'payment': 80,
        'note': "thanks"
    }
    return requests.post(URL, json=post_data)

#CREATE
def order_create1():
    URL = 'http://127.0.0.1:8000/order/create/'
    post_data = {
        'items':[
            {
                'id': 1,
                'quantity': 2,
                'modifiers': {
                    'Burger Toppings': [
                        'Tomato', 
                        'Pickles', 
                        'Mayo',
                    ],
                    'Bun Choice': [
                        'Sesame', 
                        'Whole Wheat',
                    ]
                    
                }, 
            },
        ],
        'payment': 20,
        'note': "thanks"
    }
    return requests.post(URL, json=post_data)
    
def order_create2():
    URL = 'http://127.0.0.1:8000/order/create/'
    post_data = {
        'items':[
            {
                'id': 1,
                'quantity': 2,
                'modifiers': {
                    'Burger Toppings': [
                        'Tomato', 
                        'Pickles', 
                        'Mayo',
                    ],
                    'Bun Choice': [
                        'Sesame', 
                        'Whole Wheat',
                    ]
                    
                }, 
            },
            {
                'id': 1,
                'quantity': 3,
                'modifiers': {
                    'Burger Toppings': [
                        'Tomato', 
                        'Pickles', 
                    ],
                    'Bun Choice': [
                        'Sesame', 
                        'Whole Wheat',
                    ]
                    
                }, 
            },
        ],
        'payment': 50,
        'note': "thanks"
    }
    return requests.post(URL, json=post_data)
       
def order_create3():
    URL = 'http://127.0.0.1:8000/order/create/'
    post_data = {
        'items':[
            {
                'id': 1,
                'quantity': 1,
                'modifiers': {
                    'Burger Toppings': [
                        'Tomato', 
                        'Pickles', 
                        'Mayo',
                    ],
                    'Bun Choice': [
                        'Sesame', 
                        'Whole Wheat',
                    ]
                    
                }, 
            },
            {
                'id': 2,
                'quantity': 1,
                'modifiers': {
                    'Pizza Toppings': [
                        'Pepperoni', 
                    ],
                    'Crust Choice': [
                        'Thin', 
                    ]
                    
                }, 
            },
        ],
        'payment': 30,
        'note': "thanks"
    }
    return requests.post(URL, json=post_data)

def order_list():
    URL = 'http://127.0.0.1:8000/order/'
    return requests.get(URL)

def order_get(id:str):
    URL = 'http://127.0.0.1:8000/order/' + id
    return requests.get(URL)

#response = order_list()
#response = order_get('1')
#response = order_create1()  #buy 2 burgers
#response = order_create2()  #buy 5 burgers
response = order_create3() #buy 1 burger, 1 pizza
#response = order_create_invalid()
print(response.content)
