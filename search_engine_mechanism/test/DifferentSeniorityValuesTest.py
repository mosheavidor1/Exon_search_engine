import sqlite3

import pytest


# This code will return a sorted list .
# The created table will be located in /test/test_example.db


class DifferentSeiorityValues:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def get_sorted_products_by_created_date(self, ascending=True):
        order = "ASC" if ascending else "DESC"
        query = f"SELECT * FROM website_product_merge ORDER BY created_date {order};"
        self.cursor.execute(query)
        sorted_products = self.cursor.fetchall()
        return sorted_products

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    pytest.main([__file__])
