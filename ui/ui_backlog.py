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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.table_game = QTableWidget(Backlog)
        self.table_game.setObjectName(u"table_game")
        self.table_game.setSortingEnabled(True)

        self.horizontalLayout_2.addWidget(self.table_game)

        self.frame = QFrame(Backlog)
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
        self.add_game = QPushButton(self.frame)
        self.add_game.setObjectName(u"add_game")

        self.verticalLayout.addWidget(self.add_game)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Backlog)

        QMetaObject.connectSlotsByName(Backlog)
    # setupUi

    def retranslateUi(self, Backlog):
        Backlog.setWindowTitle(QCoreApplication.translate("Backlog", u"Backlog", None))
        self.add_game.setText(QCoreApplication.translate("Backlog", u"Add", None))
        self.pushButton.setText(QCoreApplication.translate("Backlog", u"Edit", None))
        self.pushButton_3.setText(QCoreApplication.translate("Backlog", u"Remove", None))
    # retranslateUi

