import unittest
import sys

sys.path.insert(0, "/Users/karan/Downloads/UPEI/UPEI STUDY/Winter 2024/Counter-Harvesting-Tool-5.1")
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from ui import Settingtab

app = QApplication(sys.argv)
settings_tab = QMainWindow()
settings_tab_ui = Settingtab.Ui_SettingTab()
settings_tab_ui.setupUi(settings_tab)


class SettingsTabTests(unittest.TestCase):
    def test_defaults(self):
        """Test the defaults"""
        doc = QTextDocument()
        doc.setHtml(settings_tab_ui.label.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Settings")

        doc.setHtml(settings_tab_ui.label_9.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "If Database gets Corrupted")

        doc.setHtml(settings_tab_ui.label_7.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Data folders directories")

        doc.setHtml(settings_tab_ui.label_2.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Report request interval")

        doc.setHtml(settings_tab_ui.label_3.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Request timeout")


        doc.setHtml(settings_tab_ui.label_6.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "User agent")

        self.assertEqual(
            settings_tab_ui.directory_type_comboBox.currentText(), "Search database"
        )

        self.assertEqual(settings_tab_ui.directory_edit.text(), "")
        self.assertEqual(settings_tab_ui.request_interval_spin_box.value(), 0)
        self.assertEqual(settings_tab_ui.request_timeout_spin_box.value(), 0)
        self.assertEqual(settings_tab_ui.user_agent_edit.text(), "")
        self.assertEqual(settings_tab_ui.select_directory_button.text(), "Choose")
        self.assertEqual(settings_tab_ui.save_button.text(), "Save All Changes")
        self.assertEqual(
            settings_tab_ui.settings_rebuild_database_button.text(), "Rebuild Database"
        )


if __name__ == "__main__":
    unittest.main()
