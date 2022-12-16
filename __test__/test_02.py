import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions import task_02

class TestSum(unittest.TestCase):
    def test_lowercase_list(self):
        """
        A lista elemeinek kisbetűsnek kellene lennie.
        """
        data = ['Peti', 'Józsi', 'Béci', 'Sanyi', 'Pisti']
        result = task_02.transform_to_lowercase(data)
        self.assertEqual(
            result,
            ['peti', 'józsi', 'béci', 'sanyi', 'pisti']
        )

if __name__ == '__main__':
    result = unittest.main()
