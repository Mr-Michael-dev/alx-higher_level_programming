from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """
    This test case class contain test for Base class

    Test Cases:
        test_id: test if new id is created for each instanceof Base class
    """

    def setUp(self):
        """"This method sets the fixture"""
        self.base_inst_1 = Base()
        self.base_inst_2 = Base()
        self.base_inst_3 = Base(25)
        self.base_inst_4 = Base(5)
        self.base_inst_5 = Base()

    def tearDown(self):
        """
        Resets the ID counter to its initial state in the Base class.
        """
        Base._Base__nb_objects = 0


    def test_id(self):
        """
        Test case for id of each created instance
        """

        self.assertEqual(self.base_inst_1.id, 1)
        self.assertEqual(self.base_inst_2.id, 2)
        self.assertEqual(self.base_inst_3.id, 25)
        self.assertEqual(self.base_inst_4.id, 5)
        self.assertEqual(self.base_inst_5.id, 3)

if __name__ == "__main__":
    unittest.main()
