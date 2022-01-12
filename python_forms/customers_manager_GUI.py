# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/customers_manager_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_customers_management_window(object):
    def setupUi(self, customers_management_window):
        customers_management_window.setObjectName("customers_management_window")
        customers_management_window.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(customers_management_window.sizePolicy().hasHeightForWidth())
        customers_management_window.setSizePolicy(sizePolicy)
        customers_management_window.setMinimumSize(QtCore.QSize(1000, 800))
        customers_management_window.setMaximumSize(QtCore.QSize(1000000, 1000000))
        customers_management_window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(customers_management_window)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"  background-color: #838383;\n"
"  border: none;\n"
"  color: black;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #585858;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(54, 54, 54);\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.name_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_line_edit.sizePolicy().hasHeightForWidth())
        self.name_line_edit.setSizePolicy(sizePolicy)
        self.name_line_edit.setMinimumSize(QtCore.QSize(194, 50))
        self.name_line_edit.setMaximumSize(QtCore.QSize(194, 50))
        self.name_line_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_line_edit.setStyleSheet("background-color:white;")
        self.name_line_edit.setObjectName("name_line_edit")
        self.horizontalLayout.addWidget(self.name_line_edit)
        self.search_customer_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_customer_btn.sizePolicy().hasHeightForWidth())
        self.search_customer_btn.setSizePolicy(sizePolicy)
        self.search_customer_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.search_customer_btn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.search_customer_btn.setFont(font)
        self.search_customer_btn.setAutoFillBackground(False)
        self.search_customer_btn.setStyleSheet("")
        self.search_customer_btn.setObjectName("search_customer_btn")
        self.horizontalLayout.addWidget(self.search_customer_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.email_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_line_edit.sizePolicy().hasHeightForWidth())
        self.email_line_edit.setSizePolicy(sizePolicy)
        self.email_line_edit.setMinimumSize(QtCore.QSize(194, 50))
        self.email_line_edit.setMaximumSize(QtCore.QSize(194, 50))
        self.email_line_edit.setStyleSheet("background-color:white;")
        self.email_line_edit.setObjectName("email_line_edit")
        self.horizontalLayout_2.addWidget(self.email_line_edit)
        self.phone_number_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_number_line_edit.sizePolicy().hasHeightForWidth())
        self.phone_number_line_edit.setSizePolicy(sizePolicy)
        self.phone_number_line_edit.setMinimumSize(QtCore.QSize(194, 50))
        self.phone_number_line_edit.setMaximumSize(QtCore.QSize(194, 50))
        self.phone_number_line_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.phone_number_line_edit.setStyleSheet("background-color:white;")
        self.phone_number_line_edit.setObjectName("phone_number_line_edit")
        self.horizontalLayout_2.addWidget(self.phone_number_line_edit)
        self.add_customer_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_customer_btn.sizePolicy().hasHeightForWidth())
        self.add_customer_btn.setSizePolicy(sizePolicy)
        self.add_customer_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.add_customer_btn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.add_customer_btn.setFont(font)
        self.add_customer_btn.setStyleSheet("")
        self.add_customer_btn.setObjectName("add_customer_btn")
        self.horizontalLayout_2.addWidget(self.add_customer_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.customers_table_view = QtWidgets.QTableView(self.centralwidget)
        self.customers_table_view.setObjectName("customers_table_view")
        self.verticalLayout.addWidget(self.customers_table_view)
        customers_management_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(customers_management_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 19))
        self.menubar.setObjectName("menubar")
        customers_management_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(customers_management_window)
        self.statusbar.setObjectName("statusbar")
        customers_management_window.setStatusBar(self.statusbar)

        self.retranslateUi(customers_management_window)
        QtCore.QMetaObject.connectSlotsByName(customers_management_window)

    def retranslateUi(self, customers_management_window):
        _translate = QtCore.QCoreApplication.translate
        customers_management_window.setWindowTitle(_translate("customers_management_window", "Customers management"))
        self.name_line_edit.setPlaceholderText(_translate("customers_management_window", "Name"))
        self.search_customer_btn.setText(_translate("customers_management_window", "Search"))
        self.email_line_edit.setPlaceholderText(_translate("customers_management_window", "Email"))
        self.phone_number_line_edit.setPlaceholderText(_translate("customers_management_window", "Phone number"))
        self.add_customer_btn.setText(_translate("customers_management_window", "Add new customer"))
