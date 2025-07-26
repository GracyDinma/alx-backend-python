#!/usr/bin/env python3
"""Test for access nested map in utils
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock
import requests

class TestAccessNestedMap(unittest.TestCase):
    """class of Test Access Nested Map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Access nested map test with expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Assert raises context to test key error
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """class that test for JSON from remote url
    """

    @parameterized.expand([
        ("http://example.com", test_played={"payload": True}),
        ("http://holberton.io", test_payload={"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, url: str, expected, mock_get):
        """A method that test that utils.get_json
        returns expected result.
        """
        mock_get.return_value.json.return_value = {"test_played"}

if __name__ == "__main__":
    unittest.main()
