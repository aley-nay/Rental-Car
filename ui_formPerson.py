# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPerson.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_addPerson(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(637, 469)
        Form.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFDAB9, stop:1 #FFA07A);\n"
"color: #FF8A65;\n"
"font-weight:800;\n"
"font-size:14px;")
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 290, 631, 181))
        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 631, 266))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background:none")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.lineEdit_id = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit_id)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background:none")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background:none")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.label_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background:none")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background:none")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background:none")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_18)

        self.checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.checkBox)

        self.lineEdit_ad = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_ad.setObjectName(u"lineEdit_ad")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_ad)

        self.lineEdit_tcno = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_tcno.setObjectName(u"lineEdit_tcno")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_tcno)

        self.lineEdit_adres = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_adres.setObjectName(u"lineEdit_adres")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_adres)

        self.lineEdit_meslek = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_meslek.setObjectName(u"lineEdit_meslek")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_meslek)

        self.lineEdit_medeni = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_medeni.setObjectName(u"lineEdit_medeni")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_medeni)


        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_19 = QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background:none")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.label_20 = QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"background:none")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_20)

        self.label_21 = QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background:none")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.label_22 = QLabel(self.verticalLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"background:none")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_22)

        self.label_23 = QLabel(self.verticalLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"background:none")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_23)

        self.lineEdit_dTarihi = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_dTarihi.setObjectName(u"lineEdit_dTarihi")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_dTarihi)

        self.lineEdit_soyad = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_soyad.setObjectName(u"lineEdit_soyad")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_soyad)

        self.lineEdit_telno = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_telno.setObjectName(u"lineEdit_telno")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_telno)

        self.lineEdit_ehliyet = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_ehliyet.setObjectName(u"lineEdit_ehliyet")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_ehliyet)

        self.lineEdit_egitim = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_egitim.setObjectName(u"lineEdit_egitim")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_egitim)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_yeni = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_yeni.setObjectName(u"pushButton_yeni")

        self.horizontalLayout_3.addWidget(self.pushButton_yeni)

        self.pushButton_update = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_update.setObjectName(u"pushButton_update")

        self.horizontalLayout_3.addWidget(self.pushButton_update)

        self.pushButton_kaydet = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_kaydet.setObjectName(u"pushButton_kaydet")

        self.horizontalLayout_3.addWidget(self.pushButton_kaydet)

        self.pushButton_sil = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_sil.setObjectName(u"pushButton_sil")

        self.horizontalLayout_3.addWidget(self.pushButton_sil)

        self.pushButton_Getir2 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_Getir2.setObjectName(u"pushButton_Getir2")

        self.horizontalLayout_3.addWidget(self.pushButton_Getir2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Musteri Giris Ekrani ฅ^•ﻌ•^ฅ", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"User ID:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Ad", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Tc Kimlik", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Adres", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Meslek", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Medeni Durum", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Aktif", None))
        self.checkBox.setText("")
        self.label_19.setText(QCoreApplication.translate("Form", u"Soyad", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Do\u011fum Tarihi", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Tel", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Ehliyet S\u0131n\u0131f\u0131", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"E\u011fitim Durum", None))
        self.pushButton_yeni.setText(QCoreApplication.translate("Form", u"Yeni", None))
        self.pushButton_update.setText(QCoreApplication.translate("Form", u"G\u00fcncelle", None))
        self.pushButton_kaydet.setText(QCoreApplication.translate("Form", u"Kaydet", None))
        self.pushButton_sil.setText(QCoreApplication.translate("Form", u"Sil", None))
        self.pushButton_Getir2.setText(QCoreApplication.translate("Form", u"Getir", None))
    # retranslateUi

