# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import os

class Page_first(object): 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(135, 361, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(135, 434, 121, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 500, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(390, 500, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 20, 231, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(121, 200, 351, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(130, 290, 351, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(121, 357, 351, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(132, 423, 341, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 205, 170, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(132, 207, 62, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(132, 274, 208, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 108, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(281, 108, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 82, 43, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(281, 82, 133, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 56, 21, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(281, 56, 133, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(200, 30, 132, 20))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 360, 170, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 430, 170, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 500, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 22))
        self.menubar.setObjectName("menubar")
        self.menu2 = QtWidgets.QMenu(self.menubar)
        self.menu2.setObjectName("menu2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "PLP Size"))
        self.label_4.setText(_translate("MainWindow", "Number of Layers (RDL)"))
        self.pushButton_8.setText(_translate("MainWindow", "Apply"))
        self.pushButton_9.setText(_translate("MainWindow", "Cancel"))
        self.checkBox.setText(_translate("MainWindow", "Yes"))
        self.label.setText(_translate("MainWindow", "Project Name"))
        self.label_2.setText(_translate("MainWindow", "Enhanced strain (Convergence Acceleration)"))
        self.pushButton_3.setText(_translate("MainWindow", "Done"))
        self.pushButton_4.setText(_translate("MainWindow", "Cancel"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "User"))
        self.comboBox.setItemText(0, _translate("MainWindow", "G2"))
        self.comboBox.setItemText(1, _translate("MainWindow", "G3.5"))
        self.comboBox.setItemText(2, _translate("MainWindow", "G5.5"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "7"))
        self.pushButton_10.setText(_translate("MainWindow", "Next"))
        self.menu2.setTitle(_translate("MainWindow", "POPLP_Simulation_GUI"))
                # this is for click action
        self.pushButton_8.clicked.connect(self.write_parameter)
        self.pushButton_9.clicked.connect(self.cancel)        
        self.pushButton_10.clicked.connect(self.toPage_2)

       
    def write_parameter(self):
        '''function of writinig parameters'''
        project_name = self.lineEdit.text()
        PLP_size = self.comboBox.currentText()
        num_layer = self.comboBox_2.currentText()


        with open('parameter_test.inp', 'a') as file:

            file.write("!--------------------Panel size-------------------\n")

            if self.comboBox.currentText() == 'G2':
                file.write("panel_width=370\n")
                file.write("panel_length=470\n")
            if self.comboBox.currentText() == 'G3.5':
                file.write("panel_width=620\n")
                file.write("panel_length=750\n")
            if self.comboBox.currentText() == 'G5.5':
                file.write("panel_width=1300\n")
                file.write("panel_length=1500\n")
            
            file.write("!-------------------Number of layers -------------------\n")
            file.write("num_layer="+str(self.comboBox_2.currentText())+str("\n"))



    def cancel(self):
        app = QApplication(sys.argv)
        sys.exit(app.exec_())

    def toPage_2(self):
        self.w = MyWindow_2(num_layer=str(self.comboBox_2.currentText()))
        self.w.show()
        self.hide()

class Page_second(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 680)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(80, 0, 901, 621))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 70, 101, 41))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(190, 80, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 121, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 111, 31))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(210, 163, 113, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(211, 220, 113, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(60, 270, 91, 31))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(209, 280, 113, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(60, 330, 291, 31))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 337, 113, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(170, 470, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 470, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 470, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(442, 101, 421, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 131, 31))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 111, 31))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 160, 111, 31))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 220, 131, 31))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(164, 56, 151, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(165, 105, 151, 21))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(166, 165, 151, 21))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(167, 224, 151, 21))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Layer Set"))
        self.label.setText(_translate("Form", "Select Layers"))
        self.label_2.setText(_translate("Form", "Layer Name"))
        self.label_3.setText(_translate("Form", "Thickness (um)"))
        self.label_4.setText(_translate("Form", "Mesh Split"))
        self.label_5.setText(_translate("Form", "Process Temperature"))
        self.pushButton.setText(_translate("Form", "Back"))
        self.pushButton_2.setText(_translate("Form", "Set"))
        self.pushButton_3.setText(_translate("Form", "Next"))
        self.groupBox_2.setTitle(_translate("Form", "Material Property"))
        self.label_7.setText(_translate("Form", "Young\'s modulus :"))
        self.label_8.setText(_translate("Form", "CTE :"))
        self.label_9.setText(_translate("Form", "Poisson\'s ratio : "))
        self.label_10.setText(_translate("Form", "Density : "))

        # create dictionarys to collect parameters
        self.dict_thickness = {} 
        self.dict_name = {}
        self.dict_mesh = {}
        self.dict_temp = {} 
        # material parameters
        self.dict_ex = {}    # young's modulus
        self.dict_prxy = {}  # poisson ratio 
        self.dict_ctex = {}  # CTE 
        self.dict_density = {}


        # this is for click action
        self.pushButton.clicked.connect(self.toPage_1)
        self.pushButton_2.clicked.connect(self.write_parameter_dict)
        self.pushButton_3.clicked.connect(self.toPage_3)

    def write_parameter_dict(self):
        self.dict_thickness["t"+str(self.comboBox.currentText())] = self.lineEdit_2.text()  # thickness of layer
        self.dict_name["t_name"+str(self.comboBox.currentText())] = self.lineEdit.text()   # name of layer
        self.dict_mesh["t_mesh"+str(self.comboBox.currentText())] = self.lineEdit_3.text()  # mesh split
        self.dict_temp["process_"+str(self.comboBox.currentText())] = self.lineEdit_4.text()  # process temperature

        self.dict_ex["mat_ex_"+str(self.comboBox.currentText())] = self.lineEdit_5.text()  # young's modulus
        self.dict_prxy["mat_prxy_"+str(self.comboBox.currentText())] = self.lineEdit_6.text()  # poisson ratio
        self.dict_ctex["mat_ctex_"+str(self.comboBox.currentText())] = self.lineEdit_7.text()  # CTE
        self.dict_density["mat_ctex_"+str(self.comboBox.currentText())] = self.lineEdit_8.text() # density



    def toPage_1(self):
        self.w = MyWindow_1()
        self.w.show()
        self.hide()

    def toPage_3(self):
        with open('parameter_test.inp', 'a') as file:
            
            file.write("!-------------------Thickness of each layer-------------------\n")
            for key, value in self.dict_thickness.items():
                file.write(str(key)+"="+str(value)+"\n")

            file.write("!-------------------Name of each layer----------------------\n")
            for key, value in self.dict_name.items():
                file.write(str(key)+"="+"\'"+str(value)+"\'""\n")

            file.write("!-------------------Cutting accuracy of each layer----------------------\n")
            for key, value in self.dict_mesh.items():
                file.write(str(key)+"="+str(value)+"\n")
                
            file.write("!-------------------Process temperature parameters----------------------\n")
            for key, value in self.dict_temp.items():
                file.write(str(key)+"="+str(value)+"\n")


            file.write("!-------------------Material parameters----------------------\n")
            
            file.write("!young's modulus\n")
            for key, value in self.dict_ex.items():
                file.write(str(key)+"="+str(value)+"\n")

            file.write("!poisson ration\n")
            for key, value in self.dict_prxy.items():
                file.write(str(key)+"="+str(value)+"\n")

            file.write("!CTE\n")
            for key, value in self.dict_ctex.items():
                file.write(str(key)+"="+str(value)+"\n")

            file.write("!Density\n")
            for key, value in self.dict_density.items():
                if value:
                    file.write(str(key)+"="+str(value)+"\n")
            


        
        self.w = MyWindow_3(num_layer=str(self.num_layer))
        self.w.show()
        self.hide()

