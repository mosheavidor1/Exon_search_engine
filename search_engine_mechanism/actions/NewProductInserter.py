from search_engine_mechanism.infra.api.ProductAPI import ProductAPI


class NewProductInserter:
    def __init__(self, database_path, product_constants, product_descriptions_constants):
        self.product_api = ProductAPI(database_path)
        self.product_constants = product_constants
        self.product_descriptions_constants = product_descriptions_constants

    def insert_new_product(self, name, description, keywords):
        product_id = self.generate_unique_product_id()

        self.product_api.insert_new_product(product_id, name, description, keywords)

    def generate_unique_product_id(self):
        pass
