from ui.ui_addFilm import Ui_AddFilm
import sqlite3
from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QPlainTextEdit,
    QLineEdit,
    QMessageBox,
)


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
            self.add_to_database("backlog.db")
            self.close()
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Fields required!")
            dlg.setText("Title is a mandatory field!")
            dlg.exec()

    def add_to_database(self, db_name):
        blob_cover = self.convert_to_blob(self.line_cover.text())

        sql = f"""
        INSERT INTO to_watch (cover, title, series, genre, type, status, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """

        film_data = (
            blob_cover,
            self.line_title.text(),
            self.line_series.text(),
            self.line_genre.text(),
            self.line_type.text(),
            self.combo_status.currentText(),
            self.text_notes.toPlainText(),
        )

        try:
            with sqlite3.connect(db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, film_data)
                conn.commit()
        except sqlite3.OperationalError as e:
            print("Failed with error:", e)

    def convert_to_blob(self, filename):
        try:
            with open(filename, "rb") as file:
                blob = file.read()
            return blob
        except Exception:
            return "No Cover"

    def cancel_add_film(self):
        self.reject()
