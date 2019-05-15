# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'at_tool_cfg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(274, 228)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 20, 201, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_deveui = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_deveui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_deveui.setObjectName("lineEdit_deveui")
        self.verticalLayout.addWidget(self.lineEdit_deveui)
        self.lineEdit_appeui = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_appeui.setObjectName("lineEdit_appeui")
        self.verticalLayout.addWidget(self.lineEdit_appeui)
        self.lineEdit_appkey = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_appkey.setObjectName("lineEdit_appkey")
        self.verticalLayout.addWidget(self.lineEdit_appkey)
        self.lineEdit_netskey = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_netskey.setObjectName("lineEdit_netskey")
        self.verticalLayout.addWidget(self.lineEdit_netskey)
        self.lineEdit_appskey = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_appskey.setObjectName("lineEdit_appskey")
        self.verticalLayout.addWidget(self.lineEdit_appskey)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 51, 151))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(20, 180, 241, 41))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cfg_bt_ok = QtWidgets.QPushButton(self.widget2)
        self.cfg_bt_ok.setObjectName("cfg_bt_ok")
        self.horizontalLayout.addWidget(self.cfg_bt_ok)
        self.cfg_bt_no = QtWidgets.QPushButton(self.widget2)
        self.cfg_bt_no.setObjectName("cfg_bt_no")
        self.horizontalLayout.addWidget(self.cfg_bt_no)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "at_config"))
        self.lineEdit_deveui.setText(_translate("Form", "68d90000000000fe"))
        self.lineEdit_appeui.setText(_translate("Form", "68d9000000000001"))
        self.lineEdit_appkey.setText(_translate("Form", "f56117376053542e894480dd446d9cb2 "))
        self.label.setText(_translate("Form", "DEVEUI"))
        self.label_2.setText(_translate("Form", "APPEUI"))
        self.label_3.setText(_translate("Form", "APPKEY"))
        self.label_4.setText(_translate("Form", "NETSKEY"))
        self.label_5.setText(_translate("Form", "APPSKEY"))
        self.cfg_bt_ok.setText(_translate("Form", "确定"))
        self.cfg_bt_no.setText(_translate("Form", "取消"))

