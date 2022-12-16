import sys
import io
import os
import unittest
from unittest.mock import patch

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions import task_06

class TestSum(unittest.TestCase):
    def runTest(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=io.StringIO()) as fake_out:
            cnt = task_06.get_count()
            self.assertEqual(cnt, expected_out)
    
    def test_number_range_list(self):
        """
        Az előfordulások számát kellene visszaadnia
        """
        self.runTest('is', 2)

if __name__ == '__main__':
    result = unittest.main()
