import sys
import io
import os
import unittest
from unittest.mock import patch

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions import task_07

class TestUser(unittest.TestCase):
    def runTest(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=io.StringIO()) as fake_out:
            cnt = task_07.get_count()
            self.assertEqual(cnt, expected_out)
    
    def test_class_active_attribute(self):
        """
        Kellene lennie egy active attribútumnak igaz értékkel
        """
        self.assertTrue( hasattr(task_07.User, 'active') and task_07.User.active == True )
    
    def test_class_constructor(self):
        """
        A konstruktornak be kellene állítania a változókat
        """
        user = task_07.User('Pisti', 'p@p.hu')
        self.assertTrue( hasattr(user, 'name') and user.name == 'Pisti' )
        self.assertTrue( hasattr(user, 'email') and user.email == 'p@p.hu' )
        self.assertTrue( hasattr(user, 'active') and user.active == True )
        user2 = task_07.User('Pisti', 'p@p.hu', False)
        self.assertTrue( user2.active == False )
    
    def test_class_say_hello_method(self):
        """
        A say_hello metódusnak ki kellene írnia a megadott szöveget
        """
        user = task_07.User('Géza', 'p@p.hu')
        self.assertTrue(
            hasattr(user, 'say_hello') and callable(getattr(user, 'say_hello'))
        )

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user.say_hello()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'Hello, my name is Géza.\n')
    
    def test_class_is_active_method(self):
        """
        A is_active metódusnak vissza kellene adnia az active értékét
        """
        user = task_07.User('Géza', 'p@p.hu')
        self.assertTrue(
            hasattr(user, 'is_active') and callable(getattr(user, 'is_active'))
        )

        active = user.is_active()
        self.assertTrue(active)

        user.active = False

        active = user.is_active()
        self.assertFalse(active)

if __name__ == '__main__':
    result = unittest.main()
