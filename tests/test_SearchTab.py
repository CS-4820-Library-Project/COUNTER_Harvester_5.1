import unittest
import sys

sys.path.insert(0, "/Users/karan/Downloads/UPEI/UPEI STUDY/Winter 2024/Counter-Harvesting-Tool-5.1")
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from ui import SearchTab

app = QApplication(sys.argv)
search_tab = QMainWindow()
search_tab_ui = SearchTab.Ui_Search()
search_tab_ui.setupUi(search_tab)


class SearchTabTests(unittest.TestCase):
    def test_defaults(self):
        """Test the defaults"""
        doc = QTextDocument()
        doc.setHtml(search_tab_ui.label.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Search {TR Reports}")

        doc.setHtml(search_tab_ui.label_4.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Start Year")

        doc.setHtml(search_tab_ui.label_2.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Start Month")

        doc.setHtml(search_tab_ui.label_5.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "End Year")

        doc.setHtml(search_tab_ui.label_6.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "End Month")

        doc.setHtml(search_tab_ui.label_3.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Title Search")

        doc.setHtml(search_tab_ui.result_summary_edit.text())
        plain_text = doc.toPlainText()
        self.assertNotEqual(len(plain_text), 0)

        self.assertEqual(len(search_tab_ui.start_year_edit.text()), 4)
        self.assertEqual(search_tab_ui.start_month_comboBox.currentText(), "January")
        self.assertEqual(len(search_tab_ui.end_year_edit.text()), 4)
        self.assertEqual(search_tab_ui.end_month_comboBox.currentText(), "January")
        self.assertEqual(search_tab_ui.input_search_edit.text(), "")

        self.assertEqual(search_tab_ui.search_button.text(), "Search")
        self.assertEqual(search_tab_ui.save_folder_button.text(), "Go To Save Folder")


if __name__ == "__main__":
    unittest.main()
