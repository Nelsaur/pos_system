from django.db import models
from menu.validators import validate_price, validate_quantity, validate_modifiers, validate_order_items


class Item(models.Model):
    id = models.AutoField(primary_key=True)

    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[validate_price])
    quantity = models.IntegerField(default = 0, validators=[validate_quantity])
    modifiers = models.JSONField(default=dict, blank=True, validators = [validate_modifiers])

    def __str__(self):
        return f"{self.description} - ${self.price} qty:{self.quantity}"

    def quantity_by_id(menu_object, id):
        menu_item = menu_object.objects.get(pk=id)
        return menu_item.quantity
    def description_by_id(menu_object, id):
        menu_item = menu_object.objects.get(pk=id)
        return menu_item.description
    def price_by_id(menu_object, id):
        menu_item = menu_object.objects.get(pk=id)
        return menu_item.price
    
    def find_modifier_in_menu_item(modifier_name, menu_item):
        ''' returns dictionary if found, or false otherwise'''
        modifier_dict = menu_item.modifiers
        for modifier_key in modifier_dict:
            print("compare: " +modifier_key +"->"+modifier_name)
            if modifier_key == modifier_name:
                print ("Found Modifier" + str(type((modifier_dict[modifier_key]))))
                return modifier_dict[modifier_key]
        return False

    def find_topping_in_modifier(topping_name, modifier):
        for topping in modifier:
            print("topping: " +topping +"->"+topping_name)
            if topping == topping_name: return True
        return False
    
    def update_quantity(required_quantity, menu):
        for item_key in required_quantity:
            menu_item = Item.objects.get(pk=item_key)
            current_quantity = menu_item.quantity
            new_quantity = int(current_quantity) - int(required_quantity[item_key])
            menu_item.quantity = new_quantity
            Item.save(menu_item)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.JSONField(default=list, blank=True, validators=[validate_order_items])
    payment = models.DecimalField(max_digits=6, decimal_places=2, validators=[validate_price])
    note = models.TextField(default='')

    @staticmethod
    def append_description_price(menu_object, order_list):
        for item in order_list:  #item in the order
            menu_item = menu_object.objects.get(pk=item['id'])
            
            item['description'] = menu_item.description
            item['price'] = float(str(menu_item.price))
        return True

    @staticmethod
    def bill_total(order_list):
        total = 0.0
        for item in order_list:  #item in the order
            #for i in range(item['quantity']):
            total += item['quantity'] * item['price']
        return total
