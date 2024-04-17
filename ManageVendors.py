"""This module handles all operations involving managing vendors."""

import csv
import os
import json
from sys import version
import requests
import validators
import logging
from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QDialogButtonBox,
    QWidget,
    QCheckBox,
    QMainWindow,
    QDateEdit,
)

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QObject, QModelIndex, pyqtSignal
from Settings import SettingsModel
from ui import (
    ManageVendorsTab,
    AddVendor51,
    RemoveVendorDialog,
    ImportVersion,
    EditVendors51,
)

# import ManageDB
import GeneralUtils
from GeneralUtils import JsonModel
from Constants import *
import datetime
from PyQt5.QtCore import QDate
import datetime
from PyQt5.QtCore import QDate

# from Settings import SettingsModel


class Vendor51(JsonModel):
    """This holds a vendor's information

    :param name: The vendor's unique name (Mandatory, unique enforced)
    :param version: Indicates if this is for version 5.0 or 5.1 (Mandatory)
    :param base_url: The base URL for making sushi report calls (must end with '/counter/r51/reports', mandatory for 5.0)
    :param starting_year: Starting year for this version (5.0 or 5.1) (Mandatory)
    :param customer_id: The customer id used in sushi report calls (Mandatory)
    :param requestor_id: The requestor id used in sushi report calls
    :param api_key: The api key used in sushi report calls
    :param platform: The platform id used in sushi report calls
    :param requires_two_attempts: Whether it requires two attempts per report (Y/N, mandatory)
    :param does_ip_checking: Whether it does IP checking (Y/N, mandatory)
    :param needs_throttling: Whether it needs requests throttled (Y/N, mandatory)
    :param notes: Additional notes
    :param provider: Provider information
    """

    def __init__(
        self,
        name: str,
        version: str,
        base_url: str,
        starting_year: str,
        customer_id: str,
        requestor_id: str,
        api_key: str,
        platform: str,
        requires_two_attempts: bool,
        does_ip_checking: bool,
        needs_throttling: bool,
        notes: str,
        provider: str,
    ):
        self.name = name
        self.version = version  # "5.1" or "5.0"
        self.base_url = base_url  # https://...../r51/reports
        self.starting_year = starting_year
        self.customer_id = customer_id
        self.requestor_id = requestor_id
        self.api_key = api_key
        self.platform = platform
        self.requires_two_attempts = requires_two_attempts  # True or False
        self.does_ip_checking = does_ip_checking  # True or False
        self.needs_throttling = needs_throttling  # True or False
        self.notes = notes
        self.provider = provider


