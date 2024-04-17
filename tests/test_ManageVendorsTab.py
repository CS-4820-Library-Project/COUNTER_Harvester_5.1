import unittest
import sys
from ui import (
    MainWindow,
    ManageVendorsTab,
    FetchReportsTab,
    SearchTab,
    Settingtab,
)

sys.path.insert(0, "/Users/karan/Downloads/UPEI/UPEI STUDY/Winter 2024/Counter-Harvesting-Tool-5.1")
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from ui import ManageVendorsTab

app = QApplication(sys.argv)
manageVendorsTab_widget = QWidget()
manageVendorsTab_widget_ui = ManageVendorsTab.Ui_manage_vendor_tab()
manageVendorsTab_widget_ui.setupUi(manageVendorsTab_widget)


class ManageVendorsTabTests(unittest.TestCase):
    def test_default(self):
        """Test the defaults"""
        doc = QTextDocument()
        doc.setHtml(manageVendorsTab_widget_ui.label_13.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Select Vendor")
        self.assertEqual(manageVendorsTab_widget_ui.version51.text(), "Version 5.1")
        self.assertEqual(manageVendorsTab_widget_ui.version50.text(), "Version 5.0")
        self.assertEqual(
            manageVendorsTab_widget_ui.addVendorButton.text(), "Add New Vendor"
        )
        self.assertEqual(
            manageVendorsTab_widget_ui.importVendorsButton.text(), "Import Vendors"
        )
        self.assertEqual(
            manageVendorsTab_widget_ui.exportVendorsButton.text(), "Export Vendors"
        )
        self.assertEqual(manageVendorsTab_widget_ui.editvendorsbutton.text(), "Edit Vendor")

if __name__ == "__main__":
    unittest.main()
