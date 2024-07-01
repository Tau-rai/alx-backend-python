#!/usr/bin/env python3
"""Test client module"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


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
        

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url"""
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/abc/repos"
            client = GithubOrgClient("abc")
            self.assertEqual(client._public_repos_url,
                             "https://api.github.com/orgs/abc/repos")


    @patch("client.get_json", return_value=[{"name": "repo1"}])
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos"""
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/abc/repos"
            client = GithubOrgClient("abc")
            
            self.assertEqual(client.public_repos(), ["repo1"])
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/abc/repos")


    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
