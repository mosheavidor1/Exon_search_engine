import sqlite3
from datetime import datetime


class WebsiteProductMerge:
    def __init__(self, database_path, website_api):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()
        self.website_api = website_api

    def merge_products_with_websites(self):
        self.cursor.execute('''
            SELECT p.id AS product_id, p.name AS product_name, wp.website_id, wp.product_page_unique_url
            FROM products p
            INNER JOIN website_products wp ON p.id = wp.product_id
        ''')
        merged_data = self.cursor.fetchall()

        for entry in merged_data:
            product_id, product_name, website_id, product_page_url = entry

            # Get related keywords for the product from the product API
            keywords = self.get_related_keywords(product_id)

            # Update website information using WebsiteAPI
            self.update_website_info(website_id, product_page_url, keywords)

            print(
                f"Product ID: {product_id}, Product Name: {product_name}, Website ID: {website_id}, URL: {product_page_url}")

        return merged_data

    def get_related_keywords(self, product_id):
        # Assume you have a function in your product API to get related keywords
        # Replace this with the actual call to your product API
        return ["related", "keywords"]

    def update_website_info(self, website_id, website_url, keywords):
        date_created = self.get_current_datetime()

        # Assume you have additional data for the website (replace with actual data)
        available_products = 100
        references = 5

        # Call WebsiteAPI to update website information
        self.website_api.update_website(website_id, website_url, date_created, available_products, keywords, references)

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()

    def get_current_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
