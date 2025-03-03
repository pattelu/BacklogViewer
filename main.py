import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QByteArray, Qt, QStringListModel

def main():
    app = QApplication()

    # Connect to Database
    rows = connect_to_db()

    # Display "to_play" table
    to_play = display_to_play(rows)
    to_play.show()


    # Exit application
    sys.exit(app.exec())

def connect_to_db():
    try:
        with sqlite3.connect("backlog.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM to_play")
            rows = cursor.fetchall()
            return rows
    except sqlite3.OperationalError as e:
        print("Filed to open database:", e)

def display_to_play(rows):
    table = QTableWidget()
    table.resize(1280, 720)

    table.setRowCount(len(rows))
    table.setColumnCount(len(rows[0]) - 1)

    for row_idx, row in enumerate(rows):
        for col_idx, value in enumerate(row[1:]):
            if isinstance(value, bytes):
                pixmap = get_image_data_from_blob(value)
                if pixmap:
                    image_label = QLabel()
                    image_label.setPixmap(pixmap.scaledToHeight(200, Qt.SmoothTransformation))
                    table.setCellWidget(row_idx, col_idx, image_label)
            else:
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
    
    name = ["Cover", "Title", "Series", "Series No.", "Platforms", "Genre", "Owned", "Status", "Notes"]

    table.setHorizontalHeaderLabels(name)
    table.resizeRowsToContents()
    table.resizeColumnsToContents()
    return table

# Change BLOB to image
def get_image_data_from_blob(blob_data):
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


if __name__ == "__main__":
    main()
# end main