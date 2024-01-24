import sqlite3
from datetime import datetime

class WebsiteAPI:
    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def update_website(self, website_id, website_url, date_created, available_products, keywords, references):
        try:
            self.cursor.execute('''
                UPDATE Websites
                SET URL=?, date_created=?, available_products=?, keywords=?, references=?
                WHERE id=?
            ''', (website_url, date_created, available_products, keywords, references, website_id))

            self.conn.commit()
            print(f"Website with ID {website_id} updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating website: {str(e)}")
        finally:
            self.conn.close()

    def get_current_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


