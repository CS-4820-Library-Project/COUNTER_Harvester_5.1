# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchTab.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(819, 591)
        Search.setStyleSheet("*{\n"
"    \n"
"    \n"
"border:none;\n"
"background-color:transparent;\n"
"background:none;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"}\n"
"\n"
"\n"
"\n"
"#Search{\n"
"background-color: #1f232a;\n"
"}\n"
"#EditVendor{\n"
"background-color:#16191d;\n"
"}\n"
"QPushButton{\n"
"text-align:left;\n"
"padding: 5px 10px;\n"
"\n"
"border-top-left-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"text-align:left;\n"
"padding:2px 10px;\n"
"color:white;}")
        self.gridLayout_8 = QtWidgets.QGridLayout(Search)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.centralwidget = QtWidgets.QWidget(Search)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame{\n"
"    border: 2px solid #000000;\n"
"border-color:grey;\n"
"border-radius:15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none")
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 0, 5, 1, 1)
        self.end_month_comboBox = QtWidgets.QComboBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.end_month_comboBox.setFont(font)
        self.end_month_comboBox.setStyleSheet("color:white;\n"
"border-radius: 0px;\n"
"background: #2E2F30;\n"
"padding-left: 5px;")
        self.end_month_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.end_month_comboBox.setMinimumContentsLength(10)
        self.end_month_comboBox.setObjectName("end_month_comboBox")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.end_month_comboBox.addItem("")
        self.gridLayout_7.addWidget(self.end_month_comboBox, 0, 8, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:none")
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 7, 1, 1)
        self.start_month_comboBox = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_month_comboBox.sizePolicy().hasHeightForWidth())
        self.start_month_comboBox.setSizePolicy(sizePolicy)
        self.start_month_comboBox.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.start_month_comboBox.setFont(font)
        self.start_month_comboBox.setStyleSheet("color:white;\n"
"border-radius: 0px;\n"
"background: #2E2F30;\n"
"padding-left: 5px;")
        self.start_month_comboBox.setEditable(False)
        self.start_month_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.start_month_comboBox.setMinimumContentsLength(10)
        self.start_month_comboBox.setFrame(True)
        self.start_month_comboBox.setObjectName("start_month_comboBox")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.start_month_comboBox.addItem("")
        self.gridLayout_7.addWidget(self.start_month_comboBox, 0, 3, 1, 1)
        self.start_year_edit = QtWidgets.QDateEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_year_edit.sizePolicy().hasHeightForWidth())
        self.start_year_edit.setSizePolicy(sizePolicy)
        self.start_year_edit.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_year_edit.setFont(font)
        self.start_year_edit.setStyleSheet("QDateEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-button {\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QDateEdit::up-button {\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QDateEdit::up-arrow, QDateEdit::down-arrow {\n"
"    border: 5px solid rgba(255, 255, 255, 0);\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QDateEdit::up-arrow {\n"
"    border-top: none;\n"
"    border-bottom-color: white;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    border-bottom: none;\n"
"    border-top-color: white;\n"
"}")
        self.start_year_edit.setObjectName("start_year_edit")
        self.gridLayout_7.addWidget(self.start_year_edit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none")
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 2, 1, 1)
        self.end_year_edit = QtWidgets.QDateEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_year_edit.sizePolicy().hasHeightForWidth())
        self.end_year_edit.setSizePolicy(sizePolicy)
        self.end_year_edit.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.end_year_edit.setFont(font)
        self.end_year_edit.setStyleSheet("QDateEdit {\n"
"background-color: #2E2F30;\n"
"    border: 2px solid #808080;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-button {\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QDateEdit::up-button {\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QDateEdit::up-arrow, QDateEdit::down-arrow {\n"
"    border: 5px solid rgba(255, 255, 255, 0);\n"
"    width: 0;\n"
"    height: 0;\n"
"}\n"
"\n"
"QDateEdit::up-arrow {\n"
"    border-top: none;\n"
"    border-bottom-color: white;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    border-bottom: none;\n"
"    border-top-color: white;\n"
"}")
        self.end_year_edit.setObjectName("end_year_edit")
        self.gridLayout_7.addWidget(self.end_year_edit, 0, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none")
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.frame_4)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.horizontalFrame.setStyleSheet("border-radius: 8px;padding: 4px;")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_type = QtWidgets.QComboBox(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_type.sizePolicy().hasHeightForWidth())
        self.search_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.search_type.setFont(font)
        self.search_type.setStyleSheet("QComboBox{\n"
"    color: white;\n"
"border-radius: 0px;\n"
"background: #2E2F30;\n"
"padding-left: 10px;\n"
"padding-right: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: white;\n"
"    background-color: #2E2F30;\n"
"}\n"
"\n"
"\n"
"")
        self.search_type.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.search_type.setMinimumContentsLength(15)
        self.search_type.setObjectName("search_type")
        self.search_type.addItem("")
        self.search_type.addItem("")
        self.search_type.addItem("")
        self.horizontalLayout.addWidget(self.search_type)
        self.input_search_edit = QtWidgets.QLineEdit(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_search_edit.sizePolicy().hasHeightForWidth())
        self.input_search_edit.setSizePolicy(sizePolicy)
        self.input_search_edit.setMinimumSize(QtCore.QSize(0, 20))
        self.input_search_edit.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(1)
        self.input_search_edit.setFont(font)
        self.input_search_edit.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    background-color: #2E2F30;\n"
