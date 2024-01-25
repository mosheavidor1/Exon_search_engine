
import unittest
import random

from search_engine_mechanism.infra.WebsiteProductMerge import WebsiteProductMerge
from search_engine_mechanism.infra.api.DatabaseUpdater import DatabaseUpdater
from search_engine_mechanism.infra.api.ProductAPI import ProductAPI
from search_engine_mechanism.infra.api.WebsiteAPI import WebsiteAPI
from search_engine_mechanism.infra.constans.DbPath import DbPath
from search_engine_mechanism.infra.constans.products.ProductNamesConstants import ProductNamesConstants
from search_engine_mechanism.infra.constans.url.WebsiteUrlsConstants import WebsiteUrlsConstants


class TestDatabaseUpdaterAndMerge(unittest.TestCase):
    def setUp(self):
        self.database_path = ( DbPath.DATABASE_PATH)

        self.website_constants = WebsiteUrlsConstants()
        self.product_constants = ProductNamesConstants()

        self.db_updater = DatabaseUpdater(
            self.database_path, self.website_constants, self.product_constants
        )

        # Create tables and insert initial data
        self.db_updater.create_tables()
        self.db_updater.update_websites_table()
        self.db_updater.update_products_table()
        self.db_updater.commit_and_close()

    def test_merge_products_with_websites(self):

        website_api = WebsiteAPI(self.database_path)
        product_api = ProductAPI(self.database_path)


        website_product_merge = WebsiteProductMerge(self.database_path, website_api, product_api)


        merged_data = website_product_merge.merge_products_with_websites()


        for entry in merged_data:
            print(entry)


        website_product_merge.commit_and_close()


        self.assertIsNotNone(merged_data)
        self.assertGreater(len(merged_data), 0)


if __name__ == '__main__':
    unittest.main()
