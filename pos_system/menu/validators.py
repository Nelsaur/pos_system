from django.core.exceptions import ValidationError

def validate_price(value):
    if value <= 0:
        raise ValidationError("Price must be greater than $0")
    return value

    
def validate_quantity(value):
    if value < 0:
        raise ValidationError("Quantity must be greater than 0")
    return value

def validate_modifiers(value):
    if type(value) != dict: raise ValidationError("Invalid modifier JSON format - dict of modifier names")
    for modifier in value:
        if type(modifier) != str: raise ValidationError("Invalid modifier JSON format - string names of modifier")
        if type(value[modifier]) != list: raise ValidationError("Invalid modifier JSON format - list of toppings")
        for topping in value[modifier]:
            if type(topping) != str: raise ValidationError("Invalid modifier JSON format - toppings aren't strings")
    return True

def validate_order_items(item_list):
    if type(item_list) != list: raise ValidationError("Invalid modifier JSON format - list of items")
    for item_dict in item_list:
        if type(item_dict) != dict: raise ValidationError("Invalid modifier JSON format - dict of items")
        if not 'id' in item_dict.keys(): raise ValidationError("Invalid modifier JSON format - missing id of item")
        if not 'quantity' in item_dict.keys(): raise ValidationError("Invalid modifier JSON format - missing quantity of item")
        if int(item_dict['quantity']) < 0: raise ValidationError("Invalid modifier JSON format - quantity must be 0 or greater")
        if 'modifiers' in item_dict.keys():
            validate_modifiers(item_dict['modifiers'])
    return True


