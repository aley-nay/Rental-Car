# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formBul.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Bul(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(631, 475)
        Form.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFDAB9, stop:1 #FFA07A);\n"
"color: #FF8A65;\n"
"font-weight:800;\n"
"font-size:14px;")
        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 631, 301))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_aracid = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_aracid.setObjectName(u"lineEdit_aracid")
        self.lineEdit_aracid.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_aracid)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_25 = QLabel(self.verticalLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_25)

        self.label_17 = QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_18)

        self.label_20 = QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_20)

        self.label_22 = QLabel(self.verticalLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_22)

        self.lineEdit_marka = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_marka.setObjectName(u"lineEdit_marka")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_marka)

        self.lineEdit_model = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_model.setObjectName(u"lineEdit_model")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_model)

        self.lineEdit_uretimYil = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_uretimYil.setObjectName(u"lineEdit_uretimYil")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_uretimYil)

        self.lineEdit_yakit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_yakit.setObjectName(u"lineEdit_yakit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_yakit)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label)

        self.lineEdit_plaka = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_plaka.setObjectName(u"lineEdit_plaka")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_plaka)

        self.lineEdit_aracTuru = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_aracTuru.setObjectName(u"lineEdit_aracTuru")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_aracTuru)


        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.label_16 = QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.label_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.label_24 = QLabel(self.verticalLayoutWidget_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_24)

        self.label_23 = QLabel(self.verticalLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_23)

        self.label_21 = QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_21)

        self.label_19 = QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_19)

        self.lineEdit_vites = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_vites.setObjectName(u"lineEdit_vites")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_vites)

        self.lineEdit_kasa = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_kasa.setObjectName(u"lineEdit_kasa")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_kasa)

        self.lineEdit_motorHacmi = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_motorHacmi.setObjectName(u"lineEdit_motorHacmi")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_motorHacmi)

        self.lineEdit_cekis = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_cekis.setObjectName(u"lineEdit_cekis")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_cekis)

        self.lineEdit_kapi = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_kapi.setObjectName(u"lineEdit_kapi")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_kapi)

        self.lineEdit_renk = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_renk.setObjectName(u"lineEdit_renk")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lineEdit_renk)

        self.lineEdit_motor = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_motor.setObjectName(u"lineEdit_motor")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.lineEdit_motor)


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

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 300, 631, 171))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Arac Giris Ekrani ฅ^•ﻌ•^ฅ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ARAC ID", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Ara\u00e7 T\u00fcr\u00fc", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Marka", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Model", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u00dcretim Y\u0131l\u0131", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Yak\u0131t T\u00fcr\u00fc", None))
        self.label.setText(QCoreApplication.translate("Form", u"Plaka", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Vites", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Kasa Tipi", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Motor Hacmi", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"\u00c7eki\u015f", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Kap\u0131", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Renk", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Motor No", None))
        self.pushButton_yeni.setText(QCoreApplication.translate("Form", u"Yeni", None))
        self.pushButton_update.setText(QCoreApplication.translate("Form", u"G\u00fcncelle", None))
        self.pushButton_kaydet.setText(QCoreApplication.translate("Form", u"Kaydet", None))
        self.pushButton_sil.setText(QCoreApplication.translate("Form", u"Sil", None))
        self.pushButton_Getir2.setText(QCoreApplication.translate("Form", u"Getir", None))
    # retranslateUi

