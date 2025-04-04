import mysql.connector

class DatabaseConnector:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def open_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="your_password",
                database="TechShopDB"
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def close_connection(self):
        if self.cursor:
            self.cursor.close() 
        if self.connection:
            self.connection.close() 