class Page_third(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1106, 804)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(70, 50, 931, 701))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 90, 181, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(120, 160, 721, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(100, 300, 181, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 350, 721, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(120, 470, 171, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 470, 171, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 470, 181, 61))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Setting information"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Ansys程式路徑</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">存檔路徑</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.pushButton_3.setText(_translate("Form", "Analysis"))

        # this is for click action
        self.pushButton_2.clicked.connect(self.toPage_2)
        #self.pushButton_3.clicked.connect(self.run)


    
    # def run(self):
    #     os.system('cmd /k "C:\Program Files\ANSYS Inc\v192\ansys\bin\winx64\MAPDL.exe" -p ansys -np 4 -dir "C:\Users\user\Desktop\pyqt_ansys" -j "test" -s noread -l en-us -b -i "C:\Users\user\Desktop\pyqt_ansys\main.inp" -o "C:\Users\user\Desktop\pyqt_ansys\test.out')
    #     os.system('cmd /k "C:\Program Files\ANSYS Inc\v192\ansys\bin\winx64\MAPDL.exe" -p ansys -np 4 -dir "C:\Users\user\Desktop\pyqt_ansys\test" -j "test" -s noread -l en-us -b -i "C:\Users\user\Desktop\pyqt_ansys\test\eq_CTE_0222_SiNx_thickness_0.8" -o "C:\Users\user\Desktop\pyqt_ansys\test\test.out')
    def toPage_2(self):
        self.w = MyWindow_2(num_layer=str(self.num_layer))
        self.w.show()
        self.hide()



class MyWindow_1(QMainWindow, Page_first):
    def __init__(self, parent=None):
        super(MyWindow_1, self).__init__(parent)
        self.setupUi(self)

class MyWindow_2(QMainWindow, Page_second):
    def __init__(self, num_layer, parent=None):
        super(MyWindow_2, self).__init__(parent)
        self.num_layer = num_layer
        self.setupUi(self)
        
        self.comboBox.addItem("glass")
        for i in range(int(self.num_layer)):
            self.comboBox.addItem(str(i+1))

class MyWindow_3(QMainWindow, Page_third):
    def __init__(self, num_layer, parent=None):
        super(MyWindow_3, self).__init__(parent)
        self.num_layer = num_layer
        self.setupUi(self)


if __name__ == '__main__':
    
    if os.path.exists("parameter_test.inp"):
        os.remove("parameter_test.inp")
    
    app = QApplication(sys.argv)
    myWin = MyWindow_1()
    myWin.show()
    sys.exit(app.exec_())



'''
question
1. ehance strain in P1, what is this parameter?
2. Ref temperature in P2 
'''
