import random
import sqlite3


class WebsiteProductMerge:
    def __init__(self, database_path, website_api, product_api):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()
        self.website_api = website_api
        self.product_api = product_api

    def merge_products_with_websites(self):
        # Fetch all products and websites
        all_products = self.product_api.get_all_products()
        all_websites = self.website_api.get_all_websites()

        # Randomly associate each product with a website
        merged_data = []
        for product in all_products:
            website = random.choice(all_websites)
            merged_entry = {'product_name': product['name'], 'website_url': website['URL']}
            merged_data.append(merged_entry)

        return merged_data

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()

