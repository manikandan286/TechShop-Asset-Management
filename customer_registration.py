import mysql.connector

class DatabaseConnector:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="yourpassword",
                database="TechShopDB"
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def close_connection(self):
        self.cursor.close()
        self.conn.close()

class CustomerRegistration:
    def __init__(self):
        self.db = DatabaseConnector()

    def register_customer(self, name, email, phone):
        try:
            self.db.cursor.execute("SELECT * FROM Customers WHERE email = %s", (email,))
            if self.db.cursor.fetchone():
                print("Error: Email already registered!")
                return

            sql = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"
            values = (name, email, phone)
            self.db.cursor.execute(sql, values)
            self.db.conn.commit()
            print("Customer registered successfully!")
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
        finally:
            self.db.close_connection()

if __name__ == "__main__":
    customer = CustomerRegistration()
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    customer.register_customer(name, email, phone)
