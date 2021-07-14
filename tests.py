from count_some import count_some
from unittest import TestCase
import unittest

class checkingCountSomeTests(TestCase):

    def positive_numbers_only(self):
        starting_num = 5
        ending_num = 50
        k = 5
        self.assertTrue(count_some(starting_num, ending_num, k), msg='Function Works with Positive Digits')