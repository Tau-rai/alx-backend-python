#!/usr/bin/env python3
"""Test utils module"""


import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
                        self, nested_map, path, expected_output):
        """Test access_nested_map function raises exception"""
        with self.assertRaises(expected_output):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json function"""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test memoize decorator"""

    def test_memoize(self):
        """Test memoize decorator"""
        from utils import memoize

        class TestClass:
            """Test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
   
        with patch.object(TestClass, 'a_method') as mock_method:
            test_object = TestClass()
            test_object.a_property
            test_object.a_property
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
