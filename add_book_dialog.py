from ui.ui_addBook import Ui_AddBook
import sqlite3
from PySide6.QtWidgets import (
    QDialog,
    QFileDialog,
    QPlainTextEdit,
    QLineEdit,
    QMessageBox,
)


class AddBook(QDialog, Ui_AddBook):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Add and Cancel buttons
        self.button_add.clicked.connect(self.add_book)
        self.button_cancel.clicked.connect(self.cancel_add_book)

        # Add Cover button - Open File
        self.toolbutton_cover.clicked.connect(self.add_cover)

    def add_cover(self):
        # Cover
        cover_path = QFileDialog.getOpenFileName(
            self, "Select Cover", "", "Image (*.png *.jpg *jpeg *.bmp *.gif)"
        )
        self.line_cover.setText(cover_path[0])

    def mandatory_fields(self):
        if self.line_title.text() == "" or self.line_author == "":
            return False
        else:
            return True

    def add_book(self):
        if self.mandatory_fields():
            self.add_to_database("backlog.db")
            self.close()
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Fields required!")
            dlg.setText("Title and Author is a mandatory field!")
            dlg.exec()

    def add_to_database(self, db_name):
        blob_cover = self.convert_to_blob(self.line_cover.text())

        sql = f"""
        INSERT INTO to_read (cover, title, author, series, genre, status, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """

        book_data = (
            blob_cover,
            self.line_title.text(),
            self.line_author.text(),
            self.line_series.text(),
            self.line_genre.text(),
            self.combo_status.currentText(),
            self.text_notes.toPlainText(),
        )

        try:
            with sqlite3.connect(db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, book_data)
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

    def cancel_add_book(self):
        self.reject()
