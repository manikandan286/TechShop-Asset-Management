from database_connector import DatabaseConnector

class PaymentProcessing:
    def __init__(self):
        self.db = DatabaseConnector()

    def record_payment(self, order_id, payment_method, amount):
        """Records a payment for an order in the database."""
        try:
            self.db.connect()
            query = """
                INSERT INTO Payments (OrderID, PaymentMethod, Amount, PaymentDate)
                VALUES (%s, %s, %s, NOW())
            """
            self.db.cursor.execute(query, (order_id, payment_method, amount))
            self.db.conn.commit()
            print("Payment recorded successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def get_payment_details(self, order_id):
        """Fetches payment details for a specific order."""
        try:
            self.db.connect()
            query = "SELECT * FROM Payments WHERE OrderID = %s"
            self.db.cursor.execute(query, (order_id,))
            payment = self.db.cursor.fetchone()
            return payment
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

if __name__ == "__main__":
    payment = PaymentProcessing()
    payment.record_payment(order_id=1, payment_method="Credit Card", amount=250.50)
