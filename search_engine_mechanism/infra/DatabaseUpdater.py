import sqlite3
from datetime import datetime
from search_engine_mechanism.infra.constans.descriptions import ProductDescriptionsConstants

from search_engine_mechanism.infra.constans.products.ProductNamesConstants import ProductNamesConstants
from search_engine_mechanism.infra.constans.url.WebsiteUrlsConstants import WebsiteUrlsConstants


class DatabaseUpdater:
    def __init__(self, database_path, website_constants, product_constants, product_descriptions_constants):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()
        self.website_constants = website_constants
        self.product_constants = product_constants
        self.product_descriptions_constants = product_descriptions_constants

    def create_tables(self):
        # Create Websites table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Websites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                URL TEXT NOT NULL,
                date_created TEXT NOT NULL,
                seniority INTEGER
            )
        ''')

        # Create Products table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                keywords TEXT,
                date_created TEXT NOT NULL
            )
        ''')

    def update_websites_table(self):
        websites_data = [
            (self.website_constants.ABC_STORE, self.get_current_datetime(), 1),
            (self.website_constants.GLOBAL_STORE, self.get_current_datetime(), 2),
            (self.website_constants.OUR_TV_STORE, self.get_current_datetime(), 3),
            (self.website_constants.ELECTRIC_SHOP, self.get_current_datetime(), 4),
            (self.website_constants.BEST_BUYING, self.get_current_datetime(), 5),
        ]

        self.cursor.executemany('''
            INSERT OR REPLACE INTO Websites (URL, date_created, seniority)
            VALUES (?, ?, ?)
        ''', websites_data)

    def update_products_table(self):
        products_data = [
            (self.product_constants.SONY_TV_55, self.product_descriptions_constants.SONY_TV_55, "electronics, TV",
             self.get_current_datetime()),
            (self.product_constants.TV_SAMSUNG_75, self.product_descriptions_constants.TV_SAMSUNG_75, "electronics, TV",
             self.get_current_datetime()),
            (self.product_constants.TV_LG_65, self.product_descriptions_constants.TV_LG_65, "electronics, TV",
             self.get_current_datetime()),
        ]

        self.cursor.executemany('''
            INSERT OR REPLACE INTO Products (name, description, keywords, date_created)
            VALUES (?, ?, ?, ?)
        ''', products_data)

    def get_current_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()


# Example usage
website_constants = WebsiteUrlsConstants()
product_constants = ProductNamesConstants()
product_descriptions_constants = ProductDescriptionsConstants

database_path = "example.db"  # Replace with the actual path to your SQLite database file
db_updater = DatabaseUpdater(database_path, website_constants, product_constants, product_descriptions_constants)
db_updater.create_tables()
db_updater.update_websites_table()
db_updater.update_products_table()
db_updater.commit_and_close()
