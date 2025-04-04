from database_connector import DatabaseConnector

class Inventory:
    def __init__(self, product_id=None, quantity=0):
        self.product_id = product_id
        self.quantity = quantity
        self.db = DatabaseConnector()

    def add_product(self, product_id, quantity):
        """Add new product stock to the inventory."""
        try:
            self.db.connect()
            query = "INSERT INTO Inventory (ProductID, Quantity) VALUES (%s, %s)"
            values = (product_id, quantity)
            self.db.cursor.execute(query, values)
            self.db.conn.commit()
            print("Product added to inventory successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def update_stock(self, product_id, quantity):
        """Update stock quantity of an existing product."""
        try:
            self.db.connect()
            query = "UPDATE Inventory SET Quantity = %s WHERE ProductID = %s"
            self.db.cursor.execute(query, (quantity, product_id))
            self.db.conn.commit()
            print("Inventory updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def remove_product(self, product_id):
        """Remove a product from inventory."""
        try:
            self.db.connect()
            query = "DELETE FROM Inventory WHERE ProductID = %s"
            self.db.cursor.execute(query, (product_id,))
            self.db.conn.commit()
            print("Product removed from inventory.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def get_stock(self, product_id):
        """Retrieve stock level of a product."""
        try:
            self.db.connect()
            query = "SELECT Quantity FROM Inventory WHERE ProductID = %s"
            self.db.cursor.execute(query, (product_id,))
            result = self.db.cursor.fetchone()
            if result:
                print(f"Stock available: {result[0]}")
            else:
                print("Product not found in inventory.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()
