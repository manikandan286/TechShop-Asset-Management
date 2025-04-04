from database_connector import DatabaseConnector

class CustomerAccount:
    def __init__(self):
        self.db = DatabaseConnector()

    def update_customer_info(self, customer_id, new_email=None, new_phone=None):
        """Update customer email or phone number in the database."""
        try:
            self.db.connect()
            if new_email:
                query = "UPDATE Customers SET Email = %s WHERE CustomerID = %s"
                self.db.cursor.execute(query, (new_email, customer_id))
            if new_phone:
                query = "UPDATE Customers SET Phone = %s WHERE CustomerID = %s"
                self.db.cursor.execute(query, (new_phone, customer_id))
            self.db.conn.commit()
            print("Customer information updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def delete_customer_account(self, customer_id):
        """Delete a customer account from the database."""
        try:
            self.db.connect()
            query = "DELETE FROM Customers WHERE CustomerID = %s"
            self.db.cursor.execute(query, (customer_id,))
            self.db.conn.commit()
            print("Customer account deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

if __name__ == "__main__":
    account = CustomerAccount()
    account.update_customer_info(customer_id=1, new_email="newemail@example.com", new_phone="9876543210")
