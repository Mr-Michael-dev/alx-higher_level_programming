#!/usr/bin/python3
"""
MyInt class that inherits from int
"""


class MyInt(int):
    """
    This class represents a rebel integer with inverted equality operators.

    Methods:
    - __eq__: Inverts the == operator
    - __ne__: Inverts the != operator
    """

    def __eq__(self, other):
        """
        Inverts the == operator

        Args:
            - other: Another object for comparison

        Returns:
            - True if not equal, False if equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator

        Args:
            - other: Another object for comparison

        Returns:
            - True if equal, False if not equal
        """
        return super().__eq__(other)
