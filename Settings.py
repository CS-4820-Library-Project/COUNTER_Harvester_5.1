"""This module handles all operations involving the user's settings."""

import json
from os import path
import os
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject, pyqtSignal
from ui import Settingtab
import ManageDB
from Constants import *
import GeneralUtils
from GeneralUtils import JsonModel


class Setting(Enum):
    """An enum of all settings"""

    DATABASE_LOCATION = 0
    VENDORS_LOCATION = 1
    YEARLY_DIR = 2
    OTHER_DIR = 3
    REQUEST_INTERVAL = 4
    REQUEST_TIMEOUT = 5
    USER_AGENT = 8


class SettingsModel(JsonModel):
    """This holds the user's settings.

    :param database_location: The location where the database is saved.
    :param vendors_location: The location where vendor data is saved.
    :param yearly_directory: The directory where yearly reports are saved. Yearly reports are reports that include all
        the available data for a year.
    :param other_directory: The default directory where non-yearly reports are saved.
    :param request_interval: The time to wait between each report request, per vendor.
    :param request_timeout: The time to wait before timing out a connection (seconds).
    :param user_agent: The user-agent that's included in the header when making requests.
    """

    def __init__(
        self,
        database_location: str,
        vendors_location: str,
        yearly_directory: str,
        other_directory: str,
        request_interval: int,
        request_timeout: int,
        user_agent: str,
    ):
        self.yearly_directory = path.abspath(yearly_directory) + path.sep
        self.other_directory = path.abspath(other_directory) + path.sep
        self.database_location = path.abspath(database_location)
        self.vendors_location = path.abspath(vendors_location)
        self.request_interval = request_interval
        self.request_timeout = request_timeout
        self.user_agent = user_agent

    @classmethod
    def from_json(cls, json_dict: dict):
        database_location = (
            json_dict["database_location"]
            if "database_location" in json_dict
            else DATABASE_LOCATION
        )
        if not path.exists(database_location):
            database_location = DATABASE_LOCATION

        vendors_location = (
            json_dict["vendors_location"]
            if "vendors_location" in json_dict
            else VENDORS_FILE_PATH
        )
        if not path.exists(vendors_location):
            vendors_location = VENDORS_FILE_PATH

        yearly_directory = (
            json_dict["yearly_directory"]
            if "yearly_directory" in json_dict
            else YEARLY_DIR
        )
        if not path.exists(yearly_directory):
            yearly_directory = YEARLY_DIR

        other_directory = (
            json_dict["other_directory"]
            if "other_directory" in json_dict
            else OTHER_DIR
        )
        if not path.exists(other_directory):
            other_directory = OTHER_DIR

        request_interval = (
            int(json_dict["request_interval"])
            if "request_interval" in json_dict
            else REQUEST_INTERVAL
        )
        request_timeout = (
            int(json_dict["request_timeout"])
            if "request_timeout" in json_dict
            else REQUEST_TIMEOUT
        )
        user_agent = (
            json_dict["user_agent"] if "user_agent" in json_dict else USER_AGENT
        )

        return cls(
            database_location,
            vendors_location,
            yearly_directory,
            other_directory,
            request_interval,
            request_timeout,
            user_agent,
        )


