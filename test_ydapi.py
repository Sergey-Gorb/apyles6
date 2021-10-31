import os
import ydapi
import sqlite3
import unittest


class TestYandexDisk(unittest.TestCase):
    """
    Test YandexDisk
    """
    def setUp(self):
        """
        Setup a YaDloader
        """
        token_yd = '...'
        self.uploader = ydapi.YaUploader(token_yd)

    def test_set_dest_path(self):
        """
        Tests that we can successfully update an artist's name
        """
        result = self.uploader.set_dest_path('images')
        self.assertEqual(result, (200, True))
        result = self.uploader.set_dest_path('photos')
        self.assertEqual(result, (200, True))
        result = self.uploader.set_dest_path('pdfs')
        self.assertEqual(result, (404, 201))

    def tearDown(self):
        pass