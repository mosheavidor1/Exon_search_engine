import sqlite3
from datetime import datetime

from search_engine_mechanism.infra.api.DatabaseUpdater import database_path


class WebsiteProductMerge:
    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def merge_products_with_websites(self):
        self.cursor.execute('''
            SELECT p.id AS product_id, p.name AS product_name, wp.website_id, wp.product_page_unique_url, wp.date_created AS website_date_created
            FROM products p
            INNER JOIN website_products wp ON p.id = wp.product_id
        ''')
        return self.cursor.fetchall()

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()


class RankingMechanism:
    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def get_ranking_parameters(self):
        self.cursor.execute('''
            SELECT id, name, priority, grade_per_unit, date_created
            FROM ranking_parameters
        ''')
        return self.cursor.fetchall()

    def search_rank(self):
        website_product_merge = WebsiteProductMerge(database_path)
        merged_products = website_product_merge.merge_products_with_websites()

        ranking_parameters = self.get_ranking_parameters()

        # Perform the sorting (ranking) of products based on priority (seniority, keywords, references)
        # Assuming seniority is determined by the time of product and website update
        sorted_products = sorted(merged_products, key=lambda x: (
            datetime.strptime(x[4], "%Y-%m-%d %H:%M:%S"),  # Seniority (website_date_created)
            len(x[1].split()),  # Keywords (number of keywords in product name)
            x[3]  # References (assuming x[3] represents references)
        ), reverse=True)  # Reverse to have higher rank at the top

        # For demonstration purposes, just printing the sorted products
        print("Sorted Products:")
        for product in sorted_products:
            print(product)

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()