class SettingsController(QObject):
    """Controls the Settings tab

    :param settings_widget: The settings widget.
    :param settings_ui: The UI for settings_widget.
    """

    settings_changed_signal = pyqtSignal(SettingsModel)

    def __init__(self, settings_widget: QWidget, settings_ui: Settingtab.Ui_SettingTab):
        # region General
        super().__init__()
        self.settings_widget = settings_widget

        json_string = GeneralUtils.read_json_file(
            SETTINGS_FILE_DIR + SETTINGS_FILE_NAME
        )
        json_dict = json.loads(json_string)
        self.settings = SettingsModel.from_json(json_dict)
        self.save_settings_to_disk()

        # endregion

        # region Reports
        self.dir_edit = settings_ui.directory_edit
        self.dir_type_comboBox = settings_ui.directory_type_comboBox
        self.request_interval_spin_box = settings_ui.request_interval_spin_box
        self.request_timeout_spin_box = settings_ui.request_timeout_spin_box
        self.user_agent_edit = settings_ui.user_agent_edit

        self.dir_edit.setText(self.settings.database_location)
        self.dir_edit.textChanged.connect(self.on_dir_edit_changed)
        self.dir_type_comboBox.currentIndexChanged.connect(self.update_dir_edit)
        self.request_interval_spin_box.setValue(self.settings.request_interval)
        self.request_timeout_spin_box.setValue(self.settings.request_timeout)
        self.user_agent_edit.setText(self.settings.user_agent)

        settings_ui.select_directory_button.clicked.connect(
            self.on_directory_setting_clicked
        )

        settings_ui.save_button.clicked.connect(self.on_save_button_clicked)
        # endregion

        # region Search
        # set up restore database button
        self.is_rebuilding_database = False
        self.update_database_dialog = ManageDB.UpdateDatabaseProgressDialogController(
            self.settings_widget
        )
        self.rebuild_database_button = settings_ui.settings_rebuild_database_button
        self.rebuild_database_button.clicked.connect(self.on_rebuild_database_clicked)
        # endregion

    def update_dir_edit(self, index):
        if self.dir_type_comboBox.currentText() == "Yearly reports":
            self.dir_edit.setText(self.settings.yearly_directory)
        elif self.dir_type_comboBox.currentText() == "Other reports":
            self.dir_edit.setText(self.settings.other_directory)
        elif self.dir_type_comboBox.currentText() == "Search database":
            self.dir_edit.setText(self.settings.database_location)
        elif self.dir_type_comboBox.currentText() == "Vendor data file":
            self.dir_edit.setText(self.settings.vendors_location)
        else:
            self.dir_edit.setText("")

    def on_dir_edit_changed(self, new_text):
        if self.dir_type_comboBox.currentText() == "Yearly reports":
            self.settings.yearly_directory = new_text
        elif self.dir_type_comboBox.currentText() == "Other reports":
            self.settings.other_directory = new_text
        elif self.dir_type_comboBox.currentText() == "Search database":
            self.settings.database_location = new_text
        elif self.dir_type_comboBox.currentText() == "Vendor data file":
            self.settings.vendors_location = new_text

    def on_directory_setting_clicked(self):
        """Handles the signal emitted when a choose folder button is clicked

        :param setting: The setting to be changed
        """
        if self.dir_type_comboBox.currentText() == "Yearly reports":
            setting = Setting.YEARLY_DIR
            dir_path = GeneralUtils.choose_directory()
        elif self.dir_type_comboBox.currentText() == "Other reports":
            setting = Setting.OTHER_DIR
            dir_path = GeneralUtils.choose_directory()
        elif self.dir_type_comboBox.currentText() == "Search database":
            setting = Setting.DATABASE_LOCATION
            dir_path = GeneralUtils.choose_database_file()
        elif self.dir_type_comboBox.currentText() == "Vendor data file":
            setting = Setting.VENDORS_LOCATION
            dir_path = GeneralUtils.choose_dat_file()

        if dir_path:
            if setting == Setting.YEARLY_DIR:
                self.settings.yearly_directory = dir_path
            elif setting == Setting.OTHER_DIR:
                self.settings.other_directory = dir_path
            elif setting == Setting.DATABASE_LOCATION:
                self.settings.database_location = dir_path
            elif setting == Setting.VENDORS_LOCATION:
                self.settings.vendors_location = dir_path

            self.dir_edit.setText(dir_path)

    def on_save_button_clicked(self):
        """Handles the signal emitted when the save button is clicked"""
        self.update_settings()
        self.save_settings_to_disk()
        self.settings_changed_signal.emit(self.settings)
        GeneralUtils.show_message("Changes saved!")

    def on_rebuild_database_clicked(self):
        """Restores the database when the restore database button is clicked"""
        if not self.is_rebuilding_database:  # check if already running
            if GeneralUtils.ask_confirmation(
                "Are you sure you want to rebuild the database?"
            ):
                self.is_rebuilding_database = True
                self.update_database_dialog.update_database(
                    ManageDB.get_all_report_files(),
                    True,
                )
                self.is_rebuilding_database = False
        else:
            print("It is equal to the rebuild database state")
            pass

    def update_settings(self):
        """Updates the app's settings using the values entered on the UI"""

        self.settings.request_interval = self.request_interval_spin_box.value()
        self.settings.request_timeout = self.request_timeout_spin_box.value()
        self.settings.user_agent = self.user_agent_edit.text()

    def save_settings_to_disk(self):
        """Saves all settings to disk"""
        json_string = json.dumps(self.settings, default=lambda o: o.__dict__)
        GeneralUtils.save_json_file(SETTINGS_FILE_DIR, SETTINGS_FILE_NAME, json_string)
