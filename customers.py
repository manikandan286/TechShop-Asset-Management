from database_connector import DatabaseConnector

class Customer:
    def __init__(self, customer_id=None, first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.db = DatabaseConnector()
    
    def register_customer(self):
        """Insert a new customer into the database."""
        try:
            self.db.connect()
            query = "INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s)"
            values = (self.first_name, self.last_name, self.email, self.phone, self.address)
            self.db.cursor.execute(query, values)
            self.db.conn.commit()
            print("Customer registered successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()
    
    def get_customer_by_email(self, email):
        """Retrieve customer details by email."""
        try:
            self.db.connect()
            query = "SELECT * FROM Customers WHERE Email = %s"
            self.db.cursor.execute(query, (email,))
            result = self.db.cursor.fetchone()
            if result:
                print(f"Customer Found: {result}")
            else:
                print("No customer found with this email.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()
    
    def update_customer_info(self, customer_id, new_email, new_phone, new_address):
        """Update customer details."""
        try:
            self.db.connect()
            query = "UPDATE Customers SET Email = %s, Phone = %s, Address = %s WHERE CustomerID = %s"
            values = (new_email, new_phone, new_address, customer_id)
            self.db.cursor.execute(query, values)
            self.db.conn.commit()
            print("Customer information updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()
    
    def delete_customer(self, customer_id):
        """Delete a customer from the database."""
        try:
            self.db.connect()
            query = "DELETE FROM Customers WHERE CustomerID = %s"
            self.db.cursor.execute(query, (customer_id,))
            self.db.conn.commit()
            print("Customer deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()
