# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addGame.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)

class Ui_AddGame(object):
    def setupUi(self, AddGame):
        if not AddGame.objectName():
            AddGame.setObjectName(u"AddGame")
        AddGame.resize(534, 438)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddGame.sizePolicy().hasHeightForWidth())
        AddGame.setSizePolicy(sizePolicy)
        AddGame.setMaximumSize(QSize(16777215, 16777215))
        AddGame.setSizeGripEnabled(False)
        self.gridLayout = QGridLayout(AddGame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_platform = QLabel(AddGame)
        self.label_platform.setObjectName(u"label_platform")
        self.label_platform.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_platform, 5, 0, 1, 1)

        self.line_title = QLineEdit(AddGame)
        self.line_title.setObjectName(u"line_title")

        self.gridLayout.addWidget(self.line_title, 1, 1, 1, 1)

        self.line_platform = QLineEdit(AddGame)
        self.line_platform.setObjectName(u"line_platform")

        self.gridLayout.addWidget(self.line_platform, 5, 1, 1, 1)

        self.text_notes = QPlainTextEdit(AddGame)
        self.text_notes.setObjectName(u"text_notes")
        self.text_notes.setMaximumSize(QSize(16777215, 16777215))
        self.text_notes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.text_notes.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_notes.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_notes.setTabChangesFocus(True)

        self.gridLayout.addWidget(self.text_notes, 9, 1, 1, 1)

        self.label_status = QLabel(AddGame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_status, 8, 0, 1, 1)

        self.label_cover = QLabel(AddGame)
        self.label_cover.setObjectName(u"label_cover")
        self.label_cover.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_cover, 0, 0, 1, 1)

        self.frame = QFrame(AddGame)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 24))
        self.frame.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.line_cover = QLineEdit(self.frame)
        self.line_cover.setObjectName(u"line_cover")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_cover.sizePolicy().hasHeightForWidth())
        self.line_cover.setSizePolicy(sizePolicy2)
        self.line_cover.setMaximumSize(QSize(16777215, 24))
        self.line_cover.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.horizontalLayout.addWidget(self.line_cover)

        self.toolbutton_cover = QToolButton(self.frame)
        self.toolbutton_cover.setObjectName(u"toolbutton_cover")
        self.toolbutton_cover.setMaximumSize(QSize(70, 24))

        self.horizontalLayout.addWidget(self.toolbutton_cover)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.label_title = QLabel(AddGame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_title, 1, 0, 1, 1)

        self.line_series = QLineEdit(AddGame)
        self.line_series.setObjectName(u"line_series")

        self.gridLayout.addWidget(self.line_series, 3, 1, 1, 1)

        self.label_notes = QLabel(AddGame)
        self.label_notes.setObjectName(u"label_notes")
        self.label_notes.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_notes.setMargin(0)

        self.gridLayout.addWidget(self.label_notes, 9, 0, 1, 1)

        self.frame_2 = QFrame(AddGame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_add = QPushButton(self.frame_2)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setMaximumSize(QSize(100, 16777215))
        self.button_add.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_add.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_add)

        self.button_cancel = QPushButton(self.frame_2)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setMaximumSize(QSize(100, 16777215))
        self.button_cancel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_2.addWidget(self.button_cancel)


        self.gridLayout.addWidget(self.frame_2, 11, 1, 1, 1)

        self.label_series = QLabel(AddGame)
        self.label_series.setObjectName(u"label_series")
        self.label_series.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_series, 3, 0, 1, 1)

        self.label_developer = QLabel(AddGame)
        self.label_developer.setObjectName(u"label_developer")
        self.label_developer.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_developer, 2, 0, 1, 1)

        self.line_developer = QLineEdit(AddGame)
        self.line_developer.setObjectName(u"line_developer")
        self.line_developer.setMaximumSize(QSize(16777215, 24))
        self.line_developer.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)

        self.gridLayout.addWidget(self.line_developer, 2, 1, 1, 1)

        self.frame_3 = QFrame(AddGame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.combo_status = QComboBox(self.frame_3)
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.addItem("")
        self.combo_status.setObjectName(u"combo_status")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_status.sizePolicy().hasHeightForWidth())
        self.combo_status.setSizePolicy(sizePolicy3)
        self.combo_status.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.horizontalLayout_3.addWidget(self.combo_status)

        self.label_owned = QLabel(self.frame_3)
        self.label_owned.setObjectName(u"label_owned")
        sizePolicy1.setHeightForWidth(self.label_owned.sizePolicy().hasHeightForWidth())
        self.label_owned.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_owned)

        self.checkbox_owned = QCheckBox(self.frame_3)
        self.checkbox_owned.setObjectName(u"checkbox_owned")
        sizePolicy1.setHeightForWidth(self.checkbox_owned.sizePolicy().hasHeightForWidth())
        self.checkbox_owned.setSizePolicy(sizePolicy1)
        self.checkbox_owned.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_3.addWidget(self.checkbox_owned)


        self.gridLayout.addWidget(self.frame_3, 8, 1, 1, 1)

        self.label_genre = QLabel(AddGame)
        self.label_genre.setObjectName(u"label_genre")
        self.label_genre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_genre, 4, 0, 1, 1)

        self.line_genre = QLineEdit(AddGame)
        self.line_genre.setObjectName(u"line_genre")

        self.gridLayout.addWidget(self.line_genre, 4, 1, 1, 1)

        QWidget.setTabOrder(self.line_cover, self.toolbutton_cover)
        QWidget.setTabOrder(self.toolbutton_cover, self.line_title)
        QWidget.setTabOrder(self.line_title, self.line_developer)
        QWidget.setTabOrder(self.line_developer, self.line_series)
        QWidget.setTabOrder(self.line_series, self.line_genre)
        QWidget.setTabOrder(self.line_genre, self.line_platform)
        QWidget.setTabOrder(self.line_platform, self.combo_status)
        QWidget.setTabOrder(self.combo_status, self.checkbox_owned)
        QWidget.setTabOrder(self.checkbox_owned, self.text_notes)
        QWidget.setTabOrder(self.text_notes, self.button_add)
        QWidget.setTabOrder(self.button_add, self.button_cancel)

        self.retranslateUi(AddGame)

        QMetaObject.connectSlotsByName(AddGame)
    # setupUi

    def retranslateUi(self, AddGame):
        AddGame.setWindowTitle(QCoreApplication.translate("AddGame", u"Add Game", None))
        self.label_platform.setText(QCoreApplication.translate("AddGame", u"Platform", None))
        self.line_title.setPlaceholderText("")
        self.line_platform.setPlaceholderText("")
        self.text_notes.setPlainText("")
        self.label_status.setText(QCoreApplication.translate("AddGame", u"Status", None))
        self.label_cover.setText(QCoreApplication.translate("AddGame", u"Cover", None))
        self.line_cover.setPlaceholderText(QCoreApplication.translate("AddGame", u"Select game cover", None))
        self.toolbutton_cover.setText(QCoreApplication.translate("AddGame", u"Image", None))
        self.label_title.setText(QCoreApplication.translate("AddGame", u"Title", None))
        self.line_series.setPlaceholderText("")
        self.label_notes.setText(QCoreApplication.translate("AddGame", u"Notes", None))
        self.button_add.setText(QCoreApplication.translate("AddGame", u"Add", None))
        self.button_cancel.setText(QCoreApplication.translate("AddGame", u"Cancel", None))
        self.label_series.setText(QCoreApplication.translate("AddGame", u"Series", None))
        self.label_developer.setText(QCoreApplication.translate("AddGame", u"Developer", None))
        self.line_developer.setPlaceholderText("")
        self.combo_status.setItemText(0, QCoreApplication.translate("AddGame", u"Backlog", None))
        self.combo_status.setItemText(1, QCoreApplication.translate("AddGame", u"In Progress", None))
        self.combo_status.setItemText(2, QCoreApplication.translate("AddGame", u"Completed", None))
        self.combo_status.setItemText(3, QCoreApplication.translate("AddGame", u"Dropped", None))
        self.combo_status.setItemText(4, QCoreApplication.translate("AddGame", u"100%", None))

        self.label_owned.setText(QCoreApplication.translate("AddGame", u"Owned", None))
        self.checkbox_owned.setText("")
        self.label_genre.setText(QCoreApplication.translate("AddGame", u"Genre", None))
    # retranslateUi

