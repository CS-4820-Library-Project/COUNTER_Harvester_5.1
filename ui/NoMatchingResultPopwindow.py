# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoMatchingResultPopwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_noResultFound(object):
    def setupUi(self, noResultFound):
        noResultFound.setObjectName("noResultFound")
        noResultFound.resize(630, 143)
        noResultFound.setStyleSheet("*{\n"
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
"#centralwidget{\n"
"background-color:#1f232a;\n"
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
        self.centralwidget = QtWidgets.QWidget(noResultFound)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        noResultFound.setCentralWidget(self.centralwidget)

        self.retranslateUi(noResultFound)
        QtCore.QMetaObject.connectSlotsByName(noResultFound)

    def retranslateUi(self, noResultFound):
        _translate = QtCore.QCoreApplication.translate
        noResultFound.setWindowTitle(_translate("noResultFound", "MainWindow"))
        self.label.setText(_translate("noResultFound", "No matches found"))
        self.pushButton.setText(_translate("noResultFound", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    noResultFound = QtWidgets.QMainWindow()
    ui = Ui_noResultFound()
    ui.setupUi(noResultFound)
    noResultFound.show()
    sys.exit(app.exec_())