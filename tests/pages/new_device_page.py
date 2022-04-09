from tests.pages.locators.new_device_locators import NewDeviceLocators
from selenium.webdriver.support.ui import Select


class NewDevicePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.system_name = driver.find_element_by_xpath(NewDeviceLocators.system_name_input)
        self.system_type = driver.find_element_by_xpath(NewDeviceLocators.system_type_selection)
        self.hdd_capacity = driver.find_element_by_xpath(NewDeviceLocators.hdd_capacity_input)
        self.save_button = driver.find_element_by_xpath(NewDeviceLocators.save_button)

    def enter_system_name(self, name):
        self.system_name.send_keys(name)

    def make_device_selection(self, device_type):
        select = Select(self.system_type)
        select.select_by_visible_text(device_type)

    def enter_hdd_capacity(self, capacity):
        self.hdd_capacity.send_keys(capacity)

    def click_save_button(self):
        self.save_button.click()
