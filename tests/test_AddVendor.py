import unittest
import sys

sys.path.insert(0, "/Users/karan/Downloads/UPEI/UPEI STUDY/Winter 2024/Counter-Harvesting-Tool-5.1")
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from ui import AddVendor51

app = QApplication(sys.argv)
vendor_dialog = QMainWindow()
vendor_dialog_ui = AddVendor51.Ui_addVendor51Dialog()
vendor_dialog_ui.setupUi(vendor_dialog)


class AddVendorTests(unittest.TestCase):
    def test_defaults(self):
        """Test the defaults"""
        doc = QTextDocument()
        doc.setHtml(vendor_dialog_ui.label_7.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Add New Vendor")

        doc.setHtml(vendor_dialog_ui.label_15.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Version")

        doc.setHtml(vendor_dialog_ui.label.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Name")

        doc.setHtml(vendor_dialog_ui.label_2.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Base URL")

        doc.setHtml(vendor_dialog_ui.label_10.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Starting Year")

        doc.setHtml(vendor_dialog_ui.label_3.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Customer ID")

        doc.setHtml(vendor_dialog_ui.label_4.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Requester ID")

        doc.setHtml(vendor_dialog_ui.label_6.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Platform")

        doc.setHtml(vendor_dialog_ui.label_5.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "API Key")

        doc.setHtml(vendor_dialog_ui.label_8.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "2 Attempts needed")

        doc.setHtml(vendor_dialog_ui.label_9.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "IP Checking required")

        doc.setHtml(vendor_dialog_ui.label_11.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Request throttled")

        doc.setHtml(vendor_dialog_ui.provider.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Provider")

        doc.setHtml(vendor_dialog_ui.label_28.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Notes")

        doc.setHtml(vendor_dialog_ui.versionEdit.text())
        plain_text = doc.toPlainText()
        self.assertEqual(len(plain_text), 3)

        self.assertEqual(vendor_dialog_ui.nameEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.baseUrlEdit.text(), "")
        self.assertEqual(len(vendor_dialog_ui.All_reports_edit_fetch.text()), 4)
        self.assertEqual(vendor_dialog_ui.customerIdEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.requestorIdEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.platformEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.apiKeyEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.two_attempts_check_box.checkState(), False)
        self.assertEqual(vendor_dialog_ui.ip_checking_check_box.checkState(), False)
        self.assertEqual(
            vendor_dialog_ui.requests_throttled_check_box.checkState(), False
        )
        self.assertEqual(vendor_dialog_ui.providerEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.notesEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.validate_button.text(), "Validate")

    def test_ok_button(self):
        okWidget = vendor_dialog_ui.buttonBox.Ok
        self.assertIsNotNone(okWidget)
        cancelWidget = vendor_dialog_ui.buttonBox.Cancel
        self.assertIsNotNone(cancelWidget)


if __name__ == "__main__":
    unittest.main()