" border-radius:4px;\n"
"padding: 5px;\n"
"font-size: 14px;\n"
"padding-left: 14px;\n"
"}\n"
"")
        self.input_search_edit.setObjectName("input_search_edit")
        self.horizontalLayout.addWidget(self.input_search_edit)
        self.gridLayout.addWidget(self.horizontalFrame, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.result_summary_edit = QtWidgets.QLabel(self.frame_4)
        self.result_summary_edit.setStyleSheet("border: none;\n"
"font-size: 18px;")
        self.result_summary_edit.setObjectName("result_summary_edit")
        self.gridLayout.addWidget(self.result_summary_edit, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_4)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.widget_3)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.save_folder_button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.save_folder_button.setFont(font)
        self.save_folder_button.setAutoFillBackground(False)
        self.save_folder_button.setStyleSheet("QPushButton {\n"
"    background-color: #1768E3; \n"
"    color: #FFFFFF;\n"
"    font: bold;\n"
"   border-radius: 6px;\n"
"text-align: center;\n"
"padding: 14px;\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Final Project/COUNTER-Release-5.1/ui/resources/Icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_folder_button.setIcon(icon)
        self.save_folder_button.setIconSize(QtCore.QSize(28, 28))
        self.save_folder_button.setShortcut("")
        self.save_folder_button.setObjectName("save_folder_button")
        self.gridLayout_5.addWidget(self.save_folder_button, 0, 1, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.search_button.setFont(font)
        self.search_button.setAutoFillBackground(False)
        self.search_button.setStyleSheet("QPushButton {\n"
"    background-color: #1768E3; \n"
"    color: #FFFFFF;\n"
"    font: bold;\n"
"   border-radius: 6px;\n"
"text-align: center;\n"
"padding: 14px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Final Project/COUNTER-Release-5.1/ui/resources/loupe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setIconSize(QtCore.QSize(28, 28))
        self.search_button.setShortcut("")
        self.search_button.setObjectName("search_button")
        self.gridLayout_5.addWidget(self.search_button, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_3, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.centralwidget, 0, 0, 1, 1)

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)
        Search.setTabOrder(self.start_year_edit, self.start_month_comboBox)
        Search.setTabOrder(self.start_month_comboBox, self.end_year_edit)
        Search.setTabOrder(self.end_year_edit, self.end_month_comboBox)
        Search.setTabOrder(self.end_month_comboBox, self.search_type)
        Search.setTabOrder(self.search_type, self.input_search_edit)
        Search.setTabOrder(self.input_search_edit, self.search_button)
        Search.setTabOrder(self.search_button, self.save_folder_button)

    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "MainWindow"))
        self.label.setText(_translate("Search", "<html><head/><body><p align=\"center\">Search {TR Reports}</p></body></html>"))
        self.label_5.setText(_translate("Search", "<html><head/><body><p align=\"right\">End Year</p></body></html>"))
        self.end_month_comboBox.setItemText(0, _translate("Search", "January"))
        self.end_month_comboBox.setItemText(1, _translate("Search", "February"))
        self.end_month_comboBox.setItemText(2, _translate("Search", "March"))
        self.end_month_comboBox.setItemText(3, _translate("Search", "April"))
        self.end_month_comboBox.setItemText(4, _translate("Search", "May"))
        self.end_month_comboBox.setItemText(5, _translate("Search", "June"))
        self.end_month_comboBox.setItemText(6, _translate("Search", "July"))
        self.end_month_comboBox.setItemText(7, _translate("Search", "August"))
        self.end_month_comboBox.setItemText(8, _translate("Search", "September"))
        self.end_month_comboBox.setItemText(9, _translate("Search", "October"))
        self.end_month_comboBox.setItemText(10, _translate("Search", "November"))
        self.end_month_comboBox.setItemText(11, _translate("Search", "December"))
        self.label_6.setText(_translate("Search", "<html><head/><body><p align=\"right\">End Month</p></body></html>"))
        self.start_month_comboBox.setItemText(0, _translate("Search", "January"))
        self.start_month_comboBox.setItemText(1, _translate("Search", "February"))
        self.start_month_comboBox.setItemText(2, _translate("Search", "March"))
        self.start_month_comboBox.setItemText(3, _translate("Search", "April"))
        self.start_month_comboBox.setItemText(4, _translate("Search", "May"))
        self.start_month_comboBox.setItemText(5, _translate("Search", "June"))
        self.start_month_comboBox.setItemText(6, _translate("Search", "July"))
        self.start_month_comboBox.setItemText(7, _translate("Search", "August"))
        self.start_month_comboBox.setItemText(8, _translate("Search", "September"))
        self.start_month_comboBox.setItemText(9, _translate("Search", "October"))
        self.start_month_comboBox.setItemText(10, _translate("Search", "November"))
        self.start_month_comboBox.setItemText(11, _translate("Search", "December"))
        self.start_year_edit.setDisplayFormat(_translate("Search", "yyyy"))
        self.label_2.setText(_translate("Search", "<html><head/><body><p align=\"right\">Start Month</p></body></html>"))
        self.end_year_edit.setDisplayFormat(_translate("Search", "yyyy"))
        self.label_4.setText(_translate("Search", "<html><head/><body><p align=\"right\">Start Year</p></body></html>"))
        self.search_type.setItemText(0, _translate("Search", "Title Substring"))
        self.search_type.setItemText(1, _translate("Search", "ISSN"))
        self.search_type.setItemText(2, _translate("Search", "ISBN"))
        self.input_search_edit.setPlaceholderText(_translate("Search", "Please input the Title/ISSN/ISBN "))
        self.label_3.setText(_translate("Search", "Title Search"))
        self.result_summary_edit.setText(_translate("Search", "No Search Results"))
        self.save_folder_button.setText(_translate("Search", "Go To Save Folder"))
        self.search_button.setText(_translate("Search", "Search"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search = QtWidgets.QWidget()
    ui = Ui_Search()
    ui.setupUi(Search)
    Search.show()
    sys.exit(app.exec_())
