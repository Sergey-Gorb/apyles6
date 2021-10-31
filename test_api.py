import unittest
import api


class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_document_existence(self):
        """
        Test that document existence
        """
        result = api.check_document_existence('10006')
        self.assertEqual(result, True)

    def test_remove_doc_from_shelf(self):
        """
        Test that shelf existence
        """
        result = api.remove_doc_from_shelf('11111')
        self.assertEqual(result, False)

    def test_get_doc_shelf(self):
        """
        Test  that document is on shelf
        """
        result = api.get_doc_shelf('10006')
        self.assertNotEqual(result, '2')

    def test_append_doc_to_shelf(self):
        """
        Test append document on shelf
        """
        result = api.append_doc_to_shelf('10006', '1')
        self.assertTrue(result)

    def test_delete_doc(self):
        """
        Test verified document info
        """
        result = api.delete_doc('11-2')
        self.assertEqual(result, True)





if __name__ == '__main__':
    unittest.main()