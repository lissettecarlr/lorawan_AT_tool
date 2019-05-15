# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from at_tool_cfg_ui import Ui_Form

class at_tool_config(QtWidgets.QWidget,Ui_Form):

    deveui = '68d90000000000fe'
    appeui = '68d9000000000001'
    appeky = 'f56117376053542e894480dd446d9cb2'
    netskey = ''
    appskey = ''
    def __init__(self):
        super(at_tool_config, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("预存配置")

        fo = open('cfg.txt','r')

        self.deveui = fo.read(16)
        self.appeui = fo.read(16)
        self.appkey = fo.read(32)
        self.netskey = fo.read(32)
        self.appskey = fo.read(32)

        # print("%s\n"%(self.deveui))
        # print("%s\n"%(self.appeui))
        # print("%s\n"%(self.appkey))
        # print("%s\n"%(self.netskey))
        # print("%s\n"%(self.appskey))

        self.lineEdit_deveui.setText(self.deveui)
        self.lineEdit_appeui.setText(self.appeui)
        self.lineEdit_appkey.setText(self.appkey)
        self.lineEdit_netskey.setText(self.netskey)
        self.lineEdit_appskey.setText(self.appskey)

        self.cfg_bt_ok.clicked.connect(self.cfg_ok)
        self.cfg_bt_no.clicked.connect(self.cfg_no)
        fo.close()

    def open(self):
        self.show()

    def cfg_ok(self):

        self.deveui = self.lineEdit_deveui.text()
        self.appeui = self.lineEdit_appeui.text()
        self.appkey = self.lineEdit_appkey.text()
        self.netskey = self.lineEdit_netskey.text()
        self.appskey = self.lineEdit_appskey.text()

        self.deveui = self.deveui.strip()
        self.appeui = self.appeui.strip()
        self.appkey = self.appkey.strip()
        self.netskey = self.netskey.strip()
        self.appskey = self.appskey.strip()

        if(len(self.deveui) !=16):
            QMessageBox.critical(self, 'cfg error', 'deveui长度错误!')
            return None

        if(len(self.appeui) !=16):
            QMessageBox.critical(self, 'cfg error', 'appeui长度错误!')
            return None

        if(len(self.appeky) !=32):
            QMessageBox.critical(self, 'cfg error', 'appeky长度错误!')
            return None       

        if(len(self.netskey) !=32):
            QMessageBox.critical(self, 'cfg error', 'netskey长度错误!')
            return None   

        if(len(self.netskey) !=32):
            QMessageBox.critical(self, 'cfg error', 'netskey长度错误!')
            return None  

        fo = open('cfg.txt','w')
        fo.write(self.deveui)
        fo.write(self.appeui)
        fo.write(self.appkey)
        fo.write(self.netskey)
        fo.write(self.appskey)
        fo.close()

        self.close()

    def cfg_no(self):
        self.close()
 

        