#!/usr/bin/env python3
"""Test client module"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient function"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", return_value={"key": "value"})
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org"""
        client = GithubOrgClient(org_name)

        result = client.org
        self.assertEqual(result, {"key": "value"})

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")


if __name__ == "__main__":
    unittest.main()
