"""
Test class for Pypercraft
"""

import os
import unittest
import datetime
from project.project import Project


def get_current_datetime():
    """
    Gets current time
    """
    current_datetime = datetime.datetime.now()
    return current_datetime


class TestProject(unittest.TestCase):
    """
    Tests the Project Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the class instance
        """
        cls.api_key = os.getenv("OPENAI_API_KEY")
        cls.project = Project(cls.api_key)

    def test_result(self):
        """
        Tests the title
        """
        title = self.project.my_method()
        self.assertIsInstance(title, dict)
        self.assertNotEqual(title["results"], "")
        self.assertGreater(len(title["results"]), 3)


if __name__ == "__main__":
    unittest.main()
