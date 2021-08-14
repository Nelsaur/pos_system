from django.test import TestCase
from menu.models import Item

import menu.validatorsLogic as validator

validator.validate_order_id
class Test(TestCase):
    def test_modifier_valid(self):
        item = Item(
            description = "Apple",
            price = 4.00,
            quantity = 2,
            modifiers = {
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
        )
        item.full_clean()
        item.save()
        record = Item.objects.get(pk=1)
        self.assertEqual(record,item)

    def test_modifier_invalid_toppings(self): #wrong format
        item = Item(
            description = "Apple",
            price = 4.00,
            quantity = 2,
            modifiers = [
                {
                    'Burger': {
                        'Tomato' : "a", 
                        'Pickles': "b", 
                        'Mayo': "c"
                    }
                },
                {
                    'Bun Choice': [
                        'Sesame', 
                        'Whole Wheat', 
                        'Keto'
                    ]
                    
                }, 
            ],
        )
        self.assertRaises(Exception, item.full_clean)

    def test_modifier_invalid_modifier(self):   #wrong format
        item = Item(
            description = "Apple",
            price = 4.00,
            quantity = 2,
            modifiers = [
                [
                    'Burger',
                    'Bun Choice'
                ]
            ],
        )
        self.assertRaises(Exception, item.full_clean)

    