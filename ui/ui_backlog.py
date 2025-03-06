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

        self.button_remove = QPushButton(self.frame)
        self.button_remove.setObjectName(u"button_remove")

        self.verticalLayout.addWidget(self.button_remove)

        self.button_refresh = QPushButton(self.frame)
        self.button_refresh.setObjectName(u"button_refresh")

        self.verticalLayout.addWidget(self.button_refresh)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget.addTab(self.tab_game, "")
        self.tab_watcb = QWidget()
        self.tab_watcb.setObjectName(u"tab_watcb")
        self.tabWidget.addTab(self.tab_watcb, "")
        self.tab_read = QWidget()
        self.tab_read.setObjectName(u"tab_read")
        self.tabWidget.addTab(self.tab_read, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Backlog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Backlog)
    # setupUi

    def retranslateUi(self, Backlog):
        Backlog.setWindowTitle(QCoreApplication.translate("Backlog", u"Backlog", None))
        self.button_add_game.setText(QCoreApplication.translate("Backlog", u"Add", None))
        self.pushButton.setText(QCoreApplication.translate("Backlog", u"Edit", None))
        self.button_remove.setText(QCoreApplication.translate("Backlog", u"Remove", None))
        self.button_refresh.setText(QCoreApplication.translate("Backlog", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_game), QCoreApplication.translate("Backlog", u"To Play", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_watcb), QCoreApplication.translate("Backlog", u"To Watch", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_read), QCoreApplication.translate("Backlog", u"To Read", None))
    # retranslateUi

