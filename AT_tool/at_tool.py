# 串口相关
import sys
import serial
import serial.tools.list_ports

import time
import _thread

# 窗体相关
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from PyQt5.QtCore import QTimer
from at_tool_ui import Ui_MainWindow
from PyQt5.QtGui import QIcon

from at_tool_cfg import at_tool_config

class At_Tool(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(At_Tool, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("LORAWAN模组工具")
        self.setWindowIcon(QIcon('log.ico'))  
        self.init()
        self.ser = serial.Serial()
        self.port_check()
        
    def init(self):
         # 串口搜索
        self.ser_bt_find.clicked.connect(self.port_check)
        # 串口信息显示
        self.ser_comboBox.currentTextChanged.connect(self.port_info)
        # 打开串口按钮
        self.ser_bt_open.clicked.connect(self.port_open)
        # 关闭串口按钮
        self.ser_bt_close.clicked.connect(self.port_close)
        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)
        # 功能按键
        self.at_bt_join.clicked.connect(self.AT_join)
        self.at_bt_id.clicked.connect(self.AT_ID)
        self.at_bt_send.clicked.connect(self.AT_send_test)
        self.at_bt_statue.clicked.connect(self.AT_get_statue)
        self.at_bt_clear.clicked.connect(self.AT_clear)
        self.at_bt_save.clicked.connect(self.AT_save)
        self.at_bt_config.clicked.connect(self.AT_config)
        self.at_bt_set_cfg.clicked.connect(self.AT_set_config)

    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.ser_comboBox.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.ser_comboBox.addItem(port[0])
            
        if len(self.Com_Dict) == 0:
            self.statusBar().showMessage('未搜索到串口')

        # 串口信息
    def port_info(self):
        # 显示选定的串口的详细信息
        t_info = self.ser_comboBox.currentText()
        if t_info != "":
            self.statusBar().showMessage(self.Com_Dict[self.ser_comboBox.currentText()])
    
    def port_open(self):
        self.ser.port = self.ser_comboBox.currentText()
        self.ser.baudrate = 9600
        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None  


        if self.ser.isOpen():
            self.timer.start(10)        # 打开串口接收定时器，周期为10ms
            self.ser_bt_open.setEnabled(False)
            self.ser_bt_close.setEnabled(True)
            self.statusBar().showMessage('串口已被打开')

    def port_close(self):
        
        try:
            self.ser.close()

        except:
            QMessageBox.critical(self, "Port Error", "关闭失败！")
            return None  

        self.timer.stop()
        self.ser_bt_open.setEnabled(True)
        self.ser_bt_close.setEnabled(False)
        self.statusBar().showMessage('串口已被关闭')

    # 接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0:
            data = self.ser.read(num)
            num = len(data)

            # hex显示
            # if self.hex_receive.checkState():
                # out_s = ''
                # for i in range(0, len(data)):
                #     out_s = out_s + '{:02X}'.format(data[i]) + ' '
                # self.textBrowser.insertPlainText(out_s)
            # else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去

            self.textBrowser.insertPlainText(data.decode('utf-8'))

            # 统计接收字符的数量
            # self.data_num_received += num
            # self.lineEdit.setText(str(self.data_num_received))

            # 获取到text光标
            textCursor = self.textBrowser.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.textBrowser.setTextCursor(textCursor)
        else:
            pass

    def AT_join(self):
        if self.ser.isOpen():            
            send_data = "AT+JOIN\r\n"
            self.ser.write(send_data.encode())
        else:
            QMessageBox.critical(self, 'click error', '请先打开串口!')
    
    def AT_ID(self):
        if self.ser.isOpen():            
            send_data = "AT+ID\r\n"
            self.ser.write(send_data.encode())
        else:
            QMessageBox.critical(self, 'click error', '请先打开串口!')
    
    def AT_send_test(self):
        if self.ser.isOpen():            
            send_data = "AT+SEND=123456789" + '\r\n'
            self.ser.write(send_data.encode())
        else:
            QMessageBox.critical(self, 'click error', '请先打开串口!')

    def AT_get_statue(self):
        if self.ser.isOpen():            
            send_data = "AT+STATUE" + '\r\n'
            self.ser.write(send_data.encode())
        else:
            QMessageBox.critical(self, 'click error', '请先打开串口!')

    def AT_clear(self):
        if self.ser.isOpen():            
            send_data = "AT+CLEAR" + '\r\n'
            self.ser.write(send_data.encode())
        else:
            QMessageBox.critical(self, 'click error', '请先打开串口!')

    def AT_save(self):
        if self.ser.isOpen():            
            send_data = "AT+SAVE" + '\r\n'
            self.ser.write(send_data.encode())
        else:
            QMessageBox.critical(self, 'click error', '请先打开串口!')

    def AT_config(self):
        cfg_win.open() #打开配置窗口
    
    def AT_set_config(self):
        if self.ser.isOpen():   

            self.at_bt_join.setEnabled(False)  
            self.at_bt_id.setEnabled(False)        
            self.at_bt_send.setEnabled(False) 
            self.at_bt_statue.setEnabled(False) 
            self.at_bt_clear.setEnabled(False) 
            self.at_bt_save.setEnabled(False) 
            self.at_bt_config.setEnabled(False) 
            self.at_bt_set_cfg.setEnabled(False)   

            # 建立一个线程来逐个发送
            _thread.start_new_thread(self.send_cfg, ("send_cfg", 3, ) )     

    def send_cfg(self,threadName,delay):

            send_data = "AT+DEVEUI=" +cfg_win.deveui+'\r\n' 
            self.ser.write(send_data.encode())
            time.sleep(delay) 
            send_data = "AT+APPEUI=" +cfg_win.appeui+'\r\n'
            self.ser.write(send_data.encode())
            time.sleep(delay) 
            send_data = "AT+APPKEY=" +cfg_win.appkey+'\r\n'
            self.ser.write(send_data.encode())

            self.at_bt_join.setEnabled(True)  
            self.at_bt_id.setEnabled(True)        
            self.at_bt_send.setEnabled(True) 
            self.at_bt_statue.setEnabled(True) 
            self.at_bt_clear.setEnabled(True) 
            self.at_bt_save.setEnabled(True) 
            self.at_bt_config.setEnabled(True) 
            self.at_bt_set_cfg.setEnabled(True)   



            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = At_Tool()
    cfg_win = at_tool_config()

    win.show()
    sys.exit(app.exec_())
