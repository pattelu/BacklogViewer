import sqlite3
from PySide6.QtWidgets import (
    QTableWidgetItem,
    QLabel,
    QHeaderView,
)
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QByteArray, Qt


class Database:
    def __init__(self):
        super().__init__()

        self.conn = None
        self.cursor = None
        self.connect_db()

    # Connect to database
    def connect_db(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Failed to connect db:", e)

    # Close connection to database
    def close_db(self):
        if self.conn:
            self.conn.close()

    # Create database with tables: to_play, to_read, to_watch
    def create_database(self, db_name):
        # SQL for creating tables in database
        sql_statements = [
            """CREATE TABLE IF NOT EXISTS "to_play" (
                "id"	INTEGER,
                "cover"	BLOB,
                "title"	TEXT NOT NULL,
                "developer" TEXT,
                "series"	TEXT,
                "genre"	TEXT,
                "platform"	TEXT,
                "status"	TEXT,
                "owned"	TEXT NOT NULL,
                "notes"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
            );""",
            """CREATE TABLE IF NOT EXISTS "to_read" (
                "id"	INTEGER,
                "cover"	BLOB,
                "title"	TEXT NOT NULL,
                "author"	TEXT NOT NULL,
                "series"	TEXT,
                "genre"	TEXT,
                "status"	TEXT,
                "notes"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
            );""",
            """CREATE TABLE IF NOT EXISTS "to_watch" (
                "id"	INTEGER,
                "cover"	BLOB,
                "title"	TEXT NOT NULL,
                "series"	TEXT,
                "genre"	TEXT,
                "type" TEXT,
                "status"	TEXT,
                "notes"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
            );""",
        ]

        # Creating database
        try:
            self.connect_db(self, db_name)
            for statement in sql_statements:
                self.cursor.execute(statement)
                self.conn.commit()
            self.close_db(self)
        except sqlite3.OperationalError as e:
            print("Filed to open database:", e)

    # Fetch data from database
    def fetch_data(self, db_name, db_table_name):
        try:
            self.connect_db(self, db_name)
            self.cursor.execute(f"SELECT * FROM {db_table_name}")
            rows = self.cursor.fetchall()
            self.close_db(self)
        except sqlite3.OperationalError as e:
            print("Filed to open database:", e)

        return rows

    def display_table(self, rows, table_widget_name, list_name):
        table_widget_name.setRowCount(len(rows))
        table_widget_name.setColumnCount(len(rows[0]))

        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                if isinstance(value, bytes):
                    pixmap = Database.get_image_data_from_blob(self, value)
                    if pixmap:
                        image_label = QLabel()
                        image_label.setPixmap(
                            pixmap.scaledToHeight(200, Qt.SmoothTransformation)
                        )
                        table_widget_name.setCellWidget(row_idx, col_idx, image_label)
                else:
                    table_widget_name.setItem(
                        row_idx, col_idx, QTableWidgetItem(str(value))
                    )

        table_widget_name.setHorizontalHeaderLabels(list_name)
        table_widget_name.resizeRowsToContents()
        table_widget_name.resizeColumnsToContents()
        table_widget_name.horizontalHeader().setSectionResizeMode(
            table_widget_name.columnCount() - 1, QHeaderView.Stretch
        )
        # table_widget_name.horizontalHeader().stretchLastSection()
        return table_widget_name

    def check_if_table_is_empty(self, db_name, db_table_name):
        try:
            self.connect_db(self, db_name)
            self.cursor.execute(f"SELECT EXISTS (SELECT 1 FROM {db_table_name});")
            result = self.cursor.fetchall()[0][0]
            self.close_db(self)
        except sqlite3.OperationalError as e:
            print("Failed with error:", e)

        return result

    def add_to_database(self, db_name, sql_name, sql_data):
        if sql_name == "sql_game":
            sql = f"""
            INSERT INTO to_play (cover, title, developer, series, genre, platform, status, owned, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
            """
        elif sql_name == "sql_book":
            sql = f"""
            INSERT INTO to_read (cover, title, author, series, genre, status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """
        elif sql_name == "sql_film":
            sql = f"""
            INSERT INTO to_watch (cover, title, series, genre, type, status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """
        else:
            print("Wrong sql_name")

        try:
            self.connect_db(self, db_name)
            self.cursor.execute(sql, sql_data)
            self.conn.commit()
            self.close_db(self)
        except sqlite3.OperationalError as e:
            print("Failed with error:", e)

    def update_value_in_table(
        self, db_name, db_table_name, column_name, record_id, new_value
    ):
        sql = f"""
        UPDATE {db_table_name}
        SET {column_name} = ?
        WHERE id = ?
        """
        try:
            self.connect_db(self, db_name)
            self.cursor.execute(sql, (new_value, record_id))
            self.conn.commit()
            self.close_db(self)
        except sqlite3.OperationalError as e:
            print("Failed with error:", e)

    def remove_from_db(self, db_name, db_table_name, table_widget_name, header):
        sql_remove = f"""
        DELETE FROM {db_table_name} WHERE id = ?
        """

        selected_row = table_widget_name.currentRow()
        if selected_row == -1:
            return  # Row is not selected
        else:
            record_id = str(table_widget_name.item(selected_row, 0).text())
            try:
                self.connect_db(self, db_name)
                self.cursor.execute(sql_remove, (record_id,))
                self.conn.commit()
                self.close_db(self)
            except sqlite3.OperationalError as e:
                print("Failed to create tables:", e)

        self.display_table(
            self,
            self.fetch_data(self, db_name, db_table_name),
            table_widget_name,
            header,
        )

    # Change Image to BLOB
    def convert_to_blob(self, filename):
        try:
            with open(filename, "rb") as file:
                blob = file.read()
            return blob
        except Exception:
            return "No Cover"

    # Change BLOB to Image
    def get_image_data_from_blob(self, blob_data):
        try:
            image = QPixmap()
            image.loadFromData(QByteArray(blob_data))
            if not image.isNull():
                return image
            else:
                return None
        except Exception as e:
            print(f"Error with loading image from BLBO: {e}")
            return None
