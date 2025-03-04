from ui.ui_backlog import Ui_Backlog
from PySide6.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QPushButton,
)
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QByteArray, Qt
import sqlite3
from add_game import AddGame

# TDL
# Refresf database affter edition (add, remove, edit)
# Editing directly in table (?)


class Backlog(QWidget, Ui_Backlog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.add_game.clicked.connect(self.button_add_game)

        # Create database
        self.create_database("backlog.db")

        # Check if table is empty
        if self.check_if_table_is_empty("backlog.db", "to_play"):
            # Fetch data
            rows = self.fetch_data("backlog.db", "to_play")
            # Display data in table
            to_play = self.display_to_play(rows)
            to_play.show()
        else:
            sys.exit("No data to display")

    def create_database(self, db_name):
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
                self.cursor = conn.cursor()
                for statement in sql_statements:
                    self.cursor.execute(statement)
                conn.commit()
        except sqlite3.OperationalError as e:
            print("Failed to create tables:", e)

    def check_if_table_is_empty(self, db_name, table_name):
        try:
            with sqlite3.connect(db_name) as conn:
                self.cursor = conn.cursor()
                self.cursor.execute(f"SELECT EXISTS (SELECT 1 FROM {table_name});")
                return self.cursor.fetchall()[0][0]
        except sqlite3.OperationalError as e:
            print("Failed with error:", e)

    def fetch_data(self, db_name, table_name):
        try:
            with sqlite3.connect(db_name) as conn:
                self.cursor = conn.cursor()
                self.cursor.execute(f"SELECT * FROM {table_name}")
                rows = self.cursor.fetchall()
                return rows
        except sqlite3.OperationalError as e:
            print("Filed to open database:", e)

    def display_to_play(self, rows):
        self.table_game.setRowCount(len(rows))
        self.table_game.setColumnCount(len(rows[0]))

        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                if isinstance(value, bytes):
                    pixmap = self.get_image_data_from_blob(value)
                    if pixmap:
                        image_label = QLabel()
                        image_label.setPixmap(
                            pixmap.scaledToHeight(200, Qt.SmoothTransformation)
                        )
                        self.table_game.setCellWidget(row_idx, col_idx, image_label)
                else:
                    self.table_game.setItem(
                        row_idx, col_idx, QTableWidgetItem(str(value))
                    )

        name = [
            "ID",
            "Cover",
            "Title",
            "Series",
            "Series No.",
            "Platforms",
            "Genre",
            "Owned",
            "Status",
            "Notes",
        ]

        self.table_game.setHorizontalHeaderLabels(name)
        self.table_game.verticalHeader().setVisible(False)
        self.table_game.resizeRowsToContents()
        self.table_game.resizeColumnsToContents()
        return self.table_game

    # Change BLOB to image
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

    def button_add_game(self):
        self.add_game = AddGame()
        self.add_game.exec()
