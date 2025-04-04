from database_connector import DatabaseConnector

class Order:
    def __init__(self, order_id=None, customer_id=None, order_date="", total_amount=0.0, status="Pending"):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.total_amount = total_amount
        self.status = status
        self.db = DatabaseConnector()

    def place_order(self):
        """Insert a new order into the database."""
        try:
            self.db.connect()
            query = "INSERT INTO Orders (CustomerID, OrderDate, TotalAmount, Status) VALUES (%s, %s, %s, %s)"
            values = (self.customer_id, self.order_date, self.total_amount, self.status)
            self.db.cursor.execute(query, values)
            self.db.conn.commit()
            print("Order placed successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def update_order_status(self, order_id, new_status):
        """Update order status (e.g., Pending → Shipped → Delivered)."""
        try:
            self.db.connect()
            query = "UPDATE Orders SET Status = %s WHERE OrderID = %s"
            self.db.cursor.execute(query, (new_status, order_id))
            self.db.conn.commit()
            print("Order status updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def delete_order(self, order_id):
        """Delete an order from the database."""
        try:
            self.db.connect()
            query = "DELETE FROM Orders WHERE OrderID = %s"
            self.db.cursor.execute(query, (order_id,))
            self.db.conn.commit()
            print("Order deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def get_order_by_id(self, order_id):
        """Retrieve order details by OrderID."""
        try:
            self.db.connect()
            query = "SELECT * FROM Orders WHERE OrderID = %s"
            self.db.cursor.execute(query, (order_id,))
            result = self.db.cursor.fetchone()
            if result:
                print(f"Order Found: {result}")
            else:
                print("No order found with this ID.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()
