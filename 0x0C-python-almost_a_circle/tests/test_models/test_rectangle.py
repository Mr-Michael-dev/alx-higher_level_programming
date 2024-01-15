from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """
    Test for rectangle features

    Methods:
        setUp(self): sets the fixture
        tearDown(self): does nothing
        test_rectangle_is_subclass(self):
        test_id(self):
        test_setter_and_getter(self):
    """

    def setUp(self):
        """This method sets up the fixtures"""
        self.r1 = Rectangle(4, 3)
        self.r2 = Rectangle(6, 4)
        self.r3 = Rectangle(7, 5, 0, 0, 8)
        self.r4 = Rectangle(8, 3)

    def tearDown(self):
        """
        Resets the ID counter to its initial state in the Base class.
        """
        Base._Base__nb_objects = 0


    def test_rectangle_is_subclass(self):
        """Test if rectangle is subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base), "Not a subclass of Base")

    def test_id(self):
        """Test for instance id"""
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
