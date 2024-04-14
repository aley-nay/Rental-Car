# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_anapencere(object):
    def setupUi(self, anapencere):
        if not anapencere.objectName():
            anapencere.setObjectName(u"anapencere")
        anapencere.resize(767, 318)
        anapencere.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFDAB9, stop:1 #FFA07A);\n"
"color: #FF8A65;\n"
"font-weight:800;\n"
"font-size:14px;")
        self.centralwidget = QWidget(anapencere)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 80, 661, 91))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background:none")

        self.verticalLayout_2.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.musteribilgi = QPushButton(self.horizontalLayoutWidget)
        self.musteribilgi.setObjectName(u"musteribilgi")
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.musteribilgi.setFont(font)

        self.verticalLayout_2.addWidget(self.musteribilgi)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background:none")

        self.verticalLayout_3.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.aracbilgi = QPushButton(self.horizontalLayoutWidget)
        self.aracbilgi.setObjectName(u"aracbilgi")
        self.aracbilgi.setFont(font)

        self.verticalLayout_3.addWidget(self.aracbilgi)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background:none")

        self.verticalLayout_4.addWidget(self.label_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.aracbilgi2 = QPushButton(self.horizontalLayoutWidget)
        self.aracbilgi2.setObjectName(u"aracbilgi2")
        self.aracbilgi2.setFont(font)

        self.verticalLayout_4.addWidget(self.aracbilgi2)

        self.aracbilgi3 = QPushButton(self.horizontalLayoutWidget)
        self.aracbilgi3.setObjectName(u"aracbilgi3")
        self.aracbilgi3.setFont(font)

        self.verticalLayout_4.addWidget(self.aracbilgi3)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background:none")

        self.verticalLayout_5.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background:none")

        self.verticalLayout_5.addWidget(self.label_11, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.aracbilgi_plaka = QPushButton(self.horizontalLayoutWidget)
        self.aracbilgi_plaka.setObjectName(u"aracbilgi_plaka")
        self.aracbilgi_plaka.setFont(font)

        self.verticalLayout_5.addWidget(self.aracbilgi_plaka)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        anapencere.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(anapencere)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 767, 24))
        anapencere.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(anapencere)
        self.statusbar.setObjectName(u"statusbar")
        anapencere.setStatusBar(self.statusbar)

        self.retranslateUi(anapencere)

        QMetaObject.connectSlotsByName(anapencere)
    # setupUi

    def retranslateUi(self, anapencere):
        anapencere.setWindowTitle(QCoreApplication.translate("anapencere", u"Anapencere (=ↀωↀ=)", None))
        self.label_7.setText(QCoreApplication.translate("anapencere", u"M\u00fc\u015fteri Bilgileri Giri\u015f", None))
        self.musteribilgi.setText(QCoreApplication.translate("anapencere", u"B\u0130LG\u0130", None))
        self.label_8.setText(QCoreApplication.translate("anapencere", u"Ara\u00e7 Blgileri Giri\u015f", None))
        self.aracbilgi.setText(QCoreApplication.translate("anapencere", u"B\u0130LG\u0130", None))
        self.label_9.setText(QCoreApplication.translate("anapencere", u"Ara\u00e7 Kirala", None))
        self.aracbilgi2.setText(QCoreApplication.translate("anapencere", u"Kirala", None))
        self.aracbilgi3.setText(QCoreApplication.translate("anapencere", u"Kiral\u0131 ara\u00e7lar", None))
        self.label_10.setText(QCoreApplication.translate("anapencere", u"Kiral\u0131 Ara\u00e7lar", None))
        self.label_11.setText(QCoreApplication.translate("anapencere", u"(Plaka Sorgu)", None))
        self.aracbilgi_plaka.setText(QCoreApplication.translate("anapencere", u"B\u0130LG\u0130", None))
    # retranslateUi

