#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Model_BE import Model

class Ui_form(object):
        def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.resize(1037, 758)

            #НУЖНЫЕ ПОЛЯ
            #это поля, которые передаются коду Игоря
            self.LG_index = 0 #индекс в списке вариантов для L и G
            self.Y_index = 0 #индекс в списке вариантов для Y
            self.time = 0 #время окончания процесса
            self.dim = 3 #размерность
            self.x_min = 0 #self-explanatory
            self.y_min = 0
            self.x_max = 0
            self.y_max = 0
            self.start_conditions = [()] #[(x1, x2, 0)]
            self.border_conditions = [()] #[(x1, x2,t)]
            self.points_sm0 = [()] #[(x1,x2,t)]
            self.points_smG = [()] #[(x1,x2,t)]
            #x2 присутствует всегда, вне зависимости от выбранной размерности
            #вам нужно будет в зависимости от dim брать нужное количество данных из списков conditions
            
            #КОНЕЦ НУЖНЫХ ПОЛЕЙ
            
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(52, 137, 177))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
            brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(52, 137, 177))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
            brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(52, 137, 177))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
            Form.setPalette(palette)
            self.gridLayout_3 = QtWidgets.QGridLayout(Form)
            self.gridLayout_3.setObjectName("gridLayout_3")
            self.verticalLayout_22 = QtWidgets.QVBoxLayout()
            self.verticalLayout_22.setObjectName("verticalLayout_22")
            self.label = QtWidgets.QLabel(Form)
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(52, 137, 177))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(52, 137, 177))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            self.label.setPalette(palette)
            font = QtGui.QFont()
            font.setFamily("Code Bold")
            font.setPointSize(48)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.label.setObjectName("label")
            self.verticalLayout_22.addWidget(self.label)
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setObjectName("verticalLayout")
            self.tabWidget = QtWidgets.QTabWidget(Form)
            self.tabWidget.setObjectName("tabWidget")
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.gridLayout_9 = QtWidgets.QGridLayout(self.tab)
            self.gridLayout_9.setObjectName("gridLayout_9")
            self.scrollArea_3 = QtWidgets.QScrollArea(self.tab)
            self.scrollArea_3.setWidgetResizable(True)
            self.scrollArea_3.setObjectName("scrollArea_3")
            self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
            self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 981, 555))
            self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
            self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_8)
            self.formLayout.setObjectName("formLayout")
            self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(11)
            self.label_4.setFont(font)
            self.label_4.setObjectName("label_4")
            self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_4)
            self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_8)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.comboBox.setFont(font)
            self.comboBox.setObjectName("comboBox")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.comboBox)
            self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(11)
            self.label_5.setFont(font)
            self.label_5.setObjectName("label_5")
            self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label_5)
            self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_8)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.comboBox_2.setFont(font)
            self.comboBox_2.setObjectName("comboBox_2")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.comboBox_2)
            self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(10)
            self.label_6.setFont(font)
            self.label_6.setObjectName("label_6")
            self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_6)
            self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(10)
            self.label_7.setFont(font)
            self.label_7.setObjectName("label_7")
            self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.label_7)
            self.line_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
            self.line_14.setMinimumSize(QtCore.QSize(100, 0))
            self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_14.setObjectName("line_14")
            self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.line_14)
            self.line_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
            self.line_15.setMinimumSize(QtCore.QSize(100, 0))
            self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_15.setObjectName("line_15")
            self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.line_15)
            self.line_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
            self.line_16.setMinimumSize(QtCore.QSize(100, 0))
            self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_16.setObjectName("line_16")
            self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line_16)
            self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_8)
            self.gridLayout_9.addWidget(self.scrollArea_3, 0, 0, 1, 1)
            self.tabWidget.addTab(self.tab, "")
            self.tab_2 = QtWidgets.QWidget()
            self.tab_2.setObjectName("tab_2")
            self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
            self.gridLayout_8.setObjectName("gridLayout_8")
            self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_2)
            self.scrollArea_4.setWidgetResizable(True)
            self.scrollArea_4.setObjectName("scrollArea_4")
            self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
            self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 981, 555))
            self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
            self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_9)
            self.gridLayout_7.setObjectName("gridLayout_7")
            self.gridLayout_6 = QtWidgets.QGridLayout()
            self.gridLayout_6.setObjectName("gridLayout_6")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout()
            self.verticalLayout_4.setObjectName("verticalLayout_4")
            self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(11)
            self.label_12.setFont(font)
            self.label_12.setAlignment(QtCore.Qt.AlignCenter)
            self.label_12.setObjectName("label_12")
            self.verticalLayout_4.addWidget(self.label_12)
            self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_9.setObjectName("horizontalLayout_9")
            self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
            font = QtGui.QFont()
            font.setFamily("Lato")
            self.label_13.setFont(font)
            self.label_13.setObjectName("label_13")
            self.horizontalLayout_9.addWidget(self.label_13)
            self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
            self.lineEdit_3.setObjectName("lineEdit_3")
            self.horizontalLayout_9.addWidget(self.lineEdit_3)
            self.verticalLayout_4.addLayout(self.horizontalLayout_9)
            self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_10.setObjectName("horizontalLayout_10")
            self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
            font = QtGui.QFont()
            font.setFamily("Lato")
            self.label_14.setFont(font)
            self.label_14.setObjectName("label_14")
            self.horizontalLayout_10.addWidget(self.label_14)
            self.verticalLayout_3 = QtWidgets.QVBoxLayout()
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_9)
            self.radioButton.setObjectName("radioButton")
            self.verticalLayout_3.addWidget(self.radioButton)
            self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_9)
            self.radioButton_2.setObjectName("radioButton_2")
            self.radioButton_2.setChecked(True)
            self.verticalLayout_3.addWidget(self.radioButton_2)
            self.horizontalLayout_10.addLayout(self.verticalLayout_3)
            self.verticalLayout_4.addLayout(self.horizontalLayout_10)
            self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
            font = QtGui.QFont()
            font.setFamily("Lato")
            self.pushButton.setFont(font)
            self.pushButton.setObjectName("pushButton")
            self.verticalLayout_4.addWidget(self.pushButton)
            self.formLayout_2 = QtWidgets.QFormLayout()
            self.formLayout_2.setObjectName("formLayout_2")
            self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
            self.label_2.setObjectName("label_2")
            self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
            self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
            self.label_3.setObjectName("label_3")
            self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.horizontalLayout.addWidget(self.lineEdit_2)
            self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
            self.lineEdit.setObjectName("lineEdit")
            self.horizontalLayout.addWidget(self.lineEdit)
            self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
            self.lineEdit_5.setObjectName("lineEdit_5")
            self.horizontalLayout_2.addWidget(self.lineEdit_5)
            self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
            self.lineEdit_4.setObjectName("lineEdit_4")
            self.horizontalLayout_2.addWidget(self.lineEdit_4)
            self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
            self.verticalLayout_4.addLayout(self.formLayout_2)
            self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
            self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
            self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_9)
            self.gridLayout_8.addWidget(self.scrollArea_4, 0, 0, 1, 1)
            self.tabWidget.addTab(self.tab_2, "")
            self.tab_4 = QtWidgets.QWidget()
            self.tab_4.setObjectName("tab_4")
            self.gridLayout = QtWidgets.QGridLayout(self.tab_4)
            self.gridLayout.setObjectName("gridLayout")
            self.scrollArea = QtWidgets.QScrollArea(self.tab_4)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
            self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 981, 548))
            self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
            self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
            self.gridLayout_4.setObjectName("gridLayout_4")
            self.verticalLayout_26 = QtWidgets.QVBoxLayout()
            self.verticalLayout_26.setObjectName("verticalLayout_26")
            self.verticalLayout_27 = QtWidgets.QVBoxLayout()
            self.verticalLayout_27.setObjectName("verticalLayout_27")
            self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(11)
            self.label_39.setFont(font)
            self.label_39.setAlignment(QtCore.Qt.AlignCenter)
            self.label_39.setObjectName("label_39")
            self.verticalLayout_27.addWidget(self.label_39)
            self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_19.setObjectName("horizontalLayout_19")
            self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(9)
            self.label_40.setFont(font)
            self.label_40.setAlignment(QtCore.Qt.AlignCenter)
            self.label_40.setObjectName("label_40")
            self.horizontalLayout_19.addWidget(self.label_40)
            self.spinBox_5 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_4)
            self.spinBox_5.setObjectName("spinBox_5")
            #self.spinBox_5.setMinimum(1)
            self.horizontalLayout_19.addWidget(self.spinBox_5)
            self.verticalLayout_27.addLayout(self.horizontalLayout_19)
            self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
            self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_10.setObjectName("line_10")
            self.verticalLayout_27.addWidget(self.line_10)
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.verticalLayout_28 = QtWidgets.QVBoxLayout()
            self.verticalLayout_28.setObjectName("verticalLayout_28")
            self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
            font = QtGui.QFont()
            font.setFamily("Lato")
            self.label_41.setFont(font)
            self.label_41.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_41.setObjectName("label_41")
            self.verticalLayout_28.addWidget(self.label_41)
            self.horizontalLayout_3.addLayout(self.verticalLayout_28)
            self.line_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
            self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_12.setObjectName("line_12")
            self.horizontalLayout_3.addWidget(self.line_12)
            self.verticalLayout_29 = QtWidgets.QVBoxLayout()
            self.verticalLayout_29.setObjectName("verticalLayout_29")
            self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
            font = QtGui.QFont()
            font.setFamily("Lato")
            self.label_42.setFont(font)
            self.label_42.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_42.setObjectName("label_42")
            self.verticalLayout_29.addWidget(self.label_42)
            self.horizontalLayout_3.addLayout(self.verticalLayout_29)
            self.verticalLayout_27.addLayout(self.horizontalLayout_3)
            self.verticalLayout_26.addLayout(self.verticalLayout_27)
            self.gridLayout_4.addLayout(self.verticalLayout_26, 0, 0, 1, 1)
            self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
            self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_3.setObjectName("line_3")
            self.gridLayout_4.addWidget(self.line_3, 0, 1, 1, 1)
            self.verticalLayout_30 = QtWidgets.QVBoxLayout()
            self.verticalLayout_30.setObjectName("verticalLayout_30")
            self.verticalLayout_31 = QtWidgets.QVBoxLayout()
            self.verticalLayout_31.setObjectName("verticalLayout_31")
            self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(11)
            self.label_43.setFont(font)
            self.label_43.setAlignment(QtCore.Qt.AlignCenter)
            self.label_43.setObjectName("label_43")
            self.verticalLayout_31.addWidget(self.label_43)
            self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_21.setObjectName("horizontalLayout_21")
            self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(9)
            self.label_44.setFont(font)
            self.label_44.setAlignment(QtCore.Qt.AlignCenter)
            self.label_44.setObjectName("label_44")
            self.horizontalLayout_21.addWidget(self.label_44)
            self.spinBox_6 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_4)
            self.spinBox_6.setObjectName("spinBox_6")
            self.horizontalLayout_21.addWidget(self.spinBox_6)
            self.verticalLayout_31.addLayout(self.horizontalLayout_21)
            self.line_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
            self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_11.setObjectName("line_11")
            self.verticalLayout_31.addWidget(self.line_11)
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.verticalLayout_32 = QtWidgets.QVBoxLayout()
            self.verticalLayout_32.setObjectName("verticalLayout_32")
            self.label_45 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
            font = QtGui.QFont()
            font.setFamily("Lato")
            self.label_45.setFont(font)
            self.label_45.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_45.setObjectName("label_45")
            self.verticalLayout_32.addWidget(self.label_45)
            self.horizontalLayout_4.addLayout(self.verticalLayout_32)
            self.line_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
            self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_13.setObjectName("line_13")
            self.horizontalLayout_4.addWidget(self.line_13)
            self.verticalLayout_33 = QtWidgets.QVBoxLayout()
            self.verticalLayout_33.setObjectName("verticalLayout_33")
            self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
            font = QtGui.QFont()
            font.setFamily("Lato")
            self.label_46.setFont(font)
            self.label_46.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_46.setObjectName("label_46")
            self.verticalLayout_33.addWidget(self.label_46)
            self.horizontalLayout_4.addLayout(self.verticalLayout_33)
            self.line_18 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
            self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_18.setObjectName("line_18")
            self.horizontalLayout_4.addWidget(self.line_18)
            self.verticalLayout_8 = QtWidgets.QVBoxLayout()
            self.verticalLayout_8.setObjectName("verticalLayout_8")
            self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
            self.label_18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_18.setObjectName("label_18")
            self.verticalLayout_8.addWidget(self.label_18)
            self.horizontalLayout_4.addLayout(self.verticalLayout_8)
            self.verticalLayout_31.addLayout(self.horizontalLayout_4)
            self.verticalLayout_30.addLayout(self.verticalLayout_31)
            self.gridLayout_4.addLayout(self.verticalLayout_30, 0, 2, 1, 1)
            self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
            self.pushButton_2.setObjectName("pushButton_2")
            self.gridLayout_4.addWidget(self.pushButton_2, 1, 0, 1, 1)
            self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
            self.pushButton_3.setObjectName("pushButton_3")
            self.gridLayout_4.addWidget(self.pushButton_3, 1, 2, 1, 1)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
            self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 3)
            self.line = QtWidgets.QFrame(self.tab_4)
            self.line.setFrameShape(QtWidgets.QFrame.VLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
            self.tabWidget.addTab(self.tab_4, "")
            self.tab_3 = QtWidgets.QWidget()
            self.tab_3.setObjectName("tab_3")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_3)
            self.scrollArea_2.setWidgetResizable(True)
            self.scrollArea_2.setObjectName("scrollArea_2")
            self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
            self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 981, 555))
            self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
            self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_7)
            self.gridLayout_5.setObjectName("gridLayout_5")
            self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_11.setObjectName("horizontalLayout_11")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout()
            self.verticalLayout_6.setObjectName("verticalLayout_6")
            self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(11)
            self.label_29.setFont(font)
            self.label_29.setAlignment(QtCore.Qt.AlignCenter)
            self.label_29.setObjectName("label_29")
            self.verticalLayout_6.addWidget(self.label_29)
            self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_17.setObjectName("horizontalLayout_17")
            self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(9)
            self.label_34.setFont(font)
            self.label_34.setObjectName("label_34")
            self.label_34.setAlignment(QtCore.Qt.AlignCenter)
            self.horizontalLayout_17.addWidget(self.label_34)
            self.spinBox_4 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_7)
            self.spinBox_4.setObjectName("spinBox_4")
            self.horizontalLayout_17.addWidget(self.spinBox_4)
            self.verticalLayout_6.addLayout(self.horizontalLayout_17)
            self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
            self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_4.setObjectName("line_4")
            self.verticalLayout_6.addWidget(self.line_4)
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.verticalLayout_14 = QtWidgets.QVBoxLayout()
            self.verticalLayout_14.setObjectName("verticalLayout_14")
            self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_8.setObjectName("label_8")
            self.verticalLayout_14.addWidget(self.label_8)
            self.horizontalLayout_5.addLayout(self.verticalLayout_14)
            self.line_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
            self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_6.setObjectName("line_6")
            self.horizontalLayout_5.addWidget(self.line_6)
            self.verticalLayout_23 = QtWidgets.QVBoxLayout()
            self.verticalLayout_23.setObjectName("verticalLayout_23")
            self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_9.setObjectName("label_9")
            self.verticalLayout_23.addWidget(self.label_9)
            self.horizontalLayout_5.addLayout(self.verticalLayout_23)
            self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
            self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_7.setObjectName("line_7")
            self.horizontalLayout_5.addWidget(self.line_7)
            self.verticalLayout_24 = QtWidgets.QVBoxLayout()
            self.verticalLayout_24.setObjectName("verticalLayout_24")
            self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_10.setObjectName("label_10")
            self.verticalLayout_24.addWidget(self.label_10)
            self.horizontalLayout_5.addLayout(self.verticalLayout_24)
            self.verticalLayout_6.addLayout(self.horizontalLayout_5)
            self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
            self.pushButton_4.setObjectName("pushButton_4")
            self.verticalLayout_6.addWidget(self.pushButton_4)
            self.horizontalLayout_11.addLayout(self.verticalLayout_6)
            self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
            self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_2.setObjectName("line_2")
            self.horizontalLayout_11.addWidget(self.line_2)
            self.verticalLayout_7 = QtWidgets.QVBoxLayout()
            self.verticalLayout_7.setObjectName("verticalLayout_7")
            self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(12)
            self.label_32.setFont(font)
            self.label_32.setAlignment(QtCore.Qt.AlignCenter)
            self.label_32.setObjectName("label_32")
            self.verticalLayout_7.addWidget(self.label_32)
            self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_15.setObjectName("horizontalLayout_15")
            self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setPointSize(9)
            self.label_28.setFont(font)
            self.label_28.setObjectName("label_28")
            self.label_28.setAlignment(QtCore.Qt.AlignCenter)
            self.horizontalLayout_15.addWidget(self.label_28)
            self.spinBox_3 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_7)
            self.spinBox_3.setObjectName("spinBox_3")
            self.horizontalLayout_15.addWidget(self.spinBox_3)
            self.verticalLayout_7.addLayout(self.horizontalLayout_15)
            self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
            self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_5.setObjectName("line_5")
            self.verticalLayout_7.addWidget(self.line_5)
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")
            self.verticalLayout_25 = QtWidgets.QVBoxLayout()
            self.verticalLayout_25.setObjectName("verticalLayout_25")
            self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_11.setObjectName("label_11")
            self.verticalLayout_25.addWidget(self.label_11)
            self.horizontalLayout_6.addLayout(self.verticalLayout_25)
            self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
            self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_8.setObjectName("line_8")
            self.horizontalLayout_6.addWidget(self.line_8)
            self.verticalLayout_34 = QtWidgets.QVBoxLayout()
            self.verticalLayout_34.setObjectName("verticalLayout_34")
            self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_15.setObjectName("label_15")
            self.verticalLayout_34.addWidget(self.label_15)
            self.horizontalLayout_6.addLayout(self.verticalLayout_34)
            self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
            self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_9.setObjectName("line_9")
            self.horizontalLayout_6.addWidget(self.line_9)
            self.verticalLayout_35 = QtWidgets.QVBoxLayout()
            self.verticalLayout_35.setObjectName("verticalLayout_35")
            self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
            self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
            self.label_16.setObjectName("label_16")
            self.verticalLayout_35.addWidget(self.label_16)
            self.horizontalLayout_6.addLayout(self.verticalLayout_35)
            self.verticalLayout_7.addLayout(self.horizontalLayout_6)
            self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
            self.pushButton_5.setObjectName("pushButton_5")
            self.verticalLayout_7.addWidget(self.pushButton_5)
            self.horizontalLayout_11.addLayout(self.verticalLayout_7)
            self.gridLayout_5.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
            self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_7)
            self.gridLayout_2.addWidget(self.scrollArea_2, 1, 0, 1, 1)
            self.tabWidget.addTab(self.tab_3, "")
            self.verticalLayout.addWidget(self.tabWidget)
            self.pushButton_8 = QtWidgets.QPushButton(Form)
            font = QtGui.QFont()
            font.setFamily("Lato")
            font.setBold(False)
            font.setWeight(50)
            self.pushButton_8.setFont(font)
            self.pushButton_8.setObjectName("pushButton_8")
            self.verticalLayout.addWidget(self.pushButton_8)
            self.verticalLayout_22.addLayout(self.verticalLayout)
            self.gridLayout_3.addLayout(self.verticalLayout_22, 0, 0, 1, 1)

            self.comboBox.currentIndexChanged['int'].connect(self.set_LG_index)
            self.comboBox_2.currentIndexChanged['int'].connect(self.set_Y_index)

            self.lineEdit_3.editingFinished.connect(self.set_time)

            self.lineEdit_2.editingFinished.connect(self.set_x_min)
            self.lineEdit_5.editingFinished.connect(self.set_x_max)
            
            self.lineEdit.editingFinished.connect(self.set_y_min)
            self.lineEdit_4.editingFinished.connect(self.set_y_max)

            
            self.startConditionsx1 = []
            self.startConditionsx2 = []

            self.boundaryConditionsx1 = []
            self.boundaryConditionsx2 = []
            self.boundaryConditionst = []

            self.M0Conditionsx1 = []
            self.M0Conditionsx2 = []
            self.M0Conditionst = []

            self.MGConditionsx1 = []
            self.MGConditionsx2 = []
            self.MGConditionst = []
            
            self.retranslateUi(Form)
            self.tabWidget.setCurrentIndex(0)

            self.radioButton.toggled.connect(self.hideAllx2)
            self.radioButton.toggled.connect(self.set_dim)
            
            self.radioButton_2.toggled.connect(self.showAllx2)
            self.radioButton_2.toggled.connect(self.set_dim)

            self.spinBox_3.valueChanged['int'].connect(self.setMGConditions)
            self.spinBox_4.valueChanged['int'].connect(self.setM0Conditions)
            
            self.spinBox_5.valueChanged['int'].connect(self.setStartConditions)
            self.spinBox_6.valueChanged['int'].connect(self.setBoundaryConditions)

            self.pushButton_2.clicked.connect(self.set_start_conditions)
            self.pushButton_3.clicked.connect(self.set_border_conditions)
            
            self.pushButton_4.clicked.connect(self.set_points_sm0)
            self.pushButton_5.clicked.connect(self.set_points_smG)


            #пока что кнопка <<Розрахувати результат>> просто выводит все нужные нам поля в консоль
            #тут вместо "self.output" нужно будет вписать функцию, запускающую код Игоря
            self.pushButton_8.clicked.connect(self.output)
            
            QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Math Modelling", "Math Modelling"))
            Form.setWindowIcon(QIcon('stoyan.jpg'))
            self.label.setText(_translate("Form", "Math Modelling"))
            self.label_4.setText(_translate("Form", "Модель"))
            self.comboBox.setItemText(0, _translate("Form", "L1,G1"))
            self.comboBox.setItemText(1, _translate("Form", "L2,G2"))
            self.comboBox.setItemText(2, _translate("Form", "L3,G3"))
            self.label_5.setText(_translate("Form", "Функція стану процесу y(s):"))
            self.comboBox_2.setItemText(0, _translate("Form", "y1"))
            self.comboBox_2.setItemText(1, _translate("Form", "y2"))
            self.comboBox_2.setItemText(2, _translate("Form", "y3"))
            self.label_6.setText(_translate("Form", "Спостереження за системою — неперервні"))
            self.label_7.setText(_translate("Form", "Моделюючі функції — дискретні"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Модель"))
            self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("Form", "Дані про, власне, саму модель"))
            self.label_12.setText(_translate("Form", "Просторово-часова область"))
            self.label_13.setText(_translate("Form", "Час закінчення процесу:"))
            self.label_14.setText(_translate("Form", "Координатні змінні:"))
            self.radioButton.setText(_translate("Form", "(x1)"))
            self.radioButton_2.setText(_translate("Form", "(x1, x2)"))
            self.pushButton.setText(_translate("Form", "Відмітити на графіку"))
            self.label_2.setText(_translate("Form", "a"))
            self.label_3.setText(_translate("Form", "b"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Область"))
            self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Дані про просторово-часову область"))
            self.label_39.setText(_translate("Form", "Початкові умови"))
            self.label_40.setText(_translate("Form", "Кількість:"))
            self.label_41.setText(_translate("Form", "x1"))
            self.label_42.setText(_translate("Form", "x2"))
            self.label_43.setText(_translate("Form", "Крайові умови"))
            self.label_44.setText(_translate("Form", "Кількість:"))
            self.label_45.setText(_translate("Form", "x1"))
            self.label_46.setText(_translate("Form", "x2"))
            self.pushButton_2.setText(_translate("Form", "Зберегти"))
            self.pushButton_3.setText(_translate("Form", "Зберегти"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Умови"))
            self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Початкові та крайові умови"))
            self.label_29.setText(_translate("Form", "Точки для моделюючої функції u0"))
            self.label_34.setText(_translate("Form", "Кількість (M0):"))
            self.label_8.setText(_translate("Form", "x1"))
            self.label_9.setText(_translate("Form", "x2"))
            self.label_10.setText(_translate("Form", "t"))
            self.pushButton_4.setText(_translate("Form", "Зберегти"))
            self.label_32.setText(_translate("Form", "Точки для моделюючої функції uг"))
            self.label_28.setText(_translate("Form", "Кількість (MГ):"))
            self.label_11.setText(_translate("Form", "x1"))
            self.label_15.setText(_translate("Form", "x2"))
            self.label_16.setText(_translate("Form", "t"))
            self.label_18.setText(_translate("Form", "t"))
            self.pushButton_5.setText(_translate("Form", "Зберегти"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "М-змінні"))
            self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_3), _translate("Form", "M0, MГ"))
            self.pushButton_8.setText(_translate("Form", "Розрахувати результат"))



        #устанавливает количество начальных условий в соответствии с выбранным числом в spinBox_5
        #добавляет/удаляет поля ввода в списках startConditionsx1 (...x2)
        def setStartConditions(self, Form):
            l = len(self.startConditionsx1)
            n = self.spinBox_5.value()
            if n:
                if l < n:
                    for i in range (l,n):
                        self.startConditionsx1.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_28.addWidget(self.startConditionsx1[i])
                        self.startConditionsx1[i].setText("0")
                        self.startConditionsx2.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_29.addWidget(self.startConditionsx2[i])
                        self.startConditionsx2[i].setText("0")
                        if self.radioButton.isChecked():
                            self.startConditionsx2[i].hide()

                        
                if l > n:
                    for i in range(0,l-n):
                        self.startConditionsx1[-1].hide()
                        self.verticalLayout_28.removeWidget(self.startConditionsx1[-1])
                        self.startConditionsx1.pop()
                        self.startConditionsx2[-1].hide()
                        self.verticalLayout_29.removeWidget(self.startConditionsx2[-1])
                        self.startConditionsx2.pop()
            else:
                for i in range(l):
                    self.startConditionsx1[i].hide()
                    self.startConditionsx2[i].hide()
                    self.verticalLayout_28.removeWidget(self.startConditionsx1[i])
                    self.verticalLayout_29.removeWidget(self.startConditionsx2[i])
                for i in range(l):
                    self.startConditionsx1.pop()
                    self.startConditionsx2.pop()

                
            if self.radioButton.isChecked():
                for i in self.startConditionsx2:
                    i.hide()
            else:
                for i in self.startConditionsx2:
                    i.show()


        #устанавливает количество краевых условий в соответствии с выбранным числом в spinBox_6
        #добавляет/удаляет поля ввода в списках boundaryConditionsx1 (...x2)
        def setBoundaryConditions(self, Form):
            l = len(self.boundaryConditionsx1)
            n = self.spinBox_6.value()
            if n:
                if l < n:
                    for i in range (l,n):
                        self.boundaryConditionsx1.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_32.addWidget(self.boundaryConditionsx1[i])
                        self.boundaryConditionsx1[i].setText("0")
                        self.boundaryConditionsx2.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_33.addWidget(self.boundaryConditionsx2[i])
                        self.boundaryConditionsx2[i].setText("0")
                        self.boundaryConditionst.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_8.addWidget(self.boundaryConditionst[i])
                        self.boundaryConditionst[i].setText("0")
                        if self.radioButton.isChecked():
                            self.boundaryConditionsx2[i].hide()
                        
                if l > n:
                    for i in range(0,l-n):
                        self.boundaryConditionsx1[-1].hide()
                        self.verticalLayout_32.removeWidget(self.boundaryConditionsx1[-1])
                        self.boundaryConditionsx1.pop()
                        self.boundaryConditionsx2[-1].hide()
                        self.verticalLayout_33.removeWidget(self.boundaryConditionsx2[-1])
                        self.boundaryConditionsx2.pop()
                        self.boundaryConditionst[-1].hide()
                        self.verticalLayout_8.removeWidget(self.boundaryConditionst[-1])
                        self.boundaryConditionst.pop()
            else:
                for i in range(l):
                    self.boundaryConditionsx1[i].hide()
                    self.boundaryConditionsx2[i].hide()
                    self.boundaryConditionst[i].hide()
                    self.verticalLayout_32.removeWidget(self.boundaryConditionsx1[i])
                    self.verticalLayout_33.removeWidget(self.boundaryConditionsx2[i])
                    self.verticalLayout_8.removeWidget(self.boundaryConditionst[i])
                for i in range(l):
                    self.boundaryConditionsx1.pop()
                    self.boundaryConditionsx2.pop()
                    self.boundaryConditionst.pop()
                    
            if self.radioButton.isChecked():
                for i in self.boundaryConditionsx2:
                    i.hide()
            else:
                for i in self.boundaryConditionsx2:
                    i.show()

        #устанавливает количество точек для u0 в соответствии с выбранным числом в spinBox_4
        #добавляет/удаляет поля ввода в списках M0Conditionsx1 (...x2)
        def setM0Conditions(self, Form):
            l = len(self.M0Conditionsx1)
            n = self.spinBox_4.value()
            if n:
                if l < n:
                    for i in range (l,n):
                        self.M0Conditionsx1.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_14.addWidget(self.M0Conditionsx1[i])
                        self.M0Conditionsx1[i].setText("0")
                        self.M0Conditionsx2.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_23.addWidget(self.M0Conditionsx2[i])
                        self.M0Conditionsx2[i].setText("0")
                        self.M0Conditionst.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_24.addWidget(self.M0Conditionst[i])
                        self.M0Conditionst[i].setText("0")
                        if self.radioButton.isChecked():
                            self.M0Conditionsx2[i].hide()
                        
                if l > n:
                    for i in range(0,l-n):
                        self.M0Conditionsx1[-1].hide()
                        self.verticalLayout_14.removeWidget(self.M0Conditionsx1[-1])
                        self.M0Conditionsx1.pop()
                        self.M0Conditionsx2[-1].hide()
                        self.verticalLayout_23.removeWidget(self.M0Conditionsx2[-1])
                        self.M0Conditionsx2.pop()
                        self.M0Conditionst[-1].hide()
                        self.verticalLayout_24.removeWidget(self.M0Conditionst[-1])
                        self.M0Conditionst.pop()
            else:
                for i in range(l):
                    self.M0Conditionsx1[i].hide()
                    self.M0Conditionsx2[i].hide()
                    self.M0Conditionst[i].hide()
                    self.verticalLayout_14.removeWidget(self.M0Conditionsx1[i])
                    self.verticalLayout_23.removeWidget(self.M0Conditionsx2[i])
                    self.verticalLayout_24.removeWidget(self.M0Conditionst[i])
                for i in range(l):
                    self.M0Conditionsx1.pop()
                    self.M0Conditionsx2.pop()
                    self.M0Conditionst.pop()
                
            if self.radioButton.isChecked():
                for i in self.M0Conditionsx2:
                    i.hide()
            else:
                for i in self.M0Conditionsx2:
                    i.show()

        #устанавливает количество точек для ug в соответствии с выбранным числом в spinBox_3
        #добавляет/удаляет поля ввода в списках MGConditionsx1 (...x2)
        def setMGConditions(self, Form):
            l = len(self.MGConditionsx1)
            n = self.spinBox_3.value()
            if n:
                if l < n:
                    for i in range (l,n):
                        self.MGConditionsx1.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_25.addWidget(self.MGConditionsx1[i])
                        self.MGConditionsx1[i].setText("0")
                        self.MGConditionsx2.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.verticalLayout_34.addWidget(self.MGConditionsx2[i])
                        self.MGConditionsx2[i].setText("0")
                        self.MGConditionst.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4))
                        self.MGConditionst[i].setText("0")
                        self.verticalLayout_35.addWidget(self.MGConditionst[i])
                        if self.radioButton.isChecked():
                            self.MGConditionsx2[i].hide()
                    
                if l > n:
                    for i in range(0,l-n):
                        self.MGConditionsx1[-1].hide()
                        self.verticalLayout_25.removeWidget(self.MGConditionsx1[-1])
                        self.MGConditionsx1.pop()
                        self.MGConditionsx2[-1].hide()
                        self.verticalLayout_34.removeWidget(self.MGConditionsx2[-1])
                        self.MGConditionsx2.pop()
                        self.MGConditionst[-1].hide()
                        self.verticalLayout_35.removeWidget(self.MGConditionst[-1])
                        self.MGConditionst.pop()
            else:
                for i in range(l):
                    self.MGConditionsx1[i].hide()
                    self.MGConditionsx2[i].hide()
                    self.MGConditionst[i].hide()
                    self.verticalLayout_25.removeWidget(self.MGConditionsx1[i])
                    self.verticalLayout_34.removeWidget(self.MGConditionsx2[i])
                    self.verticalLayout_35.removeWidget(self.MGConditionst[i])
                for i in range(l):
                    self.MGConditionsx1.pop()
                    self.MGConditionsx2.pop()
                    self.MGConditionst.pop()
                
            if self.radioButton.isChecked():
                for i in self.MGConditionsx2:
                    i.hide()
            else:
                for i in self.MGConditionsx2:
                    i.show()
        
        #прячет все x2, когда пользователь хочет только одну пространственную переменную
        def hideAllx2(self,Form):
            self.lineEdit_4.hide()
            self.lineEdit.hide()
            self.label_42.hide()
            self.label_46.hide()
            self.label_9.hide()
            self.label_15.hide()
            self.line_7.hide()
            self.line_9.hide()
            self.line_12.hide()
            self.line_13.hide()
            if len(self.startConditionsx2):
                for i in self.startConditionsx2:
                    i.hide()
            if len(self.boundaryConditionsx2):
                for i in self.boundaryConditionsx2:
                    i.hide()
            if len(self.M0Conditionsx2):
                for i in self.M0Conditionsx2:
                    i.hide()
            if len(self.MGConditionsx2):
                for i in self.MGConditionsx2:
                    i.hide()

        #показывает все х2, когда пользователь хочет обе пространственные переменные
        def showAllx2(self, Form):
            self.lineEdit_4.show()
            self.lineEdit.show()
            self.label_42.show()
            self.label_46.show()
            self.label_9.show()
            self.label_15.show()
            self.line_7.show()
            self.line_9.show()
            self.line_12.show()
            self.line_13.show()
            if len(self.startConditionsx2):
                for i in self.startConditionsx2:
                    i.show()
            if len(self.boundaryConditionsx2):
                for i in self.boundaryConditionsx2:
                    i.show()
            if len(self.M0Conditionsx2):
                for i in self.M0Conditionsx2:
                    i.show()
            if len(self.MGConditionsx2):
                for i in self.MGConditionsx2:
                    i.show()


        #следующие функции вызываются при нажатии на кнопки/изменениях в полях ввода
        def set_LG_index(self):
            self.LG_index = self.comboBox.currentIndex()

        def set_Y_index(self):
            self.Y_index = self.comboBox_2.currentIndex()

        def set_time(self):
            self.time = float(self.lineEdit_3.text())

        def set_dim(self):
            if self.radioButton.isChecked(): self.dim = 2
            if self.radioButton_2.isChecked(): self.dim = 3

        def set_x_min(self):
            self.x_min = float(self.lineEdit_2.text())

        def set_x_max(self):
            self.x_max = float(self.lineEdit_5.text())

        def set_y_min(self):
            self.y_min = float(self.lineEdit.text())

        def set_y_max(self):
            self.y_max = float(self.lineEdit_4.text())

        def set_start_conditions(self):
            self.start_conditions.clear()
            for i in range(len(self.startConditionsx1)):
                if self.startConditionsx1[i].text() and self.startConditionsx2[i].text(): self.start_conditions.append((float(self.startConditionsx1[i].text()),float(self.startConditionsx2[i].text()),0))
                else: self.start_conditions.append((0,0,0))

        def set_border_conditions(self):
            self.border_conditions.clear()
            for i in range(len(self.boundaryConditionsx1)):
                if self.boundaryConditionsx1[i].text() and self.boundaryConditionsx2[i].text() and self.boundaryConditionst[i].text(): self.border_conditions.append((float(self.boundaryConditionsx1[i].text()),float(self.boundaryConditionsx2[i].text()),float(self.boundaryConditionst[i].text())))
                else: self.border_conditions.append((0,0,0))

        def set_points_sm0(self):
            self.points_sm0.clear()
            for i in range(len(self.M0Conditionsx1)):
                if self.M0Conditionsx1[i].text() and self.M0Conditionsx2[i].text() and self.M0Conditionst[i].text(): self.points_sm0.append((float(self.M0Conditionsx1[i].text()),float(self.M0Conditionsx2[i].text()),float(self.M0Conditionst[i].text())))
                else: self.points_sm0.append((0,0,0))

        def set_points_smG(self):
            self.points_smG.clear()
            for i in range(len(self.MGConditionsx1)):
                if self.MGConditionsx1[i].text() and self.MGConditionsx2[i].text() and self.MGConditionst[i].text(): self.points_smG.append((float(self.MGConditionsx1[i].text()),float(self.MGConditionsx2[i].text()),float(self.MGConditionst[i].text())))
                else: self.points_smG.append((0,0,0))
            

        def output(self):
            if self.dim == 2:
                new_start_conditions = list(map(lambda x: (x[0], x[2]), self.start_conditions))
                new_border_conditions = list(map(lambda x: (x[0], x[2]), self.border_conditions))
                new_points_sm0 = list(map(lambda x: (x[0], x[2]), self.points_sm0))
                new_points_smG = list(map(lambda x: (x[0], x[2]), self.points_smG))
            else:
                new_start_conditions = self.start_conditions
                new_border_conditions = self.border_conditions
                new_points_sm0 = self.points_sm0
                new_points_smG = self.points_smG
            
            print(self.LG_index)
            print(self.Y_index)
            print(self.time)
            print(self.dim)
            print(self.x_min, self.x_max, self.y_min, self.y_max)
            print(new_start_conditions)
            print(new_border_conditions)
            print(new_points_sm0)
            print(new_points_smG)
        
                
            model = Model(self.dim, self.LG_index, self.Y_index,  self.time, self.x_min, self.x_max, self.y_min, self.y_max)
            
            model.set_start_conditions(new_start_conditions)
            model.set_border_conditions(new_border_conditions)
            model.set_points_sm0(new_points_sm0)
            model.set_points_smG(new_points_smG)
            model.demo()
            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

