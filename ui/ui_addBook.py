# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addBook.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QWidget)

class Ui_AddBook(object):
    def setupUi(self, AddBook):
        if not AddBook.objectName():
            AddBook.setObjectName(u"AddBook")
        AddBook.resize(421, 291)
        AddBook.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(AddBook)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_title = QLabel(AddBook)
        self.label_title.setObjectName(u"label_title")

        self.gridLayout.addWidget(self.label_title, 1, 0, 1, 1)

        self.label_author = QLabel(AddBook)
        self.label_author.setObjectName(u"label_author")

        self.gridLayout.addWidget(self.label_author, 2, 0, 1, 1)

        self.label_status = QLabel(AddBook)
        self.label_status.setObjectName(u"label_status")

        self.gridLayout.addWidget(self.label_status, 5, 0, 1, 1)

        self.line_author = QLineEdit(AddBook)
        self.line_author.setObjectName(u"line_author")
        self.line_author.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.line_author, 2, 1, 1, 1)

        self.label_cover = QLabel(AddBook)
        self.label_cover.setObjectName(u"label_cover")

        self.gridLayout.addWidget(self.label_cover, 0, 0, 1, 1)

        self.line_series = QLineEdit(AddBook)
        self.line_series.setObjectName(u"line_series")
        self.line_series.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.line_series, 3, 1, 1, 1)

        self.frame = QFrame(AddBook)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 24))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_cover = QLineEdit(self.frame)
        self.line_cover.setObjectName(u"line_cover")
        self.line_cover.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_2.addWidget(self.line_cover)

        self.toolbutton_cover = QToolButton(self.frame)
        self.toolbutton_cover.setObjectName(u"toolbutton_cover")
        self.toolbutton_cover.setMinimumSize(QSize(70, 0))
        self.toolbutton_cover.setMaximumSize(QSize(70, 24))

        self.horizontalLayout_2.addWidget(self.toolbutton_cover)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.line_genre = QLineEdit(AddBook)
        self.line_genre.setObjectName(u"line_genre")
        self.line_genre.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.line_genre, 4, 1, 1, 1)

        self.label_series = QLabel(AddBook)
        self.label_series.setObjectName(u"label_series")

        self.gridLayout.addWidget(self.label_series, 3, 0, 1, 1)

        self.line_title = QLineEdit(AddBook)
        self.line_title.setObjectName(u"line_title")
        self.line_title.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.line_title, 1, 1, 1, 1)

        self.label_genre = QLabel(AddBook)
        self.label_genre.setObjectName(u"label_genre")

        self.gridLayout.addWidget(self.label_genre, 4, 0, 1, 1)

        self.label_notes = QLabel(AddBook)
        self.label_notes.setObjectName(u"label_notes")

        self.gridLayout.addWidget(self.label_notes, 6, 0, 1, 1)

        self.frame_2 = QFrame(AddBook)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_add = QPushButton(self.frame_2)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setCheckable(True)

        self.horizontalLayout.addWidget(self.button_add)

        self.button_cancel = QPushButton(self.frame_2)
        self.button_cancel.setObjectName(u"button_cancel")

        self.horizontalLayout.addWidget(self.button_cancel)


        self.gridLayout.addWidget(self.frame_2, 7, 1, 1, 1)

        self.combo_status = QComboBox(AddBook)
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.setObjectName(u"combo_status")

        self.gridLayout.addWidget(self.combo_status, 5, 1, 1, 1)

        self.text_notes = QPlainTextEdit(AddBook)
        self.text_notes.setObjectName(u"text_notes")

        self.gridLayout.addWidget(self.text_notes, 6, 1, 1, 1)

        QWidget.setTabOrder(self.line_cover, self.toolbutton_cover)
        QWidget.setTabOrder(self.toolbutton_cover, self.line_title)
        QWidget.setTabOrder(self.line_title, self.line_author)
        QWidget.setTabOrder(self.line_author, self.line_series)
        QWidget.setTabOrder(self.line_series, self.line_genre)
        QWidget.setTabOrder(self.line_genre, self.combo_status)
        QWidget.setTabOrder(self.combo_status, self.text_notes)
        QWidget.setTabOrder(self.text_notes, self.button_add)
        QWidget.setTabOrder(self.button_add, self.button_cancel)

        self.retranslateUi(AddBook)

        QMetaObject.connectSlotsByName(AddBook)
    # setupUi

    def retranslateUi(self, AddBook):
        AddBook.setWindowTitle(QCoreApplication.translate("AddBook", u"Add Book", None))
        self.label_title.setText(QCoreApplication.translate("AddBook", u"Title", None))
        self.label_author.setText(QCoreApplication.translate("AddBook", u"Author", None))
        self.label_status.setText(QCoreApplication.translate("AddBook", u"Status", None))
        self.label_cover.setText(QCoreApplication.translate("AddBook", u"Cover", None))
        self.line_cover.setPlaceholderText(QCoreApplication.translate("AddBook", u"Select book cover", None))
        self.toolbutton_cover.setText(QCoreApplication.translate("AddBook", u"Image", None))
        self.label_series.setText(QCoreApplication.translate("AddBook", u"Series", None))
        self.label_genre.setText(QCoreApplication.translate("AddBook", u"Genre", None))
        self.label_notes.setText(QCoreApplication.translate("AddBook", u"Notes", None))
        self.button_add.setText(QCoreApplication.translate("AddBook", u"Add", None))
        self.button_cancel.setText(QCoreApplication.translate("AddBook", u"Cancel", None))
        self.combo_status.setItemText(0, QCoreApplication.translate("AddBook", u"Backlog", None))
        self.combo_status.setItemText(1, QCoreApplication.translate("AddBook", u"In Progress", None))
        self.combo_status.setItemText(2, QCoreApplication.translate("AddBook", u"Completed", None))

    # retranslateUi

