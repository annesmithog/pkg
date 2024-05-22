from unittest import TestCase
from pkg.main import *
import sys
import io

class TestMain(TestCase):
    def test_fuck(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        fuck()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), 'Fuck Python\n')

    def test_get_fuck(self):
        self.assertEqual(get_fuck(), 'Fuck')