class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock available"):
        super().__init__(message)

class InvalidDataException(Exception):
    def __init__(self, message="Invalid data provided"):
        super().__init__(message)

class PaymentFailedException(Exception):
    def __init__(self, message="Payment processing failed"):
        super().__init__(message)
