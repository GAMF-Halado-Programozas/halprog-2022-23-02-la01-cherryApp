import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions import task_04

class TestSum(unittest.TestCase):
    def test_getting_second_list_row(self):
        """
        A lista második oszlopát kellene visszaadnia.
        """
        numbers = [
            [1, 5, 3],
            [4, 5, 6],
            [7, 9, 9]
        ]
        result = task_04.get_second_row(numbers)
        self.assertEqual(
            result,
            [5, 5, 9]
        )

if __name__ == '__main__':
    result = unittest.main()
