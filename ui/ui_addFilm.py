# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addFilm.ui'
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

class Ui_AddFilm(object):
    def setupUi(self, AddFilm):
        if not AddFilm.objectName():
            AddFilm.setObjectName(u"AddFilm")
        AddFilm.resize(413, 291)
        self.gridLayout = QGridLayout(AddFilm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_title = QLineEdit(AddFilm)
        self.line_title.setObjectName(u"line_title")
        self.line_title.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.line_title, 1, 1, 1, 1)

        self.label_cover = QLabel(AddFilm)
        self.label_cover.setObjectName(u"label_cover")

        self.gridLayout.addWidget(self.label_cover, 0, 0, 1, 1)

        self.frame = QFrame(AddFilm)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.line_cover = QLineEdit(self.frame)
        self.line_cover.setObjectName(u"line_cover")
        self.line_cover.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout.addWidget(self.line_cover)

        self.toolbutton_cover = QToolButton(self.frame)
        self.toolbutton_cover.setObjectName(u"toolbutton_cover")
        self.toolbutton_cover.setMinimumSize(QSize(70, 0))

        self.horizontalLayout.addWidget(self.toolbutton_cover)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.label_notes = QLabel(AddFilm)
        self.label_notes.setObjectName(u"label_notes")

        self.gridLayout.addWidget(self.label_notes, 6, 0, 1, 1)

        self.text_notes = QPlainTextEdit(AddFilm)
        self.text_notes.setObjectName(u"text_notes")

        self.gridLayout.addWidget(self.text_notes, 6, 1, 1, 1)

        self.label_title = QLabel(AddFilm)
        self.label_title.setObjectName(u"label_title")

        self.gridLayout.addWidget(self.label_title, 1, 0, 1, 1)

        self.line_genre = QLineEdit(AddFilm)
        self.line_genre.setObjectName(u"line_genre")
        self.line_genre.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.line_genre, 3, 1, 1, 1)

        self.combo_status = QComboBox(AddFilm)
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.setObjectName(u"combo_status")
        self.combo_status.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.combo_status, 5, 1, 1, 1)

        self.label_series = QLabel(AddFilm)
        self.label_series.setObjectName(u"label_series")

        self.gridLayout.addWidget(self.label_series, 2, 0, 1, 1)

        self.line_series = QLineEdit(AddFilm)
        self.line_series.setObjectName(u"line_series")
        self.line_series.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.line_series, 2, 1, 1, 1)

        self.label_genre = QLabel(AddFilm)
        self.label_genre.setObjectName(u"label_genre")

        self.gridLayout.addWidget(self.label_genre, 3, 0, 1, 1)

        self.label_status = QLabel(AddFilm)
        self.label_status.setObjectName(u"label_status")

        self.gridLayout.addWidget(self.label_status, 5, 0, 1, 1)

        self.frame_2 = QFrame(AddFilm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_add = QPushButton(self.frame_2)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_add)

        self.button_cancel = QPushButton(self.frame_2)
        self.button_cancel.setObjectName(u"button_cancel")

        self.horizontalLayout_2.addWidget(self.button_cancel)


        self.gridLayout.addWidget(self.frame_2, 7, 1, 1, 1)

        self.label_type = QLabel(AddFilm)
        self.label_type.setObjectName(u"label_type")

        self.gridLayout.addWidget(self.label_type, 4, 0, 1, 1)

        self.line_type = QLineEdit(AddFilm)
        self.line_type.setObjectName(u"line_type")

        self.gridLayout.addWidget(self.line_type, 4, 1, 1, 1)

        QWidget.setTabOrder(self.line_cover, self.toolbutton_cover)
        QWidget.setTabOrder(self.toolbutton_cover, self.line_title)
        QWidget.setTabOrder(self.line_title, self.line_series)
        QWidget.setTabOrder(self.line_series, self.line_genre)
        QWidget.setTabOrder(self.line_genre, self.line_type)
        QWidget.setTabOrder(self.line_type, self.combo_status)
        QWidget.setTabOrder(self.combo_status, self.text_notes)
        QWidget.setTabOrder(self.text_notes, self.button_add)
        QWidget.setTabOrder(self.button_add, self.button_cancel)

        self.retranslateUi(AddFilm)

        QMetaObject.connectSlotsByName(AddFilm)
    # setupUi

    def retranslateUi(self, AddFilm):
        AddFilm.setWindowTitle(QCoreApplication.translate("AddFilm", u"Add Film", None))
        self.label_cover.setText(QCoreApplication.translate("AddFilm", u"Cover", None))
        self.line_cover.setPlaceholderText(QCoreApplication.translate("AddFilm", u"Select film cover", None))
        self.toolbutton_cover.setText(QCoreApplication.translate("AddFilm", u"Image", None))
        self.label_notes.setText(QCoreApplication.translate("AddFilm", u"Notes", None))
        self.label_title.setText(QCoreApplication.translate("AddFilm", u"Title", None))
        self.combo_status.setItemText(0, QCoreApplication.translate("AddFilm", u"Backlog", None))
        self.combo_status.setItemText(1, QCoreApplication.translate("AddFilm", u"In Progress", None))
        self.combo_status.setItemText(2, QCoreApplication.translate("AddFilm", u"Completed", None))

        self.label_series.setText(QCoreApplication.translate("AddFilm", u"Series", None))
        self.label_genre.setText(QCoreApplication.translate("AddFilm", u"Genre", None))
        self.label_status.setText(QCoreApplication.translate("AddFilm", u"Status", None))
        self.button_add.setText(QCoreApplication.translate("AddFilm", u"Add", None))
        self.button_cancel.setText(QCoreApplication.translate("AddFilm", u"Cancel", None))
        self.label_type.setText(QCoreApplication.translate("AddFilm", u"Type", None))
    # retranslateUi

