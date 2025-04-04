from models import Customer, Product, Order, OrderDetail, Inventory, Payment
from exceptions import InsufficientStockException, PaymentFailedException

customers = [
    Customer(1, "Alice", "Smith", "alice@example.com", "9876543210", "456 Street"),
    Customer(2, "Bob", "Jones", "bob@example.com", "8765432109", "789 Avenue")
]

products = [
    Product(101, "Laptop", "Gaming Laptop", 1500),
    Product(102, "Headphones", "Noise Cancelling", 200)
]

inventory = [
    Inventory(301, products[0], 10),
    Inventory(302, products[1], 5)
]

orders = []

customer = customers[0]
order = Order(501, customer, "2025-04-03", 0)  
orders.append(order)

order_details = [
    OrderDetail(1, order, products[0], 2),  
    OrderDetail(2, order, products[1], 1)   
]

total_amount = sum(od.calculate_subtotal() for od in order_details)
order._Order__total_amount = total_amount 
try:
    payment = Payment(order, total_amount)
    payment.process_payment()
    print("Payment successful:", payment.get_payment_details())
except PaymentFailedException as e:
    print("Payment Error:", e)

print("Order Details:", order.get_order_details())
