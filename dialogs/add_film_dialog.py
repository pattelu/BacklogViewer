from ui.ui_addFilm import Ui_AddFilm
import sqlite3
from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QPlainTextEdit,
    QLineEdit,
    QMessageBox,
)
from database import Database


class AddFilm(QDialog, Ui_AddFilm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Add and Cancel buttons
        self.button_add.clicked.connect(self.add_film)
        self.button_cancel.clicked.connect(self.cancel_add_film)

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

    def add_film(self):
        if self.mandatory_fields():
            blob_cover = Database.convert_to_blob(Database, self.line_cover.text())

            data = (
                blob_cover,
                self.line_title.text(),
                self.line_series.text(),
                self.line_genre.text(),
                self.line_type.text(),
                self.combo_status.currentText(),
                self.text_notes.toPlainText(),
            )
            Database.add_to_database(Database, "backlog.db", "sql_film", data)
            self.close()
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Fields required!")
            dlg.setText("Title is a mandatory field!")
            dlg.exec()

    def cancel_add_film(self):
        self.reject()
