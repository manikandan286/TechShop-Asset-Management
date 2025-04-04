class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address

    def get_customer_info(self):
        return {
            "Customer ID": self.__customer_id,
            "Name": f"{self.__first_name} {self.__last_name}",
            "Email": self.__email,
            "Phone": self.__phone,
            "Address": self.__address
        }

class Product:
    def __init__(self, product_id, name, description, price):
        self.__product_id = product_id
        self.__name = name
        self.__description = description
        self.__price = price

    def get_product_details(self):
        return {
            "Product ID": self.__product_id,
            "Name": self.__name,
            "Description": self.__description,
            "Price": self.__price
        }

class Inventory:
    def __init__(self, inventory_id, product, quantity):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity = quantity

    def update_stock(self, purchased_qty):
        if purchased_qty > self.__quantity:
            raise InsufficientStockException("Not enough stock available.")
        self.__quantity -= purchased_qty

    def get_inventory_status(self):
        return {
            "Inventory ID": self.__inventory_id,
            "Product": self.__product.get_product_details(),
            "Stock Available": self.__quantity
        }

class Order:
    def __init__(self, order_id, customer, order_date, total_amount):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = order_date
        self.__total_amount = total_amount

    def get_order_details(self):
        return {
            "Order ID": self.__order_id,
            "Customer": self.__customer.get_customer_info(),
            "Order Date": self.__order_date,
            "Total Amount": self.__total_amount
        }

class OrderDetail:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self):
        return self.__quantity * self.__product.get_product_details()["Price"]

    def get_order_detail_info(self):
        return {
            "Order Detail ID": self.__order_detail_id,
            "Order ID": self.__order.get_order_details()["Order ID"],
            "Product": self.__product.get_product_details(),
            "Quantity": self.__quantity,
            "Subtotal": self.calculate_subtotal()
        }

class Payment:
    def __init__(self, order, amount, payment_status="Pending"):
        self.__order = order
        self.__amount = amount
        self.__payment_status = payment_status

    def process_payment(self):
        if self.__amount < self.__order.get_order_details()["Total Amount"]:
            raise PaymentFailedException("Insufficient payment amount.")
        self.__payment_status = "Completed"

    def get_payment_details(self):
        return {
            "Order ID": self.__order.get_order_details()["Order ID"],
            "Amount": self.__amount,
            "Payment Status": self.__payment_status
        }
