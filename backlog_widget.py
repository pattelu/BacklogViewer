from ui.ui_backlog import Ui_Backlog
from PySide6.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QPushButton,
    QDialog,
    QHeaderView
)
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QByteArray, Qt
from PySide6.QtSql import QSqlTableModel
import sqlite3
from add_game_dialog import AddGame
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


class Backlog(QWidget, Ui_Backlog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_add_game.clicked.connect(self.add_game)
        self.button_refresh.clicked.connect(functools.partial(self.fetch_data, "backlog.db", "to_play", self.table_game))
        self.button_remove.clicked.connect(functools.partial(self.remove_game, "backlog.db", "to_play", self.table_game))

        # Create database
        self.create_database("backlog.db")

        # Check if table is empty
        if self.check_if_table_is_empty("backlog.db", "to_play"):
            # Load data if not empty
            self.fetch_data("backlog.db", "to_play", self.table_game)


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

    def fetch_data(self, db_name, db_table_name, table_widget_name):
        try:
            with sqlite3.connect(db_name) as conn:
                self.cursor = conn.cursor()
                self.cursor.execute(f"SELECT * FROM {db_table_name}")
                self.display_table(
                    self.cursor.fetchall(), table_widget_name, games_header
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
        table_widget_name.horizontalHeader().setSectionResizeMode(table_widget_name.columnCount() -1, QHeaderView.Stretch)
        #table_widget_name.horizontalHeader().stretchLastSection()
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
            self.fetch_data("backlog.db", "to_play", self.table_game)

    def remove_game(self, db_name, db_table_name, table_widget_name):
        sql_remove = f"""
        DELETE FROM {db_table_name} WHERE id = ?
        """

        selected_row = table_widget_name.currentRow()
        if selected_row == -1:
            return # Row is not selected
        else:
            record_id = str(table_widget_name.item(selected_row, 0).text())
            try:
                with sqlite3.connect(db_name) as conn:
                    self.cursor = conn.cursor()
                    self.cursor.execute(sql_remove, (record_id,))
                    conn.commit()
            except sqlite3.OperationalError as e:
                print("Failed to create tables:", e)

            self.fetch_data(db_name, db_table_name, table_widget_name)
        

