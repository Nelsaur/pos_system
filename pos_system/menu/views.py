from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from menu.serializers import MenuSerializer, OrderSerializer

from .models import Item, Order

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .validatorsLogic import validate_order_id, validate_payment, validate_order_items_logic, validate_quantity_logic

@api_view(['GET'])
def MenuList(request):
    tasks= Item.objects.all()
    serializer = MenuSerializer(tasks, many=True)
    
    return Response(serializer.data)

class ListMenuAPIView(ListAPIView):
    """This endpoint list all of the available Menus from the database"""
    queryset = Item.objects.all()
    serializer_class = MenuSerializer

class ItemMenuAPIView(RetrieveAPIView):
    """This endpoint list all of the available Menus from the database"""
    queryset = Item.objects.all()
    serializer_class = MenuSerializer
 
    #def get(self, request, *args, **kwargs):
    #    return self.retrieve(request, *args, **kwargs)

class CreateMenuAPIView(CreateAPIView):
    """This endpoint allows for creation of a Menu"""
    queryset = Item.objects.all()
    serializer_class = MenuSerializer

class UpdateMenuAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Menu by passing in the id of the Menu to update"""
    queryset = Item.objects.all()
    serializer_class = MenuSerializer

class DeleteMenuAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Menu from the database"""
    queryset = Item.objects.all()
    serializer_class = MenuSerializer




class ListOrderAPIView(ListAPIView):
    """This endpoint list all of the available Menus from the database"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ItemOrderAPIView(RetrieveAPIView):
    """This endpoint list all of the available Menus from the database"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CreateOrderAPIView(CreateAPIView):
    """This endpoint allows for creation of a Menu"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    #serializer_class.data["note"] = "Testing"
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

from django.core.exceptions import ValidationError
@api_view(['POST'])
def CreateOrder(request):
    serializerinitial = OrderSerializer(data=request.data)
    if not serializerinitial.is_valid():
        return Response(serializerinitial.errors)

    #loop through the order items
    item_list = request.data['items']

    id_result = validate_order_id(Item, item_list)
    if type(id_result) == str:
        return Response(id_result, status=400)

    append_result = Order.append_description_price(Item, item_list)
    if type(append_result) == str:
        return Response(append_result, status=400)

    validate_order_list_result = validate_order_items_logic(Item, item_list)
    if type(validate_order_list_result) == str:
        return Response(validate_order_list_result, status=400)
    
    #validate quantity
    validate_quantity_result = validate_quantity_logic(Item, item_list)
    if type(validate_quantity_result) == str:
        return Response(validate_quantity_result, status=400)

    bill_total = Order.bill_total(item_list)

    if not validate_payment(bill_total, float(str(request.data['payment']))):
        return Response("Incorrect payment. Total bill is $" + "{:.2f}".format(bill_total), status=400)

    #all validations completed! Process!
    Item.update_quantity(validate_quantity_result, Item)

    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)






