import sqlite3


class DifferentSeiorityValues:
    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def get_sorted_products_by_created_date(self):
        query = '''
            SELECT id, product_name, website_url, created_date
            FROM website_product_merge
            ORDER BY created_date DESC;  -- Sort in descending order
        '''
        self.cursor.execute(query)
        sorted_products = self.cursor.fetchall()
        return sorted_products

    def close_connection(self):
        self.conn.close()
