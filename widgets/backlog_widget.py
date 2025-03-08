from ui.ui_backlog import Ui_Backlog
from database import Database
from dialogs.add_game_dialog import AddGame
from dialogs.add_book_dialog import AddBook
from dialogs.add_film_dialog import AddFilm

from PySide6.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QPushButton,
    QDialog,
    QHeaderView,
)

import sys


# TDL
# Important
#   Editing record in database (METHOD 1 and editing cover by drag and drop (?))
#   Info that record was added /removed / edited in database and that id is not allowed to changes, so changes was not saved - bubble (QLabel, QWidget)
#   After remove, check if table is empty
# Optional
#   Choose which columns should be displayed


class Backlog(QWidget, Ui_Backlog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Headers
        self.games_header = [
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
        self.books_header = [
            "ID",
            "Cover",
            "Title",
            "Author",
            "Series",
            "Genre",
            "Status",
            "Notes",
        ]

        self.films_header = [
            "ID",
            "Cover",
            "Title",
            "Series",
            "Genre",
            "Type",
            "Status",
            "Notes",
        ]
        # End of headers

        # Columns name
        self.columns_game = [
            "cover",
            "title",
            "developer",
            "series",
            "genre",
            "platform",
            "status",
            "owned",
            "notes",
        ]
        self.columns_book = [
            "cover",
            "title",
            "author",
            "series",
            "genre",
            "status",
            "notes",
        ]
        self.columns_film = [
            "cover",
            "title",
            "series",
            "genre",
            "type",
            "status",
            "notes",
        ]
        # Columns name end

        # Create database
        Database.create_database(Database, "backlog.db")

        # Refresh data from table
        self.refresh_data("backlog.db", "to_play", self.table_game, self.games_header)
        self.refresh_data("backlog.db", "to_read", self.table_book, self.books_header)
        self.refresh_data("backlog.db", "to_watch", self.table_film, self.films_header)

        self.table_game.cellChanged.connect(
            lambda row, column: self.edit_cell(
                row, column, "backlog.db", "to_play", self.table_game, self.columns_game
            )
        )
        self.table_book.cellChanged.connect(
            lambda row, column: self.edit_cell(
                row, column, "backlog.db", "to_read", self.table_book, self.columns_book
            )
        )
        self.table_film.cellChanged.connect(
            lambda row, column: self.edit_cell(
                row,
                column,
                "backlog.db",
                "to_watch",
                self.table_film,
                self.columns_film,
            )
        )

        # To Play tab
        self.button_add_game.clicked.connect(self.add_game)
        self.button_refresh_game.clicked.connect(
            lambda: self.refresh_data(
                "backlog.db", "to_play", self.table_game, self.games_header
            )
        )
        self.button_remove_game.clicked.connect(
            lambda: Database.remove_from_db(
                Database, "backlog.db", "to_play", self.table_game, self.games_header
            )
        )

        # To Read tab
        self.button_add_book.clicked.connect(self.add_book)
        self.button_refresh_book.clicked.connect(
            lambda: self.refresh_data(
                "backlog.db", "to_read", self.table_book, self.books_header
            )
        )
        self.button_remove_book.clicked.connect(
            lambda: Database.remove_from_db(
                Database, "backlog.db", "to_read", self.table_book, self.books_header
            )
        )

        # To Watch tab
        self.button_add_film.clicked.connect(self.add_film)
        self.button_refresh_film.clicked.connect(
            lambda: self.refresh_data(
                "backlog.db", "to_watch", self.table_film, self.films_header
            )
        )
        self.button_remove_film.clicked.connect(
            lambda: Database.remove_from_db(
                Database, "backlog.db", "to_watch", self.table_film, self.films_header
            )
        )

    # Check if table is empty and display data if not
    def refresh_data(self, db_name, db_table_name, table_widget_name, header):
        if Database.check_if_table_is_empty(Database, db_name, db_table_name):
            Database.display_table(
                self,
                Database.fetch_data(Database, db_name, db_table_name),
                table_widget_name,
                header,
            )

    # Open Add Game Dialog and refresh table
    def add_game(self):
        add_game_dlg = AddGame()
        add_game_dlg.exec()
        if add_game_dlg.button_add.isChecked():
            self.refresh_data(
                "backlog.db", "to_play", self.table_game, self.games_header
            )

    # Open Add Book Dialog and refresh table
    def add_book(self):
        add_book_dlg = AddBook()
        add_book_dlg.exec()
        if add_book_dlg.button_add.isChecked():
            self.refresh_data(
                "backlog.db", "to_read", self.table_book, self.books_header
            )

    # Open Add Film Dialog and refresh table
    def add_film(self):
        add_film_dlg = AddFilm()
        add_film_dlg.exec()
        if add_film_dlg.button_add.isChecked():
            self.refresh_data(
                "backlog.db", "to_watch", self.table_film, self.films_header
            )

    def edit_cell(
        self, row, column, db_name, db_table_name, table_widget_name, columns_name
    ):
        # METHOD 1
        # Select row
        # Press Edit Button
        # Open dialog to edit selected record
        # Add new data in dialago
        # Press button and update data

        # METHOD 2 - DONE
        # Edit value in cell
        # Update value in database

        # If id is edited, stop edition
        if column == 0:
            # Add bubble alert that value has not been saved to database
            return
        record_id = str(table_widget_name.item(row, 0).text())

        new_value = table_widget_name.item(row, column).text()

        column_name = columns_name[column - 1]

        Database.update_value_in_table(
            Database, db_name, db_table_name, column_name, record_id, new_value
        )
