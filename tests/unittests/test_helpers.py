# -*- coding: utf-8 -*-
from unittest import mock
from src import helpers

import unittest


def load(path):
    return {
        'key_1': [1, 2, 3, 4, 5],
        'key_2': ['a', 'b', 'c', 'd', 'e']
    }


class Helpers(unittest.TestCase):
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    @mock.patch('json.load', side_effect=load)
    def test_read_json(self, magic_0, magic_1):
        """Function aimed in testing the helpers.read_json function.
        Parameters
        ----------
        magic_0 : unittest.mock.MagicMock
            Mock for builtin.open() function.
        magic_1 : unittest.mock.MagicMock
            Mock for json.load() function.
        Returns
        -------
        """
        expected = {
            'key_1': [1, 2, 3, 4, 5],
            'key_2': ['a', 'b', 'c', 'd', 'e']
        }
        result = helpers.read_json(r"path")
        self.assertEqual(expected, result)
