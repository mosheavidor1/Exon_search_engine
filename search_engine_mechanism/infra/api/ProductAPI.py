import sqlite3
from datetime import datetime


class ProductAPI:
    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def insert_new_product(self, product_id, product_name, product_description, product_keywords):
        date_created = self.get_current_datetime()
        product_data = (product_id, product_name, product_description, product_keywords, date_created)

        try:
            self.cursor.execute('''
                INSERT INTO products (id, name, description, keywords, date_created)
                VALUES (?, ?, ?, ?, ?)
            ''', product_data)

            self.conn.commit()
            print(f"Product {product_name} inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting product: {str(e)}")
        finally:
            self.conn.close()

    def get_current_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

