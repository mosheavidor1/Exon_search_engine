import unittest
from unittest.mock import patch
from search_engine_mechanism.infra.api.GetSearchTermsList import app


# This test will simulate a keyword searching and it's results .
class SearchKeywordTest(unittest.TestCase):

    @patch('search_engine_mechanism.infra.SearchTermsOption.SearchTermsOption.getSearchTermOptions')
    def test_search_terms(self, mock_search_terms_option):
        app.testing = True
        client = app.test_client()

        mock_search_results = [
            {"option_value": "option1", "product_page_url": "somesiteproduct1.com"},
            {"option_value": "option2", "product_page_url": "somesiteproduct2.com"}
        ]
        mock_search_terms_option.return_value = mock_search_results

        response = client.get('/search?search_term=test')

        # Ensure the response is as expected
        self.assertEqual(response.status_code, 200)
        expected_response = {
            "status": "success",
            "data": [
                {"option_value": "option1", "product_page_url": "somesiteproduct1.com"},
                {"option_value": "option2", "product_page_url": "somesiteproduct2.com"}
            ]
        }
        self.assertDictEqual(response.get_json(), expected_response)

    @patch('search_engine_mechanism.infra.SearchTermsOption.SearchTermsOption.getSearchTermOptions')
    def test_search_terms_no_results(self, mock_search_terms_option):
        app.testing = True
        client = app.test_client()

        mock_search_terms_option.return_value = []

        response = client.get('/search?search_term=test')

        self.assertEqual(response.status_code, 200)
        expected_response = {"status": "success", "data": [], "msg": "No Data Found"}
        self.assertDictEqual(response.get_json(), expected_response)


if __name__ == '__main__':
    unittest.main()
