from datetime import datetime
import os
from tracemalloc import start
from typing import Sequence
from Constants import MONTHS, TSV_FILTER
from Settings import SettingsModel
import GeneralUtils
from ui import SearchTab
from PyQt5.QtCore import QObject, QDate
import ManageDB


class SearchController(QObject):
    def __init__(self, fetch_reports_ui: SearchTab.Ui_Search, settings: SettingsModel):
        super().__init__()
        self.file_name = ""
        self.fetch_reports_ui = fetch_reports_ui
        self.settings = settings
        self.search_type = fetch_reports_ui.search_type
        self.search_edit = fetch_reports_ui.input_search_edit
        self.start_month_comboBox = fetch_reports_ui.start_month_comboBox
        self.start_year_edit = fetch_reports_ui.start_year_edit
        self.start_year_edit.setDate(QDate(datetime.today().year - 1, 1, 1))
        self.end_month_comboBox = fetch_reports_ui.end_month_comboBox
        self.end_year_edit = fetch_reports_ui.end_year_edit
        self.end_year_edit.setDate(QDate(datetime.today().year, 1, 1))

        self.search_btn = fetch_reports_ui.search_button
        self.save_btn = fetch_reports_ui.save_folder_button
        self.result_edit = fetch_reports_ui.result_summary_edit

        self.search_btn.clicked.connect(self.search)
        self.save_btn.clicked.connect(self.open_save_folder)

    def search(self):
        search_type = self.search_type.currentText()
        search_edit = self.search_edit.text()
        start_month = self.start_month_comboBox.currentText()
        start_year = self.start_year_edit.text()
        end_month = self.end_month_comboBox.currentText()
        end_year = self.end_year_edit.text()

        if search_edit == "":
            GeneralUtils.show_message("Error, Please enter a search term")
            return

        start_month = self.get_month_number(start_month)
        start_year = int(start_year)
        end_month = self.get_month_number(end_month)
        end_year = int(end_year)

        if end_year < start_year or (
            end_year == start_year and end_month < start_month
        ):
            GeneralUtils.show_message("Error, Invalid date interval")
            return

        file_name = GeneralUtils.choose_save(TSV_FILTER)

        if file_name != "":
            if not file_name.lower().endswith(".tsv"):
                file_name += ".tsv"
            self.file_name = file_name

            results = self.get_query_result(
                search_type, start_year, end_year, start_month, end_month
            )

            self.result_edit.setText(
                f"Results: {len(results) - 1} rows\nFile: {file_name}"
            )

            GeneralUtils.save_data_as_tsv(file_name, results)
            GeneralUtils.open_file_or_dir(file_name)
        else:
            print("Error, no file location selected")

    def get_query_result(
        self,
        search_type: str,
        start_year: int,
        end_year: int,
        start_month: int,
        end_month: int,
    ):
        connection = ManageDB.create_connection(self.settings.database_location)
        if connection is not None:
            c = connection.cursor()

            if search_type == "Title Substring":
                c.execute(
                    "SELECT * FROM TR WHERE title LIKE ? AND (CASE WHEN year = ? AND year = ? THEN (CASE WHEN month >= ? AND month <= ? THEN 1 ELSE 0 END) WHEN year > ? AND year < ? THEN 1 WHEN year = ? AND month >= ? THEN 1 WHEN year = ? AND month <= ? THEN 1 ELSE 0 END)",
                    (
                        "%" + self.search_edit.text() + "%",
                        start_year,
                        end_year,
                        start_month,
                        end_month,
                        start_year,
                        end_year,
                        start_year,
                        start_month,
                        end_year,
                        end_month,
                    ),
                )
                results = c.fetchall()
            elif search_type == "ISSN":
                c.execute(
                    "SELECT * FROM TR WHERE online_issn = ? AND (CASE WHEN year = ? AND year = ? THEN (CASE WHEN month >= ? AND month <= ? THEN 1 ELSE 0 END) WHEN year > ? AND year < ? THEN 1 WHEN year = ? AND month >= ? THEN 1 WHEN year = ? AND month <= ? THEN 1 ELSE 0 END)",
                    (
                        self.search_edit.text(),
                        start_year,
                        end_year,
                        start_month,
                        end_month,
                        start_year,
                        end_year,
                        start_year,
                        start_month,
                        end_year,
                        end_month,
                    ),
                )
                results = c.fetchall()
            elif search_type == "ISBN":
                c.execute(
                    "SELECT * FROM TR WHERE isbn = ? AND (CASE WHEN year = ? AND year = ? THEN (CASE WHEN month >= ? AND month <= ? THEN 1 ELSE 0 END) WHEN year > ? AND year < ? THEN 1 WHEN year = ? AND month >= ? THEN 1 WHEN year = ? AND month <= ? THEN 1 ELSE 0 END)",
                    (
                        self.search_edit.text(),
                        start_year,
                        end_year,
                        start_month,
                        end_month,
                        start_year,
                        end_year,
                        start_year,
                        start_month,
                        end_year,
                        end_month,
                    ),
                )
                results = c.fetchall()

            c.execute("PRAGMA table_info(TR)")
            columns = c.fetchall()
            column_names = [column[1] for column in columns]

            headers = []
            for column_name in column_names:
                headers.append(column_name)
            results.insert(0, headers)

            c.close()
            connection.commit()
            connection.close()

            return results
        else:
            print("Error, no connection")
            return None

    def open_save_folder(self):
        if self.file_name == "":
            GeneralUtils.show_message("Error, Please Search first")
            return
        GeneralUtils.open_file_or_dir(os.path.dirname(self.file_name))

    def get_month_number(self, month_name: str):
        month_name = month_name.lower().strip()
        for number, name in MONTHS.items():
            if name == month_name.lower():
                return number
        return 0

    def update_settings(self, settings: SettingsModel):
        """Called when the settings are saved

        :param settings: the new settings"""
        self.settings = settings
