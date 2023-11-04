from what_is_year_now import what_is_year_now
import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):

    @patch('urllib.request.urlopen')
    @patch('json.load')
    def test_format_YMD(self, mock_load, mock_urlopen):
        mock_load.return_value = {"currentDateTime": "2023-10-31T08:00:00Z"}
        year = what_is_year_now()
        self.assertEqual(year, 2023)

    @patch('urllib.request.urlopen')
    @patch('json.load')
    def test_format_DMY(self, mock_load, mock_urlopen):
        mock_load.return_value = {"currentDateTime": "31.10.2023T08:00:00Z"}
        year = what_is_year_now()
        self.assertEqual(year, 2023)

    @patch('urllib.request.urlopen')
    @patch('json.load')
    def test_invalid_format(self, mock_load, mock_urlopen):
        mock_load.return_value = {"currentDateTime": "2023/10/31T08:00:00Z"}
        with self.assertRaises(ValueError):
            what_is_year_now()

    @patch('urllib.request.urlopen')
    @patch('json.load')
    def test_unexpected_format(self, mock_load, mock_urlopen):
        mock_load.return_value = {"currentDateTime": "2023.10-31T08:00:00Z"}
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == "__main__":      # pragma: no cover
    pass
