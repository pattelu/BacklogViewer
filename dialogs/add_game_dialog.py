from ui.ui_addGame import Ui_AddGame
import sqlite3
from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QPlainTextEdit,
    QLineEdit,
    QMessageBox,
)

from database import Database

# from PySide6.QtGui import QIntValidator


class AddGame(QDialog, Ui_AddGame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Add and Cancel buttons
        self.button_add.clicked.connect(self.add_game)
        self.button_cancel.clicked.connect(self.cancel_add_game)

        # Add Cover button - Open File
        self.toolbutton_cover.clicked.connect(self.add_cover)

    def add_cover(self):
        # Cover
        cover_path = QFileDialog.getOpenFileName(
            self, "Select Cover", "", "Image (*.png *.jpg *jpeg *.bmp *.gif)"
        )
        self.line_cover.setText(cover_path[0])

    def mandatory_fields(self):
        if self.line_title.text() == "":
            return False
        else:
            return True

    def add_game(self):
        if self.mandatory_fields():
            Database.add_to_database(self, "backlog.db", "sql_game", "game_data", True)
            self.close()
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Fields required!")
            dlg.setText("Title is a mandatory field!")
            dlg.exec()

    def cancel_add_game(self):
        self.reject()
