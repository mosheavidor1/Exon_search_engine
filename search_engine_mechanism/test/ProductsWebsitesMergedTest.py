import pytest
from search_engine_mechanism.actions.TestDatabaseUpdaterAndMerge import TestDatabaseUpdaterAndMerge


# This test will print merged products and their websites , table of products and websites
# located in /infra/api/example.db
class ProductsWebsitesMergedTest:
    @pytest.fixture
    def website_product_merge_instance(self):
        test_database_updater_and_merge = TestDatabaseUpdaterAndMerge()

        test_database_updater_and_merge.clear_website_product_merge()

        merged_data = test_database_updater_and_merge.merge_products_with_websites()
        test_database_updater_and_merge.insert_into_website_product_merge(merged_data)

        test_database_updater_and_merge.commit_and_close()

        return test_database_updater_and_merge

    def test_website_product_merge(self, website_product_merge_instance):
        assert len(website_product_merge_instance.merge_products_with_websites()) > 0


if __name__ == "__main__":
    pytest.main(["-v", "test_file_name.py"])
