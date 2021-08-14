# DOCKER INSTRUCTIONS
While in the same folder as the Dockerfile, run the following in cmd:
    docker build -t pos:1.0.0 .
    docker run -d --name pos -p 8000:8000 pos:1.0.0

# USAGE
View available items on menu:
    http://127.0.0.1:8000/menu/

View list of orders:
    http://127.0.0.1:8000/order/

See the following for sample CRUD operations:
    - menu.py for the menu
    - order.py for orders

While in the same folder as manage.py in the Docker container, run the following for tests:
    python manage.py test
