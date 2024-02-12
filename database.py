import psycopg2

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
        )

    def find_files(self, filename, date):
        query = """
            SELECT * FROM files
            WHERE filename LIKE %s
            AND date = %s
        """
        args = (f"%{filename}%", date)
        cursor = self.connection.cursor()
        cursor.execute(query, args)
        return cursor.fetchall()

    def save_file(self, uuid, filename, file_content):
        query = """
            INSERT INTO files (uuid, filename, date, content)
            VALUES (%s, %s, CURRENT_DATE, %s)
        """
        args = (uuid, filename, file_content)
        cursor = self.connection.cursor()
        cursor.execute(query, args)
        self.connection.commit()

    def get_file(self, uuid):
        query = """
            SELECT filename, content FROM files
            WHERE uuid = %s
        """
        args = (uuid,)
        cursor = self.connection.cursor()
        cursor.execute(query, args)
        return cursor.fetchone()
