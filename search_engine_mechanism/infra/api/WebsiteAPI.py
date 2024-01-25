import sqlite3
from datetime import datetime


def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class WebsiteAPI:
    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def insert_new_website(self, website_id, website_url, seniority):
        date_created = get_current_datetime()
        website_data = (website_id, website_url, date_created, seniority)

        try:
            self.cursor.execute('''
                INSERT INTO websites (id, url, date_created, seniority)
                VALUES (?, ?, ?, ?)
            ''', website_data)

            self.conn.commit()
            print(f"Website {website_url} inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting website: {str(e)}")
        finally:
            self.conn.close()

    def get_all_websites(self):
        try:
            self.cursor.execute('SELECT * FROM websites')
            columns = [column[0] for column in self.cursor.description]
            websites = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
            return websites
        except sqlite3.Error as e:
            print(f"Error fetching all websites: {str(e)}")
        finally:
            self.conn.close()
