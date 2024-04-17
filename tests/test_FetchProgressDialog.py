import unittest
import sys

sys.path.insert(0, "/Users/karan/Downloads/UPEI/UPEI STUDY/Winter 2024/Counter-Harvesting-Tool-5.1")
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from ui import FetchProgressDialog

app = QApplication(sys.argv)
fetch_progress_dialog = QMainWindow()
fetch_progress_dialog_ui = FetchProgressDialog.Ui_FetchProgressDialog()
fetch_progress_dialog_ui.setupUi(fetch_progress_dialog)


class FetchProgressDialogTests(unittest.TestCase):
    def test_defaults(self):
        """Test the defaults"""
        doc = QTextDocument()
        doc.setHtml(fetch_progress_dialog_ui.status_label.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Fetching...")

        self.assertEqual(fetch_progress_dialog_ui.progress_bar.value(), 20)

        self.assertEqual(fetch_progress_dialog_ui.log_file_button.text(), "Log File")


    def test_ok_button(self):
        okWidget = fetch_progress_dialog_ui.buttonBox.Ok
        self.assertIsNotNone(okWidget)
        cancelWidget = fetch_progress_dialog_ui.buttonBox.Cancel
        self.assertIsNotNone(cancelWidget)


if __name__ == "__main__":
    unittest.main()
