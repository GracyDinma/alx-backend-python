#!/usr/bin/env python3
"""
A test suite for github org client.
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from utils import get_json
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """This class implements the test_org method"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        This method test that the GithubOrgClient returns the correct value.
        """
        expected_response = {"payload": True}
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, expected_response)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct value"""

        mock_payload = {"repos_url": "https://api.github.com/orgs/{org}"}

        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = mock_payload
            client = GithubOrgClient("test-org")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/{org}"
            )

    @patch("client.GithubOrgClient.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that _public_repos_url return value of choice"""
        mock_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get_json.return_value = mock_payload

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_url:
            url = "https://api.github.com/orgs/testorg/repos"
            mock_url.return_value = url

            client = GithubOrgClient('testorg')
            repos = client.public_repos()

            self.assertEqual(repos, ["repo1", "repo2"])

            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(url)
