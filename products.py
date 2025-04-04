from database_connector import DatabaseConnector

class Product:
    def __init__(self, product_id=None, name="", category="", price=0.0, stock=0, description=""):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.description = description
        self.db = DatabaseConnector()

    def add_product(self):
        """Insert a new product into the database."""
        try:
            self.db.connect()
            query = "INSERT INTO Products (Name, Category, Price, Stock, Description) VALUES (%s, %s, %s, %s, %s)"
            values = (self.name, self.category, self.price, self.stock, self.description)
            self.db.cursor.execute(query, values)
            self.db.conn.commit()
            print("Product added successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def update_product(self, product_id, new_name, new_category, new_price, new_stock, new_description):
        """Update product details."""
        try:
            self.db.connect()
            query = "UPDATE Products SET Name=%s, Category=%s, Price=%s, Stock=%s, Description=%s WHERE ProductID=%s"
            values = (new_name, new_category, new_price, new_stock, new_description, product_id)
            self.db.cursor.execute(query, values)
            self.db.conn.commit()
            print("Product updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def delete_product(self, product_id):
        """Delete a product from the database."""
        try:
            self.db.connect()
            query = "DELETE FROM Products WHERE ProductID = %s"
            self.db.cursor.execute(query, (product_id,))
            self.db.conn.commit()
            print("Product deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def get_product_by_id(self, product_id):
        """Retrieve product details by ProductID."""
        try:
            self.db.connect()
            query = "SELECT * FROM Products WHERE ProductID = %s"
            self.db.cursor.execute(query, (product_id,))
            result = self.db.cursor.fetchone()
            if result:
                print(f"Product Found: {result}")
            else:
                print("No product found with this ID.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()
