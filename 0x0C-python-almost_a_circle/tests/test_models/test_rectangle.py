import unittest
from unittest.mock import patch
from io import StringIO

from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Tests for the Rectangle class itself."""

    def test_is_subclass_of_base(self):
        """Test if Rectangle is a subclass of Base."""
        self.assertTrue(issubclass(Rectangle, Base))


class TestRectangleInstances(unittest.TestCase):
    """
    Test for rectangle instances
    """

    def setUp(self):
        """This method sets up the fixtures"""
        self.r1 = Rectangle(4, 3)
        self.r2 = Rectangle(6, 4)
        self.r3 = Rectangle(7, 5, 0, 0, 8)
        self.r4 = Rectangle(8, 3)
        self.r9 = Rectangle(6, 3, 2, 2, 10)

    def tearDown(self):
        """
        Resets the ID counter to its initial state in the Base class.
        """
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test if IDs are assigned correctly"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 8)
        self.assertEqual(self.r4.id, 3)

    def test_setter_and_getter(self):
        """Test for setter and getter method"""
        self.r1.width = 5
        self.r1.height = 3
        self.r1.x = 6
        self.r1.y = 4

        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 6)
        self.assertEqual(self.r1.y, 4)
        self.assertEqual(self.r3.width, 7)
        self.assertEqual(self.r3.height, 5)

    def test_raise_TypeError(self):
        """
        Tests if TypeError is raised for non-integer inputs.
        """
        with self.assertRaises(TypeError):
            r5 = Rectangle("a", 5)
            r6 = Rectangle(4, "d")
            self.r3.x = "5"  # String
            self.r3.y = "bar"  # String
            self.r3.width = "a"  # String
            self.r3.height = "b"  # String

    def test_raise_ValueError(self):
        """
        Tests if ValueError is raised for invalid values.
        """
        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 5)  # Width should be > 0
            r8 = Rectangle(6, -3)  # Height should be > 0
            self.r3.x = -5  # X should be >= 0
            self.r3.y = -1  # Y should be >= 0
            self.r3.width = -4  # Width should be > 0
            self.r3.height = 0  # Height should be > 0

    def test_area(self):
        """Test if the area is calculated correctly"""
        self.assertEqual(self.r1.area(), 12)
        self.assertEqual(self.r2.area(), 24)

        self.r3.width = 7
        self.r3.height = 9

        self.assertEqual(self.r3.area(), 63)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_output(self, mock_stdout):
        """Test if display method output correct rectangle"""
        # Create a Rectangle instance
        r = Rectangle(3, 4)

        # Call the display method
        r.display()

        # Get the printed output from mock_stdout
        printed_output = mock_stdout.getvalue().strip()

        # Assert the printed output matches the expected result
        expected_output = "###\n###\n###\n###"
        self.assertEqual(printed_output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_coordinates(self, mock_stdout):
        """Test if display method output correct cordinates"""
        r = Rectangle(5, 2, 3, 2)
        r.display()

        printed_output = mock_stdout.getvalue().rstrip()
        expected_output = "\n\n   #####\n   #####"

        self.assertEqual(printed_output, expected_output)

    def test__str__(self):
        """Test return value of __str__ method"""
        self.assertEqual(str(self.r9), "[Rectangle] (10) 2/2 - 6/3")

        self.r9.x = 1
        self.r9.y = 3
        self.r9.width = 4

        self.assertNotEqual(str(self.r9), "[Rectangle] (10) 2/2 - 6/3")

    def test_update_with_arg(self):
        """
        Test if update method correctly updates the rectangle with *args
        """

        r10 = Rectangle(6, 3, 1, 1, 76)

        self.assertEqual(str(r10), "[Rectangle] (76) 1/1 - 6/3")

        r10.update()
        self.assertEqual(str(r10), "[Rectangle] (76) 1/1 - 6/3")

        r10.update(68)
        self.assertEqual(str(r10), "[Rectangle] (68) 1/1 - 6/3")

        r10.update(68, 4)
        self.assertEqual(str(r10), "[Rectangle] (68) 1/1 - 4/3")

        r10.update(68, 4, 7)
        self.assertEqual(str(r10), "[Rectangle] (68) 1/1 - 4/7")

        r10.update(68, 4, 7, 2)
        self.assertEqual(str(r10), "[Rectangle] (68) 2/1 - 4/7")

        r10.update(68, 4, 7, 2, 3)
        self.assertEqual(str(r10), "[Rectangle] (68) 2/3 - 4/7")

        my_tuple = (10, 2, 4, 6, 8)
        r10.update(*my_tuple)
        self.assertEqual(str(r10), "[Rectangle] (10) 6/8 - 2/4")

    def test_update_with_kwargs(self):
        """
        Test if update correctly updates rectangle with **kwargs
        """

        r11 = Rectangle(9, 6, 2, 2, 53)
        self.assertEqual(str(r11), "[Rectangle] (53) 2/2 - 9/6")

        r11.update()
        self.assertEqual(str(r11), "[Rectangle] (53) 2/2 - 9/6")

        r11.update(id=45)
        self.assertEqual(str(r11), "[Rectangle] (45) 2/2 - 9/6")

        r11.update(width=5)
        self.assertEqual(str(r11), "[Rectangle] (45) 2/2 - 5/6")

        r11.update(height=3)
        self.assertEqual(str(r11), "[Rectangle] (45) 2/2 - 5/3")

        r11.update(x=1)
        self.assertEqual(str(r11), "[Rectangle] (45) 1/2 - 5/3")

        r11.update(y=0)
        self.assertEqual(str(r11), "[Rectangle] (45) 1/0 - 5/3")

        my_dict = {"width": 6, "height": 4, "x": 3, "y": 4, "id": 26}

        r11.update(**my_dict)
        self.assertEqual(str(r11), "[Rectangle] (26) 3/4 - 6/4")

    def test_rectangle_to_dict(self):
        """
        Test for the return value of to_dictionary.
        
        Dictionary must contain id, width, height, x and y attributes
        """
        r13 = Rectangle(7, 5, 1, 2, 8)
        rect_dict = r13.to_dictionary()
        my_dict = {'id': 8, 'width': 7, 'height': 5, 'x': 1, 'y': 2}
        self.assertDictEqual(rect_dict, my_dict)

        r13.update(width=3)
        rect_dict_2 = r13.to_dictionary()
        my_dict_2 = {'id': 8, 'width': 3, 'height': 5, 'x': 1, 'y': 2}
        self.assertTrue(rect_dict_2, my_dict_2)


if __name__ == '__main__':
    unittest.main()
