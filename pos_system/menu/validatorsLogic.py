from menu.models import Item


def validate_order_id(menu_object, order_list):
    for item in order_list:  #item in the order
        try:
            menu_object.objects.get(pk=item['id'])
        except:
            return "ID# "+ str(item['id']) + " Does not exist in menu"
    return True

def validate_payment(total, payment):
    if total == payment:
        return True
    return False

def validate_order_items_logic(menu_object, order_list):
    '''checks to make sure the items ordered are valid. Ie, no pepperoni on hamburgers and no buns on pizza'''
    for item in order_list:  #item in the order
        menu_item = menu_object.objects.get(pk=item['id'])
        
        if 'modifiers' in item:
            modifier_dict = item['modifiers']
            for modifier_key in modifier_dict:  #loop through every modifier in the order item
                result = Item.find_modifier_in_menu_item(modifier_key, menu_item)
                if(type(result) == bool): return modifier_key + " does not exist in menu item " + item['description']
                for topping in modifier_dict[modifier_key]:
                    if Item.find_topping_in_modifier(topping, result) == False: return topping + " does not exist in menu item " + item['description'] + ' with modifier: ' + modifier_key
                
                print(type(result))
                print(result)
    return True

def validate_quantity_logic(menu_object, order_list):
    required_quantities = dict()
    for item in order_list:  #item in the order
        
        current_id = item['id']
        current_quantity = item['quantity']

        if not current_id in required_quantities.keys():
            required_quantities[current_id] = current_quantity
        else:
            required_quantities[current_id] += current_quantity

    for order_item_id in required_quantities:
        available_quantity = Item.quantity_by_id(menu_object, order_item_id)
        if (required_quantities[order_item_id] > available_quantity):
            return f"Not enough {Item.description_by_id(menu_object, order_item_id)} available!"
    return required_quantities
     