class ManageVendorsController(QObject):
    """Controls the Manage Vendors tab

    :param manage_vendors_widget: The manage vendors widget.
    :param manage_vendors_ui: The UI for the manage_vendors_widget.
    """

    def __init__(
        self,
        manage_vendors_widget: QWidget,
        manage_vendors_ui: ManageVendorsTab.Ui_manage_vendor_tab,
        settings: SettingsModel,
    ):
        super().__init__()
        self.manage_vendors_widget = manage_vendors_widget
        self.curr_version = "5.1"

        self.add_vendor_button = manage_vendors_ui.addVendorButton
        self.edit_vendor_button = manage_vendors_ui.editvendorsbutton

        # button to see vendor list of version 5.0
        self.version50_button = manage_vendors_ui.version50
        self.version50_button.clicked.connect(self.on_click_version50)

        # button to see vendor list of version 5.1
        self.version51_button = manage_vendors_ui.version51
        self.version51_button.clicked.connect(self.on_click_version51)

        self.export_vendors_button = manage_vendors_ui.exportVendorsButton
        self.import_vendors_button = manage_vendors_ui.importVendorsButton

        self.add_vendor_button.clicked.connect(self.on_add_vendor_clicked)
        self.import_vendors_button.clicked.connect(self.on_import_vendors_clicked)
        self.export_vendors_button.clicked.connect(self.on_export_vendors_clicked)

        self.edit_vendor_button.clicked.connect(self.edit_vendor_window)
        self.vendor_list_view = manage_vendors_ui.vendorsListView
        self.vendor_list_view.clicked.connect(self.on_vendor_selected)

        self.settings = settings
        self.vendors_v50: list[Vendor51] = []
        self.vendors_v51: list[Vendor51] = []
        self.vendor_names_v50 = set()
        self.vendor_names_v51 = set()

        self.get_vendor_names()
        self.sort_vendors()
        self.on_click_version51()

        self.isValidated: bool = False

    # """
    # Show List According to selected version Section
    # """

    def update_vendor_names(self):
        """Updates the local set of vendor names used for validation"""
        self.vendor_names_v50.clear()
        for vendor in self.vendors_v50:
            self.vendor_names_v50.add(vendor.name.lower())

        self.vendor_names_v51.clear()
        for vendor in self.vendors_v51:
            self.vendor_names_v51.add(vendor.name.lower())

    def sort_vendors(self):
        """Sorts the vendors alphabetically based their names"""
        self.vendors_v50 = sorted(
            self.vendors_v50, key=lambda vendor: vendor.name.lower()
        )
        self.vendors_v51 = sorted(
            self.vendors_v51, key=lambda vendor: vendor.name.lower()
        )

    def get_vendor_names(self):
        """
        Retrieves vendor names and populates the model with vendor objects.

        This method reads JSON data from a file, creates Vendor objects, and appends them to an array.
        It also adds the lowercase version of each vendor name to a set for easy lookup.
        """
        try:
            # script_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = self.settings.vendors_location
            if not os.path.exists(file_path):
                return
            # Read JSON data from vendors.dat
            with open(file_path, "r") as file:
                vendors_data = json.load(file)

            # Populate the model with vendor names
            for vendor_data in vendors_data:
                vendor_name = vendor_data.get("name", "")
                version = vendor_data.get("version", "")
                base_url = vendor_data.get("base_url", "")
                starting_year = vendor_data.get("starting_year", "")
                customer_id = vendor_data.get("customer_id", "")
                requestor_id = vendor_data.get("requestor_id", "")
                api_key = vendor_data.get("api_key", "")
                platform = vendor_data.get("platform", "")
                requires_two_attempts = vendor_data.get("requires_two_attempts", False)
                does_ip_checking = vendor_data.get("does_ip_checking", False)
                needs_throttling = vendor_data.get("needs_throttling", False)
                notes = vendor_data.get("notes", "")
                provider = vendor_data.get("provider", "")

                # Create a Vendor object and append it to the array
                vendor_object = Vendor51(
                    name=vendor_name,
                    version=version,
                    base_url=base_url,
                    starting_year=starting_year,
                    customer_id=customer_id,
                    requestor_id=requestor_id,
                    api_key=api_key,
                    platform=platform,
                    requires_two_attempts=requires_two_attempts,
                    does_ip_checking=does_ip_checking,
                    needs_throttling=needs_throttling,
                    notes=notes,
                    provider=provider,
                )

                if vendor_name:
                    if version == "5.0":
                        self.vendors_v50.append(vendor_object)
                        vendor_name: str = vendor_name.lower()
                        self.vendor_names_v50.add(vendor_name)
                    else:
                        self.vendors_v51.append(vendor_object)
                        vendor_name: str = vendor_name.lower()
                        self.vendor_names_v51.add(vendor_name)

            self.update_vendors_dat_file()
            self.update_vendors51_dat_file()

        except Exception as e:
            print(f"Error loading vendors: {e}")

    def on_click_version50(self):
        """
        Handle the click event for the version 5.0 button.
        Loads vendors data for version 5.0 and updates the vendor list view accordingly.
        """
        try:
            # Create a QStringListModel
            model = QStandardItemModel()

            for vendor_data in self.vendors_v50:
                vendor_name = vendor_data.name
                item = QStandardItem(vendor_name)
                item.setEditable(False)
                model.appendRow(item)

            self.version50_button.setStyleSheet(
                """
                    QPushButton { 
                        color: #FFFFFF;
                        font: bold;
                        border-radius: 4px;
                        text-align: center;
                        background-color: #1768E3;
                    }
                """
            )
            self.version51_button.setStyleSheet(
                """
                    QPushButton { 
                        color: #FFFFFF;
                        font: bold;
                        border-radius: 4px;
                        text-align: center;
                    }
                """
            )
            # Set the model for the QListView
            self.vendor_list_view.setModel(model)
            self.curr_version = "5.0"
            self.selected_index = -1

        except Exception as e:
            print(f"Error loading vendors: {e}")

    def on_click_version51(self):
        """
        Handle the click event for the version 5.1 button.
        Loads vendors_v51 data into the vendor_list_view.

        Raises:
            Exception: If there is an error loading vendors.
        """
        try:
            # Create a QStringListModel
            model = QStandardItemModel()

            for vendor_data in self.vendors_v51:
                vendor_name = vendor_data.name
                item = QStandardItem(vendor_name)
                item.setEditable(False)
                model.appendRow(item)

            self.version51_button.setStyleSheet(
                """
                    QPushButton { 
                        color: #FFFFFF;
                        font: bold;
                        border-radius: 4px;
                        text-align: center;
                        background-color: #1768E3;
                    }
                """
            )
            self.version50_button.setStyleSheet(
                """
                    QPushButton { 
                        color: #FFFFFF;
                        font: bold;
                        border-radius: 4px;
                        text-align: center;
                    }
                """
            )

            # Set the model for the QListView
            self.vendor_list_view.setModel(model)
            self.curr_version = "5.1"
            self.selected_index = -1

        except Exception as e:
            print(f"Error loading vendors: {e}")

    # """
    # Adding A New Vendor Section
    # """

    def add_vendor(self, new_vendor: Vendor51, version: str) -> tuple[bool, str]:
        """Adds a new vendor to the system if the vendor is valid

        :param new_vendor: The new vendor to be added
        :returns: (is_successful, message) A Tuple with the completion status and a message
        """

        # Check if vendor name is valid
        is_valid, message = self.validate_new_name(new_vendor.name, "", version)
        if not is_valid:
            return is_valid, message

        is_valid, message = self.validate_url(new_vendor.base_url, version)
        if not is_valid:
            return is_valid, message
        if new_vendor.customer_id == "":
            return False, "Customer Id cannot be empty."

        if version == "5.1":
            self.vendors_v51.append(new_vendor)
            self.vendor_names_v51.add(new_vendor.name.lower())
            self.sort_vendors()
            self.on_click_version51()
            self.update_vendors51_dat_file()
        else:
            self.vendors_v50.append(new_vendor)
            self.vendor_names_v50.add(new_vendor.name.lower())
            self.sort_vendors()
            self.on_click_version50()
            self.update_vendors_dat_file()

        return True, ""

    def on_add_vendor_clicked(self):
        """Handles the signal emitted when the add vendor button is clicked

        A dialog is show to allow the user to enter a new vendor's information. If the information entered is valid,
        the vendor is added to the system
        """
        vendor_dialog = QMainWindow()
        vendor_dialog_ui = AddVendor51.Ui_addVendor51Dialog()
        vendor_dialog_ui.setupUi(vendor_dialog)
        vendor_dialog.show()

        name_edit = vendor_dialog_ui.nameEdit
        version_edit = vendor_dialog_ui.versionEdit
        version_edit.setText("5.1" if self.curr_version == "5.1" else "5.0")
        base_url_edit = vendor_dialog_ui.baseUrlEdit

        start_year = vendor_dialog_ui.All_reports_edit_fetch
        # Get the current date and time
        current_date = datetime.datetime.now()
        # Calculate the date for the same day of the last year
        last_year_date = QDate(
            current_date.year - 1, current_date.month, current_date.day
        )
        # set previous year date to the start_year
        start_year.setDate(last_year_date)

        customer_id_edit = vendor_dialog_ui.customerIdEdit
        requestor_id_edit = vendor_dialog_ui.requestorIdEdit
        api_key_edit = vendor_dialog_ui.apiKeyEdit
        platform_edit = vendor_dialog_ui.platformEdit
        two_attempts_check_box = vendor_dialog_ui.two_attempts_check_box
        ip_checking_check_box = vendor_dialog_ui.ip_checking_check_box
        requests_throttled_check_box = vendor_dialog_ui.requests_throttled_check_box
        provider_edit = vendor_dialog_ui.providerEdit
        notes_edit = vendor_dialog_ui.notesEdit

        validate_button = vendor_dialog_ui.validate_button
        self.isValidated = False

        name_validation_label = vendor_dialog_ui.name_validation_label
        name_validation_label.hide()
        url_validation_label = vendor_dialog_ui.url_validation_label
        url_validation_label.hide()

        name_edit.textChanged.connect(
            lambda new_name: self.on_name_text_changed(
                new_name, "", name_validation_label, version_edit.text()
            )
        )

        base_url_edit.textChanged.connect(
            lambda url: self.on_url_text_changed(url, url_validation_label, True)
        )

        def attempt_add_vendor():
            if not self.isValidated:
                GeneralUtils.show_message("Please validate the vendor first.")
                return

            vendor = Vendor51(
                name_edit.text(),
                version_edit.text(),
                base_url_edit.text(),
                start_year.text(),
                customer_id_edit.text(),
                requestor_id_edit.text(),
                api_key_edit.text(),
                platform_edit.text(),
                two_attempts_check_box.isChecked(),
                ip_checking_check_box.isChecked(),
                requests_throttled_check_box.isChecked(),
                notes_edit.text(),
                provider_edit.text(),
            )

            is_valid, message = self.add_vendor(vendor, version_edit.text())
            if is_valid:
                self.sort_vendors()
                self.update_vendor_names()
                if version_edit.text() == "5.1":
                    self.on_click_version51()
                    self.update_vendors51_dat_file()
                    self.selected_index = -1
                else:
                    self.on_click_version50()
                    self.update_vendors_dat_file()
                    self.selected_index = -1

                vendor_dialog.close()
            else:
                GeneralUtils.show_message(message)

        def validate_vendor():
            try:
                request_url = base_url_edit.text()
                # triming the url and removing /reports from the end and adding /status
                request_url = request_url.strip()
                if request_url.endswith("/reports"):
                    request_url = request_url[:-8]
                request_url += "/status"

                response = requests.get(request_url, timeout=10)
                url = response.history[0].url if response.history else response.url
                if response.status_code == 200:
                    logging.info(f"Vendor : {name_edit.text()}, URL for Validation : {url} \n Success\n\n")
                    GeneralUtils.show_message("Vendor validated successfully")
                    self.isValidated = True
                else:
                    response_text = response.text
                    if len(response_text) > 500:
                        response_text = response_text[:500] + "..."
                    logging.info(f"Vendor : {name_edit.text()}, URL for Validation : {url} \n {response_text}\n\n")
                    GeneralUtils.show_message(
                        f"Vendor validation failed with status code: {response.status_code} \n Check Logs for more info"
                    )
            except requests.exceptions.Timeout as e:
                logging.info(
                    f"Vendor : {name_edit.text()}, Vendor validation failed: Timeout , URL : {request_url} \n\n"
                )
                GeneralUtils.show_message("Vendor validation failed: Timeout")
                return
            except requests.exceptions.RequestException as e:
                logging.info(
                    f"Vendor : {name_edit.text()}, Vendor validation failed: {e} , \nURL : {request_url} \n\n"
                )
                GeneralUtils.show_message(f"Vendor validation failed: {e}")
                return

        validate_button.clicked.connect(lambda: validate_vendor())
        button_box = vendor_dialog_ui.buttonBox
        ok_button = button_box.button(QDialogButtonBox.Ok)
        ok_button.clicked.connect(attempt_add_vendor)
        cancel_button = button_box.button(QDialogButtonBox.Cancel)
        cancel_button.clicked.connect(lambda: vendor_dialog.close())

        vendor_dialog.exec_()

    # """
    # Data Validation Section
    # """

    def on_name_text_changed(
        self,
        new_name: str,
        original_name: str,
        validation_label: QLabel,
        version: str,
        validate: bool = True,
    ):
        """Handles the signal emitted when a vendor's name is changed

        :param new_name: The new name entered in the text field
        :param original_name: The vendor's original name
        :param validation_label: The label to show validation messages
        :param version: The version of the Vendor List to put the vendor
        :param validate: This indicates whether the new_name should be validated
        """
        if not validate:
            validation_label.hide()
            return

        is_valid, message = self.validate_new_name(new_name, original_name, version)

        if is_valid:
            validation_label.hide()
        else:
            validation_label.show()
            validation_label.setText(message)

    def validate_new_name(
        self, new_name: str, original_name: str, version: str
    ) -> tuple[bool, str]:
        """Validates a new vendor name

        :param new_name: The new name to be validated
        :param original_name: The original name
        :param version: The version of the Vendor List to put the vendor
        :returns: (is_successful, message) A Tuple with the completion status and a message
        """
        if not new_name:
            return False, "Vendor name can't be empty"

        if version == "5.1":
            if (
                new_name.lower() in self.vendor_names_v51
                and new_name.lower() != original_name.lower()
            ):
                return False, "Duplicate vendor name"
            else:
                return True, ""
        elif version == "5.0":
            if (
                new_name.lower() in self.vendor_names_v50
                and new_name.lower() != original_name.lower()
            ):
                return False, "Duplicate vendor name"
            else:
                return True, ""
        else:
            return True, ""

    def on_url_text_changed(
        self,
        url: str,
        validation_label: QLabel,
        validate: bool,
    ):
        """Handles the signal emitted when a vendor's URL is changed

        :param url: The URL entered in the text field
        :param validation_label: The label to show validation messages
        :param validate: This indicates whether the url should be validated
        hide or show the validation label
        """
        if not validate:
            validation_label.hide()
            return

        is_valid, message = self.validate_url(url, self.curr_version)
        if is_valid:
            validation_label.hide()
        else:
            validation_label.show()
            validation_label.setText(message)

    def validate_url(self, url: str, version: str) -> tuple[bool, str]:
        """Validates a new url

        :param url: The URL to be validated
        :returns: (is_successful, message) A Tuple with the completion status and a message
        """
        if not validators.url(url):
            return False, "Invalid Url"

        if version == "5.0" and not url.endswith("/reports"):
            return False, "URL must end with '/reports'"
        elif version == "5.1" and not url.endswith("/r51/reports"):
            return False, "URL must end with '/r51/reports'"

        return True, ""

    # """
    # Update dat files Section
    # """

    def write_data_to_file(self, file_path: str, vendors: list[Vendor51]):
        """
        Write the data of vendors to a file in JSON format.

        Args:
            file_path (str): The path of the file to write the data to.
            vendors (list[Vendor51]): The list of vendors to write to the file.

        Returns:
            None
        """
        data = [vendor.__dict__ for vendor in vendors]
        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)

    def update_vendors51_dat_file(self):
        """
        Updates the 'vendors51.dat' file with the data from 'self.vendors_v51'.
        """
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_directory, "vendors51.dat")
        self.write_data_to_file(file_path, self.vendors_v51)
        all_vendors: list[Vendor51] = []
        for vendor in self.vendors_v50:
            all_vendors.append(vendor)
        for vendor in self.vendors_v51:
            all_vendors.append(vendor)
        self.write_data_to_file(self.settings.vendors_location, all_vendors)

    def update_vendors_dat_file(self):
        """
        Updates the vendors.dat file with the data from self.vendors_v50.
        """
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_directory, "vendors.dat")
        self.write_data_to_file(file_path, self.vendors_v50)
        all_vendors: list[Vendor51] = []
        for vendor in self.vendors_v50:
            all_vendors.append(vendor)
        for vendor in self.vendors_v51:
            all_vendors.append(vendor)
        self.write_data_to_file(self.settings.vendors_location, all_vendors)

    # """
    # Import Export Section
    # """

    def import_vendors_tsv(self, file_path: str):
        """Imports the vendors of version 5.1 and version 5.0 from a TSV file path to the system

        :param file_path: The file path of the vendors TSV file
        """
        try:
            tsv_file = open(file_path, "r", encoding="utf-8", newline="")
            reader = csv.DictReader(tsv_file, delimiter="\t")
            for row in reader:
                if "requires_two_attempts" in row:
                    requires_two_attempts = (
                        row["requires_two_attempts"].lower() == "true"
                    )
                else:
                    requires_two_attempts = False

                if "does_ip_checking" in row:
                    does_ip_checking = row["does_ip_checking"].lower() == "true"
                else:
                    does_ip_checking = False

                if "needs_throttling" in row:
                    needs_throttling = row["needs_throttling"].lower() == "true"
                else:
                    needs_throttling = False

                vendor = Vendor51(
                    row["name"] if "name" in row else "",
                    row["version"] if "version" in row else "",
                    row["base_url"] if "base_url" in row else "",
                    row["starting_year"] if "starting_year" in row else "",
                    row["customer_id"] if "customer_id" in row else "",
                    row["requestor_id"] if "requestor_id" in row else "",
                    row["api_key"] if "api_key" in row else "",
                    row["platform"] if "platform" in row else "",
                    requires_two_attempts,
                    does_ip_checking,
                    needs_throttling,
                    row["notes"] if "notes" in row else "",
                    row["provider"] if "provider" in row else "",
                )

                is_valid, message = self.validate_new_name(
                    vendor.name, "", vendor.version
                )
                if not is_valid:
                    if message == "Duplicate vendor name":
                        org_vendor = None
                        if vendor.version == "5.0":
                            for v in self.vendors_v50:
                                if v.name.lower() == vendor.name.lower():
                                    org_vendor = v
                                    break
                        else:
                            for v in self.vendors_v51:
                                if v.name.lower() == vendor.name.lower():
                                    org_vendor = v
                                    break

                        if org_vendor:
                            is_valid, message = self.update_vendor_while_importing(
                                vendor, org_vendor, vendor.version
                            )
                            if not is_valid:
                                print(
                                    f"error in importing vendor : {vendor.name}, version {vendor.version}, message : {message}"
                                )
                    else:
                        print(
                            f"error in importing vendor : {vendor.name} , version {vendor.version}, message : {message}"
                        )
                else:
                    is_valid, message = self.add_vendor(vendor, vendor.version)
                    if not is_valid:
                        print(
                            f"error in importing vendor : {vendor.name} , version {vendor.version}, message : {message}"
                        )

            tsv_file.close()

            self.sort_vendors()
            self.selected_index = -1
            self.on_click_version50()
            self.update_vendors_dat_file()
            self.on_click_version51()
            self.update_vendors51_dat_file()
            self.update_vendor_names()

            GeneralUtils.show_message(f"Import successful!")
        except Exception as e:
            GeneralUtils.show_message(f"File import failed: {e}")

    def import_vendors_clicked(
        self, import_version_dialog, remove_previous: bool = False
    ):
        import_version_dialog.close()
        file_path = GeneralUtils.choose_file(TSV_FILTER)

        if file_path:
            if remove_previous:
                self.remove_all_previous_vendors()
            self.import_vendors_tsv(file_path)

    def remove_all_previous_vendors(self):
        self.vendors_v50.clear()
        self.vendors_v51.clear()
        self.vendor_names_v50.clear()
        self.vendor_names_v51.clear()
        file_path = self.settings.vendors_location
        if os.path.exists(file_path):
            os.remove(file_path)

    def on_import_vendors_clicked(self):
        """Handles the signal emitted when the import vendors button is clicked.
        A file select dialog is shown to allow the user to select the vendors TSV file to import. The selected file is then imported.
        """
        import_version_dialog = QMainWindow()
        import_version_dialog_ui = ImportVersion.Ui_importVersionDialog()

        import_version_dialog_ui.setupUi(import_version_dialog)
        import_version_dialog.show()

        import_btn = import_version_dialog_ui.import_button
        remove_previous_vendors_checkbox = import_version_dialog_ui.checkBox
        # TODO

        import_btn.clicked.connect(
            lambda: self.import_vendors_clicked(
                import_version_dialog, remove_previous_vendors_checkbox.isChecked()
            )
        )

        import_version_dialog.exec_()

    def on_export_vendors_clicked(self):
        """Handles the signal emitted when the export vendors button is clicked.

        A folder select dialog is shown to allow the user to select the target directory to export the vendors file to.
        A vendors TSV file containing all the vendors in the system is then exported
        """
        dir_path = GeneralUtils.choose_directory()
        if dir_path:
            self.export_vendors_tsv(dir_path)

    def export_vendors_tsv(self, dir_path):
        """Exports all vendor information as a TSV file to a directory

        :param dir_path: The directory path to export the vendors TSV file to
        """
        file_path = f"{dir_path}{EXPORT_ALL_VENDORS_FILE_NAME}"
        column_names = [
            "name",
            "version",
            "base_url",
            "starting_year",
            "customer_id",
            "requestor_id",
            "api_key",
            "platform",
            "requires_two_attempts",
            "does_ip_checking",
            "needs_throttling",
            "notes",
            "provider",
        ]
        try:
            tsv_file = open(file_path, "w", encoding="utf-8", newline="")
            tsv_dict_writer = csv.DictWriter(tsv_file, column_names, delimiter="\t")
            tsv_dict_writer.writeheader()

            all_vendors = self.vendors_v50 + self.vendors_v51

            for vendor in all_vendors:
                tsv_dict_writer.writerow(vendor.__dict__)

            tsv_file.close()
            GeneralUtils.show_message(f"Exported to {file_path}")

        except Exception as e:
            GeneralUtils.show_message(f"File export failed: {e}")

    # """
    # Edit section
    # """

    def on_vendor_selected(self, model_index: QModelIndex):
        """Handles the signal emitted when a vendor is selected

        :param model_index: An object containing the location of the vendor on the vendor list
        """
        self.selected_index = model_index.row()

    def edit_vendor_window(self):
        """Handles the signal emitted when the edit vendor button is clicked

        A dialog is show to allow the user to update vendor's information. If the information entered is valid,
        the vendor is updated to the system
        """
        if self.selected_index < 0:
            GeneralUtils.show_message("Please select a vendor to edit")
            return

        edit_vendor_dialog = QMainWindow()
        edit_vendor_dialog_ui = EditVendors51.Ui_editVendors51()
        edit_vendor_dialog_ui.setupUi(edit_vendor_dialog)
        edit_vendor_dialog.show()

        name_edit = edit_vendor_dialog_ui.nameEdit
        version_edit = edit_vendor_dialog_ui.versionEdit
        base_url_edit = edit_vendor_dialog_ui.baseUrlEdit
        start_year = edit_vendor_dialog_ui.All_reports_edit_fetch
        customer_id_edit = edit_vendor_dialog_ui.customerIdEdit
        requestor_id_edit = edit_vendor_dialog_ui.requestorIdEdit
        api_key_edit = edit_vendor_dialog_ui.apiKeyEdit
        platform_edit = edit_vendor_dialog_ui.platformEdit
        two_attempts_check_box = edit_vendor_dialog_ui.two_attempts_check_box
        ip_checking_check_box = edit_vendor_dialog_ui.ip_checking_check_box
        requests_throttled_check_box = (
            edit_vendor_dialog_ui.requests_throttled_check_box
        )
        provider_edit = edit_vendor_dialog_ui.providerEdit
        notes_edit = edit_vendor_dialog_ui.notesEdit

        name_validation_label = edit_vendor_dialog_ui.name_validation_label
        name_validation_label.hide()
        url_validation_label = edit_vendor_dialog_ui.url_validation_label
        url_validation_label.hide()

        if self.curr_version == "5.1":
            selected_vendor = self.vendors_v51[self.selected_index]
        else:
            selected_vendor = self.vendors_v50[self.selected_index]

        name_edit.setText(selected_vendor.name)
        version_edit.setText(selected_vendor.version)
        base_url_edit.setText(selected_vendor.base_url)
        current_date = datetime.datetime.now()
        starting_year = QDate(
            int(selected_vendor.starting_year), current_date.month, current_date.day
        )
        start_year.setDate(starting_year)
        customer_id_edit.setText(selected_vendor.customer_id)
        requestor_id_edit.setText(selected_vendor.requestor_id)
        api_key_edit.setText(selected_vendor.api_key)
        platform_edit.setText(selected_vendor.platform)
        two_attempts_check_box.setChecked(selected_vendor.requires_two_attempts)
        ip_checking_check_box.setChecked(selected_vendor.does_ip_checking)
        requests_throttled_check_box.setChecked(selected_vendor.needs_throttling)
        provider_edit.setText(selected_vendor.provider)
        notes_edit.setText(selected_vendor.notes)

        name_edit.textChanged.connect(
            lambda new_name: self.on_name_text_changed(
                new_name,
                selected_vendor.name,
                name_validation_label,
                selected_vendor.version,
            )
        )

        base_url_edit.textChanged.connect(
            lambda url: self.on_url_text_changed(url, url_validation_label, True)
        )

        def attempt_edit_vendor():
            vendor = Vendor51(
                name_edit.text(),
                selected_vendor.version,
                base_url_edit.text(),
                start_year.text(),
                customer_id_edit.text(),
                requestor_id_edit.text(),
                api_key_edit.text(),
                platform_edit.text(),
                two_attempts_check_box.isChecked(),
                ip_checking_check_box.isChecked(),
                requests_throttled_check_box.isChecked(),
                notes_edit.text(),
                provider_edit.text(),
            )

            is_valid, message = self.edit_vendor(
                vendor, selected_vendor, selected_vendor.version
            )
            if is_valid:
                self.sort_vendors()
                self.selected_index = -1
                if selected_vendor.version == "5.1":
                    self.on_click_version51()
                    self.update_vendors51_dat_file()
                else:
                    self.on_click_version50()
                    self.update_vendors_dat_file()
                edit_vendor_dialog.close()
            else:
                GeneralUtils.show_message(message)

        save_changes = edit_vendor_dialog_ui.saveVendorChangesButton
        save_changes.clicked.connect(attempt_edit_vendor)

        undo_changes = edit_vendor_dialog_ui.undoVendorChangesButton
        undo_changes.clicked.connect(lambda: edit_vendor_dialog.close())

        remove_vendor = edit_vendor_dialog_ui.removeVendorButton
        remove_vendor.clicked.connect(
            lambda: self.on_remove_vendor_clicked(edit_vendor_dialog)
        )

        edit_vendor_dialog.exec_()

    def update_vendor_while_importing(
        self, new_vendor: Vendor51, old_vendor: Vendor51, version: str
    ):
        is_valid, message = self.validate_url(new_vendor.base_url, version)
        if not is_valid:
            return is_valid, message
        if version == "5.1":
            self.vendors_v51.remove(old_vendor)
            self.vendors_v51.append(new_vendor)
            self.vendor_names_v51.remove(old_vendor.name.lower())
            self.vendor_names_v51.add(new_vendor.name.lower())
            self.sort_vendors()
            self.on_click_version51()
            self.update_vendors51_dat_file()
        else:
            self.vendors_v50.remove(old_vendor)
            self.vendors_v50.append(new_vendor)
            self.vendor_names_v50.remove(old_vendor.name.lower())
            self.vendor_names_v50.add(new_vendor.name.lower())
            self.sort_vendors()
            self.on_click_version50()
            self.update_vendors_dat_file()

        return True, ""

    def edit_vendor(
        self,
        new_vendor: Vendor51,
        original_vendor: Vendor51,
        version: str,
    ) -> tuple[bool, str]:
        # Check if vendor name is valid
        is_valid, message = self.validate_new_name(
            new_vendor.name, original_vendor.name, version
        )
        if not is_valid:
            return is_valid, message

        is_valid, message = self.validate_url(new_vendor.base_url, version)
        if not is_valid:
            return is_valid, message
        if new_vendor.customer_id == "":
            return False, "Customer Id cannot be empty."

        if version == "5.1":
            self.vendors_v51[self.selected_index] = new_vendor
            self.vendor_names_v51.add(new_vendor.name.lower())
            self.vendor_names_v51.remove(original_vendor.name.lower())
            self.sort_vendors()
            self.on_click_version51()
            self.update_vendors51_dat_file()
        else:
            self.vendors_v50[self.selected_index] = new_vendor
            self.vendor_names_v50.add(new_vendor.name.lower())
            self.vendor_names_v50.remove(original_vendor.name.lower())
            self.sort_vendors()
            self.on_click_version50()
            self.update_vendors_dat_file()

        return True, ""

    def on_remove_vendor_clicked(self, edit_vendor_dialog: QMainWindow):
        """Handles the signal emitted when the remove vendor button is clicked.

        A confirmation dialog is shown to confirm the removal of the vendor. The vendor is removed from the system if
        confirmed
        """
        dialog_remove = QDialog()
        dialog_remove_ui = RemoveVendorDialog.Ui_Dialog_remove()
        dialog_remove_ui.setupUi(dialog_remove)

        def remove_vendor():
            if self.selected_index >= 0:
                if self.curr_version == "5.0":
                    self.vendors_v50.pop(self.selected_index)
                    self.selected_index = -1
                    self.sort_vendors()
                    self.on_click_version50()
                    self.update_vendor_names()
                    self.update_vendors_dat_file()
                else:
                    self.vendors_v51.pop(self.selected_index)
                    self.selected_index = -1
                    self.sort_vendors()
                    self.on_click_version51()
                    self.update_vendor_names()
                    self.update_vendors51_dat_file()
                dialog_remove.close()
                edit_vendor_dialog.close()

        button_box = dialog_remove_ui.buttonBox
        button_box.accepted.connect(remove_vendor)
        button_box.rejected.connect(lambda: dialog_remove.close())
        dialog_remove.exec_()

    def update_settings(self, settings: SettingsModel):
        """Called when the settings are saved

        :param settings: the new settings"""
        self.settings = settings
