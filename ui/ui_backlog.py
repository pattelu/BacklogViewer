# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backlog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Backlog(object):
    def setupUi(self, Backlog):
        if not Backlog.objectName():
            Backlog.setObjectName(u"Backlog")
        Backlog.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Backlog.sizePolicy().hasHeightForWidth())
        Backlog.setSizePolicy(sizePolicy)
        Backlog.setMaximumSize(QSize(1280, 720))
        self.horizontalLayout_2 = QHBoxLayout(Backlog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(Backlog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_game = QWidget()
        self.tab_game.setObjectName(u"tab_game")
        self.horizontalLayout = QHBoxLayout(self.tab_game)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table_game = QTableWidget(self.tab_game)
        self.table_game.setObjectName(u"table_game")
        self.table_game.setDragEnabled(False)
        self.table_game.setAlternatingRowColors(True)
        self.table_game.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_game.setGridStyle(Qt.PenStyle.SolidLine)
        self.table_game.setSortingEnabled(True)
        self.table_game.horizontalHeader().setMinimumSectionSize(1)
        self.table_game.horizontalHeader().setDefaultSectionSize(100)
        self.table_game.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.table_game)

        self.frame = QFrame(self.tab_game)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_add_game = QPushButton(self.frame)
        self.button_add_game.setObjectName(u"button_add_game")
        self.button_add_game.setCheckable(False)

        self.verticalLayout.addWidget(self.button_add_game)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.button_remove_game = QPushButton(self.frame)
        self.button_remove_game.setObjectName(u"button_remove_game")

        self.verticalLayout.addWidget(self.button_remove_game)

        self.button_refresh_game = QPushButton(self.frame)
        self.button_refresh_game.setObjectName(u"button_refresh_game")

        self.verticalLayout.addWidget(self.button_refresh_game)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget.addTab(self.tab_game, "")
        self.tab_read = QWidget()
        self.tab_read.setObjectName(u"tab_read")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_read)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.table_book = QTableWidget(self.tab_read)
        self.table_book.setObjectName(u"table_book")
        self.table_book.setDragEnabled(False)
        self.table_book.setAlternatingRowColors(True)
        self.table_book.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_book.setGridStyle(Qt.PenStyle.SolidLine)
        self.table_book.setSortingEnabled(True)
        self.table_book.horizontalHeader().setMinimumSectionSize(1)
        self.table_book.horizontalHeader().setDefaultSectionSize(100)
        self.table_book.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_4.addWidget(self.table_book)

        self.frame_2 = QFrame(self.tab_read)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_add_book = QPushButton(self.frame_2)
        self.button_add_book.setObjectName(u"button_add_book")
        self.button_add_book.setCheckable(False)

        self.verticalLayout_2.addWidget(self.button_add_book)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.button_remove_book = QPushButton(self.frame_2)
        self.button_remove_book.setObjectName(u"button_remove_book")

        self.verticalLayout_2.addWidget(self.button_remove_book)

        self.button_refresh_book = QPushButton(self.frame_2)
        self.button_refresh_book.setObjectName(u"button_refresh_book")

        self.verticalLayout_2.addWidget(self.button_refresh_book)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab_read, "")
        self.tab_watch = QWidget()
        self.tab_watch.setObjectName(u"tab_watch")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_watch)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.table_film = QTableWidget(self.tab_watch)
        self.table_film.setObjectName(u"table_film")
        self.table_film.setDragEnabled(False)
        self.table_film.setAlternatingRowColors(True)
        self.table_film.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_film.setGridStyle(Qt.PenStyle.SolidLine)
        self.table_film.setSortingEnabled(True)
        self.table_film.horizontalHeader().setMinimumSectionSize(1)
        self.table_film.horizontalHeader().setDefaultSectionSize(100)
        self.table_film.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_5.addWidget(self.table_film)

        self.frame_3 = QFrame(self.tab_watch)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.button_add_film = QPushButton(self.frame_3)
        self.button_add_film.setObjectName(u"button_add_film")
        self.button_add_film.setCheckable(False)

        self.verticalLayout_3.addWidget(self.button_add_film)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.button_remove_film = QPushButton(self.frame_3)
        self.button_remove_film.setObjectName(u"button_remove_film")

        self.verticalLayout_3.addWidget(self.button_remove_film)

        self.button_refresh_film = QPushButton(self.frame_3)
        self.button_refresh_film.setObjectName(u"button_refresh_film")

        self.verticalLayout_3.addWidget(self.button_refresh_film)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab_watch, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Backlog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Backlog)
    # setupUi

    def retranslateUi(self, Backlog):
        Backlog.setWindowTitle(QCoreApplication.translate("Backlog", u"Backlog", None))
        self.button_add_game.setText(QCoreApplication.translate("Backlog", u"Add", None))
        self.pushButton.setText(QCoreApplication.translate("Backlog", u"Edit", None))
        self.button_remove_game.setText(QCoreApplication.translate("Backlog", u"Remove", None))
        self.button_refresh_game.setText(QCoreApplication.translate("Backlog", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_game), QCoreApplication.translate("Backlog", u"To Play", None))
        self.button_add_book.setText(QCoreApplication.translate("Backlog", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("Backlog", u"Edit", None))
        self.button_remove_book.setText(QCoreApplication.translate("Backlog", u"Remove", None))
        self.button_refresh_book.setText(QCoreApplication.translate("Backlog", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_read), QCoreApplication.translate("Backlog", u"To Read", None))
        self.button_add_film.setText(QCoreApplication.translate("Backlog", u"Add", None))
        self.pushButton_3.setText(QCoreApplication.translate("Backlog", u"Edit", None))
        self.button_remove_film.setText(QCoreApplication.translate("Backlog", u"Remove", None))
        self.button_refresh_film.setText(QCoreApplication.translate("Backlog", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_watch), QCoreApplication.translate("Backlog", u"To Watch", None))
    # retranslateUi

