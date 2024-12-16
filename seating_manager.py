"""
Main restaurant tables manager system
"""
from table import Table
from group import Group

class SeatingMananger:
    """
    Manages customers groups: seats them into tables and releases the tables
    once customers leaves the restaurant.
    """
    def __init__(self) -> None:
        pass

    def arrives(self, customer_group: Group) -> None:
        """
        Sits customers into a table.
        """

    def leaves(self, customer_group: Group) -> None:
        """
        Releases a group from a table when leaving.
        """

    def locate(self, customer_group: Group) -> Table:
        """
        Locates a table where a group of customers a seating.
        """
