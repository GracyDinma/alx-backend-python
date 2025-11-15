#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function in utils.py
This module verifies that access_nested_map correctly retrieves
values from a nested dictionary with a sequence of keys.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the access_nested_map function.
    Ensures correct value retrieval from nested dictionaries.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that a KeyError is raised using assertRaises.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test suite for get_json and ensures retrieval of expected result.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns the expected JSON payload.
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
