from ui.ui_addGame import Ui_AddGame

from PySide6.QtWidgets import QDialog, QFileDialog, QPlainTextEdit, QLineEdit
from PySide6.QtGui import QIntValidator

class AddGame(QDialog, Ui_AddGame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Add and Cancel buttons
        self.button_add.clicked.connect(self.add_game)
        self.button_cancel.clicked.connect(self.cancel_add_game)
        
        # Cover button
        self.toolbutton_cover.clicked.connect(self.add_cover)

        # Limit "Series No."" filed only for digits
        self.line_series_no.setValidator(QIntValidator())


    def add_cover(self):
        # Cover
        cover_path = QFileDialog.getOpenFileName(self, "Select Cover", "", "Image (*.png *.jpg *jpeg *.bmp *.gif)")
        self.line_cover.setText(cover_path[0])

    def validate_data():
        ...

    def add_game(self):
        print("Successfully added game!")

    def cancel_add_game(self):
        self.reject()