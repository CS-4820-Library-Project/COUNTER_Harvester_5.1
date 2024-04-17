import unittest
import sys

sys.path.insert(0, "/Users/karan/Downloads/UPEI/UPEI STUDY/Winter 2024/Counter-Harvesting-Tool-5.1")
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from ui import FetchReportsTab

app = QApplication(sys.argv)
fetch_reports_tab = QMainWindow()
fetch_reports_tab_ui = FetchReportsTab.Ui_FetchReports()
fetch_reports_tab_ui.setupUi(fetch_reports_tab)


class FetchReportsTests(unittest.TestCase):
    def test_defaults(self):
        """Test the defaults"""
        doc = QTextDocument()
        doc.setHtml(fetch_reports_tab_ui.label.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Fetch Report")

        doc.setHtml(fetch_reports_tab_ui.lblYear.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Year")

        self.assertEqual(len(fetch_reports_tab_ui.All_reports_edit_fetch.text()), 4)

        self.assertEqual(
            fetch_reports_tab_ui.fetch_all_data_button.text(), "Fetch All Reports"
        )

        doc.setHtml(fetch_reports_tab_ui.lblAdvanceFetchReport.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Advanced Fetch Reports")

        doc.setHtml(fetch_reports_tab_ui.lblFetchAllReport_3.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Select Vendors")

        self.assertEqual(fetch_reports_tab_ui.version_50_button.text(), "Version 5.0")
        self.assertEqual(fetch_reports_tab_ui.version_51_button.text(), "Version 5.1")

        self.assertEqual(
            fetch_reports_tab_ui.select_allvendors_button.text(), "Select All"
        )
        self.assertEqual(
            fetch_reports_tab_ui.deselect_allvendors_button.text(), "Deselect All"
        )

        doc.setHtml(fetch_reports_tab_ui.lblFetchAllReport_5.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Select Report Types")

        self.assertEqual(
            fetch_reports_tab_ui.select_all_master_reports_button.text(), "Select all"
        )

        self.assertEqual(
            fetch_reports_tab_ui.deselect_all_master_reports_button.text(),
            "Deselect all",
        )

        self.assertEqual(
            fetch_reports_tab_ui.pr_master_report_checkbox.checkState(), False
        )
        self.assertEqual(
            fetch_reports_tab_ui.tr_master_report_checkbox.checkState(), False
        )
        self.assertEqual(
            fetch_reports_tab_ui.ir_master_report_checkbox.checkState(), False
        )
        self.assertEqual(
            fetch_reports_tab_ui.dr_master_report_checkbox.checkState(), False
        )

        self.assertEqual(
            fetch_reports_tab_ui.select_more_options_button.text(),
            "Select more options",
        )

        doc.setHtml(fetch_reports_tab_ui.label_2.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Report(s) will be saved to:")

        self.assertEqual(fetch_reports_tab_ui.custom_dir_edit.text(), "")
        self.assertEqual(fetch_reports_tab_ui.custom_dir_button.text(), "Browse")

        self.assertEqual(
            fetch_reports_tab_ui.fetch_selected_reports_button.text(),
            "Fetch Selected Reports",
        )

        doc.setHtml(fetch_reports_tab_ui.lblFetchAllReport_4.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Date Range")

        doc.setHtml(fetch_reports_tab_ui.lblBeginDate.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Begin Year")

        doc.setHtml(fetch_reports_tab_ui.lblEndDate.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "End Year")

        doc.setHtml(fetch_reports_tab_ui.label_3.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Begin Month")

        doc.setHtml(fetch_reports_tab_ui.label_4.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "End Month")

        self.assertEqual(len(fetch_reports_tab_ui.begin_date_edit_fetch_year.text()), 4)

        self.assertEqual(len(fetch_reports_tab_ui.end_date_edit_fetch_year.text()), 4)

        doc.setHtml(fetch_reports_tab_ui.lblOptions.text())
        plain_text = doc.toPlainText()
        self.assertEqual(plain_text, "Select Standard View")


if __name__ == "__main__":
    unittest.main()
