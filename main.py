import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from backlog_widget import Backlog

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Backlog()
    window.show()

    app.exec()
# end main
