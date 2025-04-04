from database_connector import DatabaseConnector

class SalesReport:
    def __init__(self):
        self.db = DatabaseConnector()

    def total_sales(self):
        """Retrieve total sales revenue from orders."""
        try:
            self.db.connect()
            query = "SELECT SUM(TotalAmount) FROM Orders"
            self.db.cursor.execute(query)
            result = self.db.cursor.fetchone()
            if result and result[0]:
                print(f"Total Sales Revenue: ₹{result[0]}")
            else:
                print("No sales data available.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def sales_by_product(self):
        """Retrieve sales count for each product."""
        try:
            self.db.connect()
            query = """
            SELECT P.ProductName, SUM(OD.Quantity) AS TotalSold 
            FROM OrderDetails OD 
            JOIN Products P ON OD.ProductID = P.ProductID 
            GROUP BY P.ProductName
            """
            self.db.cursor.execute(query)
            results = self.db.cursor.fetchall()
            if results:
                print("\nSales Report by Product:")
                for row in results:
                    print(f"{row[0]} - {row[1]} units sold")
            else:
                print("No product sales data available.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def sales_by_date(self):
        """Retrieve daily sales report."""
        try:
            self.db.connect()
            query = """
            SELECT OrderDate, SUM(TotalAmount) AS TotalSales 
            FROM Orders 
            GROUP BY OrderDate
            ORDER BY OrderDate DESC
            """
            self.db.cursor.execute(query)
            results = self.db.cursor.fetchall()
            if results:
                print("\nSales Report by Date:")
                for row in results:
                    print(f"{row[0]} - ₹{row[1]}")
            else:
                print("No daily sales data available.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()
