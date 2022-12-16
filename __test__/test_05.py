import sys
import io
import os
import unittest
from unittest.mock import patch

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions import task_05

class TestSum(unittest.TestCase):
    def runTest(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=io.StringIO()) as fake_out:
            task_05.print_number_range()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)
    
    def test_number_range_list(self):
        """
        A számokat ki kellene írnia a megadott számig
        """
        self.runTest(5, '0\n1\n2\n3\n4')

if __name__ == '__main__':
    result = unittest.main()
