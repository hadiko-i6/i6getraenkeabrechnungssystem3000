# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cashin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1008, 748)
        Form.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);\n"
"font-size:50px;")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Ok = QtWidgets.QPushButton(self.widget_2)
        self.Ok.setStyleSheet("background-color: rgb(18, 88, 35);")
        self.Ok.setObjectName("Ok")
        self.gridLayout_3.addWidget(self.Ok, 0, 0, 1, 1)
        self.Cancel = QtWidgets.QPushButton(self.widget_2)
        self.Cancel.setStyleSheet("background-color: rgb(100, 19, 19);")
        self.Cancel.setObjectName("Cancel")
        self.gridLayout_3.addWidget(self.Cancel, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 3, 1, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.num9 = QtWidgets.QPushButton(self.widget)
        self.num9.setObjectName("num9")
        self.gridLayout.addWidget(self.num9, 1, 3, 1, 1)
        self.num2 = QtWidgets.QPushButton(self.widget)
        self.num2.setObjectName("num2")
        self.gridLayout.addWidget(self.num2, 3, 2, 1, 1)
        self.num4 = QtWidgets.QPushButton(self.widget)
        self.num4.setObjectName("num4")
        self.gridLayout.addWidget(self.num4, 2, 1, 1, 1)
        self.num6 = QtWidgets.QPushButton(self.widget)
        self.num6.setObjectName("num6")
        self.gridLayout.addWidget(self.num6, 2, 3, 1, 1)
        self.num0 = QtWidgets.QPushButton(self.widget)
        self.num0.setObjectName("num0")
        self.gridLayout.addWidget(self.num0, 4, 1, 1, 3)
        self.num7 = QtWidgets.QPushButton(self.widget)
        self.num7.setObjectName("num7")
        self.gridLayout.addWidget(self.num7, 1, 1, 1, 1)
        self.num1 = QtWidgets.QPushButton(self.widget)
        self.num1.setObjectName("num1")
        self.gridLayout.addWidget(self.num1, 3, 1, 1, 1)
        self.num8 = QtWidgets.QPushButton(self.widget)
        self.num8.setObjectName("num8")
        self.gridLayout.addWidget(self.num8, 1, 2, 1, 1)
        self.num5 = QtWidgets.QPushButton(self.widget)
        self.num5.setObjectName("num5")
        self.gridLayout.addWidget(self.num5, 2, 2, 1, 1)
        self.num3 = QtWidgets.QPushButton(self.widget)
        self.num3.setObjectName("num3")
        self.gridLayout.addWidget(self.num3, 3, 3, 1, 1)
        self.Clear = QtWidgets.QPushButton(self.widget)
        self.Clear.setObjectName("Clear")
        self.gridLayout.addWidget(self.Clear, 0, 2, 1, 2)
        self.gridLayout_2.addWidget(self.widget, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 2, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        self.AmountLabel = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AmountLabel.sizePolicy().hasHeightForWidth())
        self.AmountLabel.setSizePolicy(sizePolicy)
        self.AmountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AmountLabel.setObjectName("AmountLabel")
        self.gridLayout_4.addWidget(self.AmountLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_3, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(323, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Ok.setText(_translate("Form", "Ok"))
        self.Cancel.setText(_translate("Form", "Cancel"))
        self.num9.setText(_translate("Form", "9"))
        self.num2.setText(_translate("Form", "2"))
        self.num4.setText(_translate("Form", "4"))
        self.num6.setText(_translate("Form", "6"))
        self.num0.setText(_translate("Form", "0"))
        self.num7.setText(_translate("Form", "7"))
        self.num1.setText(_translate("Form", "1"))
        self.num8.setText(_translate("Form", "8"))
        self.num5.setText(_translate("Form", "5"))
        self.num3.setText(_translate("Form", "3"))
        self.Clear.setText(_translate("Form", "Clear"))
        self.label.setText(_translate("Form", "€"))
        self.AmountLabel.setText(_translate("Form", "0.00"))
