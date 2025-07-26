#!/usr/bin/env python3
"""Test for access nested map in utils
"""
import unittest
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
"""class of Test Access Nested Map
"""
    def test_access_nested_map(self):
    """Access nested map test with paramenters
    """
        self.assertEqual(access_nested_map({'a': 1}, 'b'), 0)
    @parameterized.expand(["a", "b", "c"])
