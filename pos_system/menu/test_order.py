from django.test import TestCase
from menu.models import Item, Order
import menu.validatorsLogic as validator

class TestOrder(TestCase):
    def test_valid_order(self):
        item = Item(
            description = "Hamburger",
            price = 4.00,
            quantity = 4,
            modifiers = {
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
        )
        item.full_clean()
        item.save()

        order = Order(
            items = [
                {
                    'id': 1,
                    'quantity': 3,
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
            payment = 12,
            note = 'hello world!'
        )
        order.full_clean()
        order.save()

        record = Order.objects.get(pk=1)
        self.assertEqual(record,order)

    def test_valid_reduced_quantity_from_sale(self):
        item = Item(
            description = "Hamburger",
            price = 4.00,
            quantity = 4,
            modifiers = {
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
        )
        item.full_clean()
        item.save()

        order = Order(
            items = [
                {
                    'id': 1,
                    'quantity': 3,
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
            payment = 12,
            note = 'hello world!'
        )
        order.full_clean()
        order.save()

        self.assertEquals(Item.objects.get(pk=1).quantity, 4) #inventory before the sale
        reduce_quantity = {1: 3}
        valid_quantity_status = validator.validate_quantity_logic(Item, order.items)
        self.assertEquals(valid_quantity_status, reduce_quantity)
        Item.update_quantity(reduce_quantity, Item)
        self.assertEquals(Item.objects.get(pk=1).quantity, 1) #inventory after the sale


    def test_out_of_stock(self):
        item = Item(
            description = "Hamburger",
            price = 4.00,
            quantity = 4,
            modifiers = {
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
        )
        item.full_clean()
        item.save()

        order = Order(
            items = [
                {
                    'id': 1,
                    'quantity': 8,
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
            payment = 12,
            note = 'hello world!'
        )
        order.full_clean()
        order.save()

        reduce_quantity = {1: 8}
        self.assertRaises(Exception, validator.validate_quantity_logic(Item, order.items)) #error when inventory is less than order


    def test_total_bill(self):
        item = Item(
            description = "Cheeseburger",
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

        order = Order(
            items = [
                {
                    'id': 1,
                    'quantity': 3,
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
            payment = 60,
            note = 'hello world!'
        )
        Order.append_description_price(Item,order.items)
        self.assertEqual(Order.bill_total(order.items),12)  # expected total bill amount


