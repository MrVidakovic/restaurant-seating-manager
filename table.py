"""
A table in the restaurant.
"""
class IncorrectSeatsSizeError(Exception):
    """Exception raised when the number of sites is not between 2 and 6"""
    def __init__(self):
        message = "Incorrect number of seats. A table should have between 2 and 6 seats"

        self.message = message
        super().__init__(message)
        self.error_code = 1

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

class TableNotFoundError(Exception):
    """Exception raised when the number of sites is not between 2 and 6"""
    def __init__(self):
        message = "The reference table provided is not found"

        self.message = message
        super().__init__(message)
        self.error_code = 1

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class Table:
    """
    A table in the restaurant.
    """
    def __init__(self, table_number: int, seats: int) -> None:
        if (seats < 2) or (seats > 6):
            raise IncorrectSeatsSizeError

        self.table_number = table_number
        self.seats = seats
        self.next = None
        self.previous = None

class TableList:
    """
    A double linked list of tables.
    """
    def __init__(self):
        self.root = None

    def add_empty_list(self, table_number: int, seats: int) -> None:
        if self.root is None:
            new_table = Table(table_number=table_number, seats=seats)
            self.root = new_table

    def add_begging(self, table_number: int, seats: int) -> None:
        if self.root is None:
            self.add_empty_list(table_number=table_number, seats=seats)
            return

        new_table = Table(table_number=table_number, seats=seats)
        new_table.next = self.root
        self.root.previous = new_table
        self.root = new_table

    def add_end(self, table_number: int, seats: int) -> None:
        if self.root is None:
            self.add_empty_list(table_number=table_number, seats=seats)
            return

        list_pointer = self.root
        while list_pointer.next is not None:
            list_pointer = list_pointer.next
        new_table = Table(table_number=table_number, seats=seats)
        list_pointer.next = new_table
        new_table.previous = list_pointer

    def add_after_table(self, table_number_to_locate: int, table_number: int, seats: int) -> None:
        if self.root is None:
            self.add_empty_list(table_number=table_number, seats=seats)
            return

        table_to_locate = self.root
        while table_to_locate is not None:
            if table_to_locate.table_number == table_number_to_locate:
                break
            table_to_locate = table_number_to_locate.next

        if table_to_locate is None:
            raise TableNotFoundError

        new_table = Table(table_number=table_number, seats=seats)
        new_table.previous = table_to_locate
        new_table.next = table_to_locate.next
        if table_to_locate.next is not None:
            table_to_locate.next.previous = new_table
        table_to_locate.next = new_table
