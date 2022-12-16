import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions import task_03

class TestSum(unittest.TestCase):
    def test_list_sorting(self):
        """
        A lista elemeinek rendezettnek kellene lennie.
        """
        data = ['Peti', 'Józsi', 'Béci', 'Sanyi', 'Pisti']
        result = task_03.sort_names(data)
        self.assertEqual(
            result,
            ['Béci', 'Józsi', 'Peti', 'Pisti', 'Sanyi']
        )

if __name__ == '__main__':
    result = unittest.main()
