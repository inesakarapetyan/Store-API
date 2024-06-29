# Store-API
Django


--------------------------------------------------------------------------------------------------------------------------------------------------------
|                                                            DESCRIPTION                                                                               |
--------------------------------------------------------------------------------------------------------------------------------------------------------



This project is a simple online store backend built using a RESTful API. It provides endpoints for managing products, customers, and orders. The API is designed to handle basic CRUD (Create, Read, Update, Delete) operations and can be used as a foundation for a more complex e-commerce platform.

Key Features

1.Product Management: Create, read, update, and delete products in the store. Each product has attributes such as name, description, price, and stock quantity.

2.Customer Management: Manage customer information, including creating new customers, viewing customer details, updating information, and deleting customers.

3.Order Management: Handle orders placed by customers. This includes creating new orders, viewing order details, updating order status, and deleting orders.

API Endpoints

Product Endpoints

-GET /api/products/: Retrieve a list of all products.


-POST /api/products/: Create a new product.

-GET /api/products/{id}/: Retrieve details of a specific product.

-PUT /api/products/{id}/: Update details of a specific product.

-DELETE /api/products/{id}/: Delete a specific product.

Customer Endpoints

-GET /api/customers/: Retrieve a list of all customers.

-POST /api/customers/: Create a new customer.

-GET /api/customers/{id}/: Retrieve details of a specific customer.

-PUT /api/customers/{id}/: Update details of a specific customer.
-DELETE /api/customers/{id}/: Delete a specific customer.

Order Endpoints

-GET /api/orders/: Retrieve a list of all orders.

-POST /api/orders/: Create a new order.

-GET /api/orders/{id}/: Retrieve details of a specific order.

-PUT /api/orders/{id}/: Update details of a specific order.

-DELETE /api/orders/{id}/: Delete a specific order.





------------------------------------------------------------------------------------------------------------------------------------------------------
|                                                            RUN CODE                                                                                |
------------------------------------------------------------------------------------------------------------------------------------------------------

For Windows Users

1.Open Visual Studio Code

2.Open Terminal:

Open the integrated terminal in VS Code by navigating to 'View > Terminal' or using the shortcut 'Ctrl + ~' (backtick).

3.py -m venv venv         # Create a virtual environment

4.\venv\Scripts\activate      # Activate the virtual environment

5.py -m pip install --upgrade pip    # Upgrade pip

6.pip install django    # Install Django

7.django-admin startproject myproject      # Create a Django project

8.cd myproject              # Navigate into the project directory

9.python manage.py startapp main   #Create a project

10.python manage.py runserver         # Start the Django development server

For Mac or Linux Users

1.Open Visual Studio Code

2.Open Terminal:

Open the integrated terminal in VS Code by navigating to 'View > Terminal' or using the shortcut 'Ctrl + ~' (backtick).

3.python3 -m venv venv             # Create a virtual environment

4.source ./venv/bin/activate            # Activate the virtual environment


5.python3 -m pip install --upgrade pip    # Upgrade pip

6.pip install django         # Install Django

7.django-admin startproject myproject     # Create a Django project

8.cd myproject              # Navigate into the project directory

9.python3 manage.py startapp main   #Create a project

10.python3 manage.py runserver         # Start the Django development server
