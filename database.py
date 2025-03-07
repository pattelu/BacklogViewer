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

        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def create_database(self, db_name):
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
        try:
            with sqlite3.connect(db_name) as conn:
                self.cursor = conn.cursor()
                for statement in sql_statements:
                    self.cursor.execute(statement)
                conn.commit()
        except sqlite3.OperationalError as e:
            print("Failed to create tables:", e)

    def fetch_data(self, db_name, db_table_name, table_widget_name, header):
        try:
            with sqlite3.connect(db_name) as conn:
                self.cursor = conn.cursor()
                self.cursor.execute(f"SELECT * FROM {db_table_name}")
                Database.display_table(
                    self, self.cursor.fetchall(), table_widget_name, header
                ).show()
        except sqlite3.OperationalError as e:
            print("Filed to open database:", e)

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
            with sqlite3.connect(db_name) as conn:
                self.cursor = conn.cursor()
                self.cursor.execute(f"SELECT EXISTS (SELECT 1 FROM {db_table_name});")
                return self.cursor.fetchall()[0][0]
        except sqlite3.OperationalError as e:
            print("Failed with error:", e)

    def add_to_database(self, db_name, sql_name, sql_data, owned=False):
        blob_cover = Database.convert_to_blob(self, self.line_cover.text())

        if owned:
            if self.checkbox_owned.isChecked():
                owned = "Yes"
            else:
                owned = "No"

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

        if sql_data == "game_data":
            data = (
                blob_cover,
                self.line_title.text(),
                self.line_developer.text(),
                self.line_series.text(),
                self.line_genre.text(),
                self.line_platform.text(),
                self.combo_status.currentText(),
                owned,
                self.text_notes.toPlainText(),
            )
        elif sql_data == "book_data":
            data = (
                blob_cover,
                self.line_title.text(),
                self.line_author.text(),
                self.line_series.text(),
                self.line_genre.text(),
                self.combo_status.currentText(),
                self.text_notes.toPlainText(),
            )
        elif sql_data == "film_data":
            data = (
                blob_cover,
                self.line_title.text(),
                self.line_series.text(),
                self.line_genre.text(),
                self.line_type.text(),
                self.combo_status.currentText(),
                self.text_notes.toPlainText(),
            )
        else:
            print("Wrong sql_data")

        try:
            with sqlite3.connect(db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
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
                with sqlite3.connect(db_name) as conn:
                    self.cursor = conn.cursor()
                    self.cursor.execute(sql_remove, (record_id,))
                    conn.commit()
            except sqlite3.OperationalError as e:
                print("Failed to create tables:", e)

            Database.fetch_data(self, db_name, db_table_name, table_widget_name, header)

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
