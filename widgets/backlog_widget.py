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

import functools


# TDL
# Editing record in database
# Choose which columns should be displayed
# Info that game was added /removed / edited in database - bubble (QLabel, QWidget)


# Headers
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
# End of headers


class Backlog(QWidget, Ui_Backlog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Create database
        Database.create_database(Database, "backlog.db")

        # Refres data from table
        self.refresh_data("backlog.db", "to_play", self.table_game, games_header)
        self.refresh_data("backlog.db", "to_read", self.table_book, books_header)
        self.refresh_data("backlog.db", "to_watch", self.table_film, films_header)

        # To Play tab
        self.button_add_game.clicked.connect(self.add_game)
        self.button_refresh_game.clicked.connect(
            functools.partial(
                self.refresh_data,
                "backlog.db",
                "to_play",
                self.table_game,
                games_header,
            )
        )
        self.button_remove_game.clicked.connect(
            functools.partial(
                Database.remove_from_db,
                Database,
                "backlog.db",
                "to_play",
                self.table_game,
                games_header,
            )
        )

        # To Read tab
        self.button_add_book.clicked.connect(self.add_book)
        self.button_refresh_book.clicked.connect(
            functools.partial(
                self.refresh_data,
                "backlog.db",
                "to_read",
                self.table_book,
                books_header,
            )
        )
        self.button_remove_book.clicked.connect(
            functools.partial(
                Database.remove_from_db,
                Database,
                "backlog.db",
                "to_read",
                self.table_book,
                books_header,
            )
        )

        # To Watch tab
        self.button_add_film.clicked.connect(self.add_film)
        self.button_refresh_film.clicked.connect(
            functools.partial(
                self.refresh_data,
                "backlog.db",
                "to_watch",
                self.table_film,
                films_header,
            )
        )
        self.button_remove_film.clicked.connect(
            functools.partial(
                Database.remove_from_db,
                Database,
                "backlog.db",
                "to_watch",
                self.table_film,
                films_header,
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
            self.refresh_data("backlog.db", "to_play", self.table_game, games_header)

    # Open Add Book Dialog and refresh table
    def add_book(self):
        add_book_dlg = AddBook()
        add_book_dlg.exec()
        if add_book_dlg.button_add.isChecked():
            self.refresh_data("backlog.db", "to_read", self.table_book, books_header)

    # Open Add Film Dialog and refresh table
    def add_film(self):
        add_film_dlg = AddFilm()
        add_film_dlg.exec()
        if add_film_dlg.button_add.isChecked():
            self.refresh_data("backlog.db", "to_watch", self.table_film, films_header)
