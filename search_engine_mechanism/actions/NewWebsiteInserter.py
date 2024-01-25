from search_engine_mechanism.infra.api.WebsiteAPI import WebsiteAPI


class NewWebsiteInserter:
    def __init__(self, database_path, website_constants):
        self.website_api = WebsiteAPI(database_path)
        self.website_constants = website_constants

    def insert_new_website(self, url, seniority):
        date_created = get_current_datetime()

        # Check if the website with the given URL already exists
        existing_website = self.website_api.get_website_by_url(url)

        if existing_website:
            # Website already exists, update its information
            self.website_api.update_website(website_id=existing_website[0], website_url=url, date_created=date_created,
                                            available_products=None, keywords=None, references=None)
        else:
            # Website doesn't exist, insert a new record
            self.website_api.update_website(website_id=None, website_url=url, date_created=date_created,
                                            available_products=None, keywords=None, references=None)
