import unittest
from unittest.mock import patch
from search_engine_mechanism.infra.api.GetSearchTermsList import app


# If keyword resulting two results with same name , an error message will appear.
class SameKeywordTest(unittest.TestCase):

    @patch('search_engine_mechanism.infra.SearchTermsOption.SearchTermsOption.getSearchTermOptions')
    def test_duplicate_search_terms(self, mock_search_terms_option):
        app.testing = True
        client = app.test_client()

        # Simulate two values with the same name in the database
        mock_search_results = [
            {"option_value": "duplicate_term", "product_page_url": "somesiteproduct1.com"},
            {"option_value": "duplicate_term", "product_page_url": "somesiteproduct2.com"}
        ]
        mock_search_terms_option.return_value = mock_search_results

        response = client.get('/search?search_term=duplicate_term')

        # Ensure the response is as expected
        self.assertEqual(response.status_code, 400)  # Assuming 400 is used for duplicate entry error
        expected_response = {"status": "error",
                             "msg": "Value 'duplicate_term' already exists. Please choose another name."}
        self.assertDictEqual(response.get_json(), expected_response)


if __name__ == '__main__':
    unittest.main()
