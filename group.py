"""
A group of customers.
"""
class IncorrectGroupSizeError(Exception):
    """Exception raised when the number of sites is not between 2 and 6"""
    def __init__(self):
        message = "Incorrect number of people. A group should have between 2 and 6 seats"
        self.message = message
        super().__init__(message)
        self.error_code = 1

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

class Group:

    """
    A group of customers.
    """
    def __init__(self, customers: int) -> None:
        if (customers < 1) or (customers > 6):
            raise IncorrectGroupSizeError

        self.customers = customers
        self.table = None
