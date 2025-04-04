from database_connector import DatabaseConnector

class ProductSearch:
    def __init__(self):
        self.db = DatabaseConnector()

    def search_by_name(self, product_name):
        """Search for products by name."""
        try:
            self.db.connect()
            query = "SELECT * FROM Products WHERE ProductName LIKE %s"
            self.db.cursor.execute(query, ('%' + product_name + '%',))
            results = self.db.cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def search_by_category(self, category):
        """Search for products by category."""
        try:
            self.db.connect()
            query = "SELECT * FROM Products WHERE Category = %s"
            self.db.cursor.execute(query, (category,))
            results = self.db.cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def get_recommendations(self):
        """Fetch recommended products (top 5 based on sales)."""
        try:
            self.db.connect()
            query = """
                SELECT P.ProductID, P.ProductName, SUM(O.Quantity) AS TotalSold
                FROM OrderDetails O
                JOIN Products P ON O.ProductID = P.ProductID
                GROUP BY P.ProductID
                ORDER BY TotalSold DESC
                LIMIT 5
            """
            self.db.cursor.execute(query)
            recommendations = self.db.cursor.fetchall()
            return recommendations
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

if __name__ == "__main__":
    search = ProductSearch()
    print(search.search_by_name("Laptop"))
    print(search.search_by_category("Electronics"))
    print(search.get_recommendations())
