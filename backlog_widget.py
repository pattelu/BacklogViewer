from ui.ui_backlog import Ui_Backlog
from PySide6.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QPushButton,
    QDialog,
    QHeaderView,
)
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QByteArray, Qt
from PySide6.QtSql import QSqlTableModel
import sqlite3
from add_game_dialog import AddGame
from add_book_dialog import AddBook
from add_film_dialog import AddFilm
import functools

# TDL
# Editing record in database
# Choose which columns should be displayed
# Info that game was added /removed / edited in database - bubble (QLabel, QWidget)
# Separete database logic in new file

games_header = [
    "ID",
    "Cover",
    "Title",
    "Developer",
    "Series",
    "Genre",
    "Platform",
    "Status",
    "Owned",
    "Notes",
]

books_header = [
    "ID",
    "Cover",
    "Title",
    "Author",
    "Series",
    "Genre",
    "Status",
    "Notes",
]

films_header = [
    "ID",
    "Cover",
    "Title",
    "Series",
    "Genre",
    "Type",
    "Status",
    "Notes",
]


class Backlog(QWidget, Ui_Backlog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Create database
        self.create_database("backlog.db")

        # Check if table is empty
        if self.check_if_table_is_empty("backlog.db", "to_play"):
            # Load data if not empty
            self.fetch_data("backlog.db", "to_play", self.table_game, games_header)
        if self.check_if_table_is_empty("backlog.db", "to_read"):
            # Load data if not empty
            self.fetch_data("backlog.db", "to_read", self.table_book, books_header)
        if self.check_if_table_is_empty("backlog.db", "to_watch"):
            # Load data if not empty
            self.fetch_data("backlog.db", "to_watch", self.table_film, films_header)

        # To Play tab
        self.button_add_game.clicked.connect(self.add_game)
        self.button_refresh_game.clicked.connect(
            functools.partial(
                self.fetch_data, "backlog.db", "to_play", self.table_game, games_header
                )
        )
        self.button_remove_game.clicked.connect(
            functools.partial(
                self.remove_from_db, "backlog.db", "to_play", self.table_game, games_header
            )
        )

        # To Read tab
        self.button_add_book.clicked.connect(self.add_book)
        self.button_refresh_book.clicked.connect(
            functools.partial(
                self.fetch_data, "backlog.db", "to_read", self.table_book, books_header
                )
        )
        self.button_remove_book.clicked.connect(
            functools.partial(
                self.remove_from_db, "backlog.db", "to_read", self.table_book, books_header
            )
        )

        # To Watch tab
        self.button_add_film.clicked.connect(self.add_film)
        self.button_refresh_film.clicked.connect(
            functools.partial(
                self.fetch_data, "backlog.db", "to_watch", self.table_film, films_header
            )
        )
        self.button_remove_film.clicked.connect(
            functools.partial(
                self.remove_from_db, "backlog.db", "to_watch", self.table_film, films_header
            )
        )

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

    def check_if_table_is_empty(self, db_name, db_table_name):
        try:
            with sqlite3.connect(db_name) as conn:
                self.cursor = conn.cursor()
                self.cursor.execute(f"SELECT EXISTS (SELECT 1 FROM {db_table_name});")
                return self.cursor.fetchall()[0][0]
        except sqlite3.OperationalError as e:
            print("Failed with error:", e)

    def fetch_data(self, db_name, db_table_name, table_widget_name, header):
        try:
            with sqlite3.connect(db_name) as conn:
                self.cursor = conn.cursor()
                self.cursor.execute(f"SELECT * FROM {db_table_name}")
                self.display_table(
                    self.cursor.fetchall(), table_widget_name, header
                ).show()
        except sqlite3.OperationalError as e:
            print("Filed to open database:", e)

    def display_table(self, rows, table_widget_name, list_name):
        table_widget_name.setRowCount(len(rows))
        table_widget_name.setColumnCount(len(rows[0]))

        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                if isinstance(value, bytes):
                    pixmap = self.get_image_data_from_blob(value)
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

    def add_game(self):
        add_game_dlg = AddGame()
        add_game_dlg.exec()
        if add_game_dlg.button_add.isChecked():
            self.fetch_data("backlog.db", "to_play", self.table_game, games_header)

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

            self.fetch_data(db_name, db_table_name, table_widget_name, header)

    def add_book(self):
        add_book_dlg = AddBook()
        add_book_dlg.exec()
        if add_book_dlg.button_add.isChecked():
            self.fetch_data("backlog.db", "to_read", self.table_book, books_header)

    def add_film(self):
        add_film_dlg = AddFilm()
        add_film_dlg.exec()
        a = add_film_dlg.result()
        print(a)
        if add_film_dlg.button_add.isChecked():
            self.fetch_data("backlog.db", "to_watch", self.table_film, films_header)
