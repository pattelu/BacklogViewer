import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QByteArray, Qt, QStringListModel


def main():
    app = QApplication()

    # Create database
    create_database("backlog.db")

    # Check if table is empty
    if check_if_table_is_empty("backlog.db", "to_play"):
        # Fetch data
        rows = fetch_data("backlog.db", "to_play")
        # Display data in table
        to_play = display_to_play(rows)
        to_play.show()
    else:
        sys.exit("No data to display")

    # Exit application
    sys.exit(app.exec())


def create_database(db_name):
    sql_statements = [
        """CREATE TABLE IF NOT EXISTS "to_play" (
        "id"	INTEGER,
        "cover"	BLOB,
        "title"	TEXT NOT NULL,
        "series"	TEXT,
        "series_no"	INTEGER,
        "platforms"	TEXT,
        "genre"	TEXT,
        "owned"	INTEGER NOT NULL CHECK(owned IN (0, 1)),
        "status"	TEXT,
        "notes"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
        );""",
    ]
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Failed to create tables:", e)

def check_if_table_is_empty(db_name, table_name):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT EXISTS (SELECT 1 FROM {table_name});")
            return cursor.fetchall()[0][0]
    except sqlite3.OperationalError as e:
        print("Failed with error:", e)

def fetch_data(db_name, table_name):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            return rows
    except sqlite3.OperationalError as e:
        print("Filed to open database:", e)

def display_to_play(rows):
    table = QTableWidget()
    table.resize(1280, 720)

    table.setRowCount(len(rows))
    table.setColumnCount(len(rows[0]))

    for row_idx, row in enumerate(rows):
        for col_idx, value in enumerate(row):
            if isinstance(value, bytes):
                pixmap = get_image_data_from_blob(value)
                if pixmap:
                    image_label = QLabel()
                    image_label.setPixmap(pixmap.scaledToHeight(200, Qt.SmoothTransformation))
                    table.setCellWidget(row_idx, col_idx, image_label)
            else:
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
    
    name = ["ID", "Cover", "Title", "Series", "Series No.", "Platforms", "Genre", "Owned", "Status", "Notes"]

    table.setHorizontalHeaderLabels(name)
    table.verticalHeader().setVisible(False)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    return table

# Change BLOB to image
def get_image_data_from_blob(blob_data):
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


if __name__ == "__main__":
    main()
# end main