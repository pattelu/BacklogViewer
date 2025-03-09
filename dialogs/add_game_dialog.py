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

# from widgets.backlog_widget import Backlog


class AddGame(QDialog, Ui_AddGame):
    def __init__(self, button_name="Add", table_widget_name=None, column_name=None):
        super().__init__()
        self.setupUi(self)

        self.table_widget_name = table_widget_name
        self.column_name = column_name

        if button_name != "Add":
            self.button_add.setText(button_name)
            self.button_add.clicked.connect(
                self.edit_game(lambda: table_widget_name, column_name)
            )
        else:
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
            blob_cover = Database.convert_to_blob(Database, self.line_cover.text())

            if self.checkbox_owned.isChecked():
                owned = "Yes"
            else:
                owned = "No"

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

            Database.add_to_database(Database, "backlog.db", "sql_game", data)
            self.close()
        else:
            self.button_add.setChecked(False)
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Fields required!")
            dlg.setText("Title is a mandatory field!")
            dlg.exec()

    def cancel_add_game(self):
        self.reject()
