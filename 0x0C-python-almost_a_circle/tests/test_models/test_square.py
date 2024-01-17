import unittest
from unittest.mock import patch
from io import StringIO

from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquareClass(unittest.TestCase):
    """Tests for the Square class itself."""

    def test_is_subclass_of_rectangle(self):
        """Test if Square is a subclass of Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))


class TestSquareleInstances(unittest.TestCase):
    """
    Test for rectangle instances
    """

    def setUp(self):
        """This method sets up the fixtures"""
        self.s1 = Square(4)
        self.s2 = Square(6)
        self.s3 = Square(7, 0, 0, 8)
        self.s4 = Square(8)
        self.s9 = Square(6, 2, 2, 10)

    def tearDown(self):
        """
        Resets the ID counter to its initial state in the Base class.
        """
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test if IDs are assigned correctly"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 8)
        self.assertEqual(self.s4.id, 3)

    def test_setter_and_getter(self):
        """Test for setter and getter method"""
        self.s1.size = 5
        self.s1.x = 6
        self.s1.y = 4

        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s1.x, 6)
        self.assertEqual(self.s1.y, 4)
        self.assertEqual(self.s3.width, 7)
        self.assertEqual(self.s3.height, 7)

    def test_raise_TypeError(self):
        """
        Tests if TypeError is raised for non-integer inputs.
        """
        with self.assertRaises(TypeError):
            r5 = Square("a")
            self.r3.x = "5"  # String
            self.r3.y = "bar"  # String
            self.r3.width = "a"  # String
            self.r3.height = "b"  # String

    def test_raise_ValueError(self):
        """
        Tests if ValueError is raised for invalid values.
        """
        with self.assertRaises(ValueError):
            s7 = Square(0)  # Size should be > 0
            s8 = Square(-3)  # Size should be > 0
            self.s3.x = -5  # X should be >= 0
            self.s3.y = -1  # Y should be >= 0
            self.s3.size = -4  # size should be > 0
            self.s3.size = 0  # size should be > 0

    def test_area(self):
        """Test if the area is calculated correctly"""
        self.assertEqual(self.s1.area(), 16)
        self.assertEqual(self.s2.area(), 36)

        self.s3.width = 7

        self.assertEqual(self.s3.area(), 49)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_output(self, mock_stdout):
        """Test if display method output correct square"""
        # Create a Square instance
        r = Square(4)

        # Call the display method
        r.display()

        # Get the printed output from mock_stdout
        printed_output = mock_stdout.getvalue().strip()

        # Assert the printed output matches the expected result
        expected_output = "####\n####\n####\n####"
        self.assertEqual(printed_output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_coordinates(self, mock_stdout):
        """Test if display method output correct cordinates"""
        r = Square(4, 3, 2)
        r.display()

        printed_output = mock_stdout.getvalue().rstrip()
        expected_output = "\n\n   ####\n   ####\n   ####\n   ####"

        self.assertEqual(printed_output, expected_output)

    def test__str__(self):
        """Test return value of __str__ method"""
        self.assertEqual(str(self.s9), "[Square] (10) 2/2 - 6")

        self.s9.x = 1
        self.s9.y = 3
        self.s9.size = 4

        self.assertNotEqual(str(self.s9), "[Square] (10) 2/2 - 6")

    def test_update_with_arg(self):
        """
        Test if update method correctly updates the square with *args
        """

        s10 = Square(6, 1, 1, 76)

        self.assertEqual(str(s10), "[Square] (76) 1/1 - 6")

        s10.update()
        self.assertEqual(str(s10), "[Square] (76) 1/1 - 6")

        s10.update(68)
        self.assertEqual(str(s10), "[Square] (68) 1/1 - 6")

        s10.update(68, 4)
        self.assertEqual(str(s10), "[Square] (68) 1/1 - 4")

        s10.update(68, 4, 2)
        self.assertEqual(str(s10), "[Square] (68) 2/1 - 4")

        s10.update(68, 4, 2, 3)
        self.assertEqual(str(s10), "[Square] (68) 2/3 - 4")

        my_tuple = (10, 2, 6, 8)
        s10.update(*my_tuple)
        self.assertEqual(str(s10), "[Square] (10) 6/8 - 2")

    def test_update_with_kwargs(self):
        """
        Test if update correctly updates square with **kwargs
        """

        s11 = Square(9, 2, 2, 53)
        self.assertEqual(str(s11), "[Square] (53) 2/2 - 9")

        s11.update()
        self.assertEqual(str(s11), "[Square] (53) 2/2 - 9")

        s11.update(id=45)
        self.assertEqual(str(s11), "[Square] (45) 2/2 - 9")

        s11.update(size=5)
        self.assertEqual(str(s11), "[Square] (45) 2/2 - 5")

        s11.update(x=1)
        self.assertEqual(str(s11), "[Square] (45) 1/2 - 5")

        s11.update(y=0)
        self.assertEqual(str(s11), "[Square] (45) 1/0 - 5")

        my_dict = {"size": 6, "x": 3, "y": 4, "id": 26}

        s11.update(**my_dict)
        self.assertEqual(str(s11), "[Square] (26) 3/4 - 6")


if __name__ == '__main__':
    unittest.main()
