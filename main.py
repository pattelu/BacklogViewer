import sys
from PySide6.QtWidgets import QApplication
from backlog import Backlog

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Backlog()
    window.show()

    app.exec()
# end main
