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
        Database.create_database(self, "backlog.db")

        # Check if table is empty
        if Database.check_if_table_is_empty(self, "backlog.db", "to_play"):
            # Load data if not empty
            Database.fetch_data(
                self, "backlog.db", "to_play", self.table_game, games_header
            )
        if Database.check_if_table_is_empty(self, "backlog.db", "to_read"):
            # Load data if not empty
            Database.fetch_data(
                self, "backlog.db", "to_read", self.table_book, books_header
            )
        if Database.check_if_table_is_empty(self, "backlog.db", "to_watch"):
            # Load data if not empty
            Database.fetch_data(
                self, "backlog.db", "to_watch", self.table_film, films_header
            )

        # To Play tab
        self.button_add_game.clicked.connect(self.add_game)
        self.button_refresh_game.clicked.connect(
            functools.partial(
                Database.fetch_data,
                self,
                "backlog.db",
                "to_play",
                self.table_game,
                games_header,
            )
        )
        self.button_remove_game.clicked.connect(
            functools.partial(
                Database.remove_from_db,
                self,
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
                Database.fetch_data,
                self,
                "backlog.db",
                "to_read",
                self.table_book,
                books_header,
            )
        )
        self.button_remove_book.clicked.connect(
            functools.partial(
                Database.remove_from_db,
                self,
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
                Database.fetch_data,
                self,
                "backlog.db",
                "to_watch",
                self.table_film,
                films_header,
            )
        )
        self.button_remove_film.clicked.connect(
            functools.partial(
                Database.remove_from_db,
                self,
                "backlog.db",
                "to_watch",
                self.table_film,
                films_header,
            )
        )

    def add_game(self):
        add_game_dlg = AddGame()
        add_game_dlg.exec()
        if add_game_dlg.button_add.isChecked():
            Database.fetch_data(
                self, "backlog.db", "to_play", self.table_game, games_header
            )

    def add_book(self):
        add_book_dlg = AddBook()
        add_book_dlg.exec()
        if add_book_dlg.button_add.isChecked():
            Database.fetch_data(
                self, "backlog.db", "to_read", self.table_book, books_header
            )

    def add_film(self):
        add_film_dlg = AddFilm()
        add_film_dlg.exec()
        if add_film_dlg.button_add.isChecked():
            Database.fetch_data(
                self, "backlog.db", "to_watch", self.table_film, films_header
            )
