import requests


class InsertKeyWords:
    def __init__(self, search_term):
        self.search_term = search_term

    def getSearchTermOptions(self):
        api_key = 'YOUR_API_KEY'  # Replace with the actual API key
        search_engine_url = 'https://api.example.com/search'  # Replace with the actual search engine API endpoint

        params = {
            'api_key': api_key,
            'q': self.search_term,
        }

        try:
            response = requests.get(search_engine_url, params=params)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"Error: {str(e)}")
            return None


search_terms_to_test = ["python programming", "web development", "machine learning"]

for search_term in search_terms_to_test:
    searched_keywords = InsertKeyWords(search_term)
    search_results = searched_keywords.getSearchTermOptions()

    if search_results:
        print(f"Search results for '{search_term}':")
        for result in search_results:
            print(result)
    else:
        print(f"Failed to retrieve search results for '{search_term}'.")
    print("\n")
