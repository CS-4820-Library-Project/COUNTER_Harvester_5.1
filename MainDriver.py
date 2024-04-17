from ast import main
from json import load
import locale
import sys
import os
from dotenv import load_dotenv
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QDialog,
    QVBoxLayout,
    QLabel,
    QDialogButtonBox,
    QMessageBox,
    QLineEdit,
)
import ManageDB
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
import os
from Search import SearchController
from Settings import SettingsController
from ui import (
    MainWindow,
    ManageVendorsTab,
    FetchReportsTab,
    SearchTab,
    Settingtab,
)
from ManageVendors import ManageVendorsController
from FetchReports import FetchReportsController
import GeneralUtils
import hashlib

load_dotenv()


def trap_exc_during_debug(*args):
    # when app raises an uncaught exception, print info
    pass
    # print(args)


# install exception hook: without this, uncaught exception would cause the application to exit
sys.excepthook = trap_exc_during_debug

# endregion

if hasattr(Qt, "AA_EnableHighDpiScaling"):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, "AA_UseHighDpiPixmaps"):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


def trap_exc_during_debug(*args):
    # when app raises an uncaught exception, print info
    pass
    # print(args)


# install exception hook: without this, uncaught exception would cause the application to exit
sys.excepthook = trap_exc_during_debug

# endregion

if hasattr(Qt, "AA_EnableHighDpiScaling"):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, "AA_UseHighDpiPixmaps"):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

authorized = False


class PasswordDialog(QDialog):
    def __init__(self, parent=None):
        super(PasswordDialog, self).__init__(parent)
        self.setWindowTitle("Enter Password")
        self.setGeometry(200, 200, 300, 100)

        layout = QVBoxLayout()

        self.label = QLabel("Enter password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def check_password(self, hash_pass):
        entered_password = self.password_input.text()
        input_hash = hashlib.md5(entered_password.encode("utf8")).hexdigest()
        if input_hash == hash_pass:
            global authorized
            authorized = True
        return input_hash == hash_pass

    def accept(self):
        correct_password_hash = os.getenv("MANAGE_VENDOR_PASSWORD_HASH")
        if self.check_password(correct_password_hash):
            super().accept()
        else:
            QMessageBox.warning(
                self, "Access Denied", "Incorrect password. Access denied."
            )


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget {font-family: Segoe UI; font-size: 12pt;}")

    main_window = QMainWindow()
    main_window_ui = MainWindow.Ui_mainWindow()
    main_window_ui.setupUi(main_window)

    settings_tab = QWidget(main_window)
    settings_ui = Settingtab.Ui_SettingTab()
    settings_ui.setupUi(settings_tab)
    settings_controller = SettingsController(settings_tab, settings_ui)

    manage_vendors_tab = QWidget(main_window)
    manage_vendors_ui = ManageVendorsTab.Ui_manage_vendor_tab()
    manage_vendors_ui.setupUi(manage_vendors_tab)
    manage_vendors_controller = ManageVendorsController(
        manage_vendors_tab, manage_vendors_ui, settings_controller.settings
    )

    def show_manage_vendors():
        password_dialog = PasswordDialog()
        if password_dialog.exec_() == QDialog.Accepted or authorized:
            main_window_ui.tab_widget.setCurrentWidget(manage_vendors_tab)
        else:
            QMessageBox.warning(
                main_window,
                "Access Denied",
                "Incorrect password. Access to 'Manage Vendors' denied.",
            )

    def handle_tab_change(index):
        if index == 0 and authorized == False:  # Index of "Manage Vendors" tab
            password_dialog = PasswordDialog()
            if password_dialog.exec_() != QDialog.Accepted:
                main_window_ui.tab_widget.setCurrentIndex(
                    1
                )  # Switch to another tab (index 1) if password is incorrect
                return
        # Allow changing to the selected tab
        if index == 1:
            fetch_reports_controller.update_vendors(manage_vendors_controller.vendors_v50, manage_vendors_controller.vendors_v51)
        main_window_ui.tab_widget.setCurrentIndex(index)


    def handle_tab_change2(index):
        if index == 0 and authorized == False:
            main_window_ui.tab_widget.setCurrentIndex(1)

    main_window_ui.tab_widget.currentChanged.connect(handle_tab_change2)
    main_window_ui.tab_widget.tabBarClicked.connect(handle_tab_change)

    fetch_reports_tab = QWidget(main_window)
    fetch_reports_ui = FetchReportsTab.Ui_FetchReports()
    fetch_reports_ui.setupUi(fetch_reports_tab)
    fetch_reports_controller = FetchReportsController(
        manage_vendors_controller.vendors_v50,
        manage_vendors_controller.vendors_v51,
        settings_controller.settings,
        fetch_reports_tab,
        fetch_reports_ui,
    )

    search_tab = QWidget(main_window)
    search_ui = SearchTab.Ui_Search()
    search_ui.setupUi(search_tab)
    search_controller = SearchController(search_ui, settings_controller.settings)

    settings_controller.settings_changed_signal.connect(
        search_controller.update_settings
    )
    settings_controller.settings_changed_signal.connect(
        manage_vendors_controller.update_settings
    )
    settings_controller.settings_changed_signal.connect(
        fetch_reports_controller.update_settings
    )

    # region Add tabs to main window
    main_window_ui.tab_widget.addTab(
        manage_vendors_tab, manage_vendors_tab.windowIcon(), "Manage Vendors"
    )
    main_window_ui.tab_widget.addTab(
        fetch_reports_tab, fetch_reports_tab.windowIcon(), "Fetch Reports"
    )
    main_window_ui.tab_widget.addTab(search_tab, search_tab.windowIcon(), "Search")
    main_window_ui.tab_widget.addTab(
        settings_tab, settings_tab.windowIcon(), "Settings"
    )
    main_window_ui.tab_widget.setCurrentIndex(1)
    # endregion
    main_window.show()
    sys.exit(app.exec_())
