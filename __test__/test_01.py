import io
import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions import task_01

class TestSum(unittest.TestCase):
    def test_print_first_chars(self):
        """
        Az első karaktereknek meg kellene jelenniük
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        result = task_01.print_first_chars()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'H\nt\ni\na\nt\nm\n')

if __name__ == '__main__':
    result = unittest.main()
