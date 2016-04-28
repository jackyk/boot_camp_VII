'''Test suite for super_sum.'''
from unittest import TestCase
from super_sum  import super_sum

class SuperSumTestCase(TestCase):
    '''Test Case for super_sum'''

    def test_empty_input(self):
        self.assertEqual(super_sum() ,0)

    def test_sum_of_integers(self):
        self.assertEqual(super_sum(1,2,3), 6)
        self.assertEqual(super_sum(-1,1), 0)
        self.assertNotEqual(super_sum(10.20,30), 100)

    def test_sum_of_items_in_one_list(self):
        self.assertEqual(super_sum([1,2,3]) ,6)

    def test_if_is_a_str(self):
        self.assertEqual(super_sum(), 0)
