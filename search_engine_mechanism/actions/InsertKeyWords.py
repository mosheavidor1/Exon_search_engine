import requests
import sqlite3

class InsertKeyWords:
    def __init__(self, search_term, database_path):
        self.search_term = search_term
        self.database_path = database_path

    def getSearchTermOptions(self):
        api_key = 'YOUR_API_KEY'
        search_engine_url = 'https://api.example.com/search'
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

    def search_product_by_keyword(self):
        try:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()

            query = f"SELECT DISTINCT product_name FROM products WHERE product_name LIKE ?;"
            cursor.execute(query, ('%' + self.search_term + '%',))
            matching_products = cursor.fetchall()

            # Print the search results
            if matching_products:
                print(f"Search results for '{self.search_term}':")
                for product in matching_products:
                    print(product[0])
            else:
                print(f"No keyword matches found for '{self.search_term}'.")

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:

            conn.close()


database_path = r"/search_engine_mechanism/infra/api/example.db"


search_terms_to_test = ["python programming", "web development", "machine learning"]

for search_term in search_terms_to_test:
    searched_keywords = InsertKeyWords(search_term, database_path)
    searched_keywords.search_product_by_keyword()
    print("\n")
