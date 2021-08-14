from django.test import TestCase
from menu.models import Item
import menu.validatorsLogic as validator

class TestMenu(TestCase):
    def test_valid_fields(self):
        item = Item(
            description = "Apple",
            price = 4.00,
            quantity = 32,
            modifiers={
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

    def test_failed_price(self):
        item = Item(
            description = "Apple",
            quantity = 32,
            price = -4.00,
        )
        self.assertRaises(Exception, item.full_clean)

    def test_failed_price2(self):
        item = Item(
            description = "Apple",
            quantity = 32,
            price = 0,
        )
        self.assertRaises(Exception, item.full_clean)

    def test_failed_price3(self):
        item = Item(
            description = "Apple",
            quantity = 32,
            price = 'invalid',
        )
        self.assertRaises(Exception, item.full_clean)
                
    def test_failed_qty(self):
        item = Item(
            description = "Apple",
            price = 4.00,
            quantity = -32,
        )
        self.assertRaises(Exception, item.full_clean)
        
    def test_failed_qty2(self):
        item = Item(
            description = "Apple",
            price = 4.00,
            quantity = "invalid",
        )
        self.assertRaises(Exception, item.full_clean)

    
    def test_empty_description(self):
        item = Item(
            description = "",
            price = 4.00,
            quantity = 1,
        )
        self.assertRaises(Exception, item.full_clean)
