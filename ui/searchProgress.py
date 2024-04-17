# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchProgress.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, searchProgress):
        searchProgress.setObjectName("searchProgress")
        searchProgress.setGeometry(QtCore.QRect(0, 0, 911, 585))
        searchProgress.setStyleSheet("*{\n"
"    \n"
"    \n"
"border:none;\n"
"background-color:transparent;\n"
"background:none;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"font-family:georgia;\n"
"}\n"
"\n"
"\n"
"\n"
"#centralwidget{\n"
"background-color: #1f232a;\n"
"}\n"
"#EditVendor{\n"
"background-color:#16191d;\n"
"}\n"
"QPushButton{\n"
"text-align:center;\n"
"border:2px solid grey;\n"
"border-radius:15px;\n"
"padding: 5px 10px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"\n"
"padding:2px 10px;\n"
"color:white;}")
        self.centralwidget = QtWidgets.QWidget(searchProgress)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("georgia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("text-align:center;")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(sizePolicy)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout_3.addWidget(self.progress_bar, 1, 0, 1, 1)
        self.results_scroll_area = QtWidgets.QScrollArea(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_scroll_area.sizePolicy().hasHeightForWidth())
        self.results_scroll_area.setSizePolicy(sizePolicy)
        self.results_scroll_area.setWidgetResizable(True)
        self.results_scroll_area.setObjectName("results_scroll_area")
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 661, 85))
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")
        self.scroll_area_vertical_layout = QtWidgets.QVBoxLayout(self.scroll_area_widget_contents)
        self.scroll_area_vertical_layout.setObjectName("scroll_area_vertical_layout")
        self.results_scroll_area.setWidget(self.scroll_area_widget_contents)
        self.gridLayout_3.addWidget(self.results_scroll_area, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ExportButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("georgia")
        font.setPointSize(10)
        self.ExportButton.setFont(font)
        self.ExportButton.setStyleSheet("padding-right:5px;")
        self.ExportButton.setObjectName("ExportButton")
        self.gridLayout_2.addWidget(self.ExportButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(570, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.DoneButton = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DoneButton.sizePolicy().hasHeightForWidth())
        self.DoneButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("georgia")
        font.setPointSize(10)
        self.DoneButton.setFont(font)
        self.DoneButton.setStyleSheet("padding-left:5px;")
        self.DoneButton.setObjectName("DoneButton")
        self.gridLayout_2.addWidget(self.DoneButton, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        searchProgress.setCentralWidget(self.centralwidget)

        self.retranslateUi(searchProgress)
        QtCore.QMetaObject.connectSlotsByName(searchProgress)

    def retranslateUi(self, searchProgress):
        _translate = QtCore.QCoreApplication.translate
        searchProgress.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Search Progress</p></body></html>"))
        self.ExportButton.setText(_translate("MainWindow", "Export"))
        self.DoneButton.setText(_translate("MainWindow", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searchProgress = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(searchProgress)
    searchProgress.show()
    sys.exit(app.exec_())
