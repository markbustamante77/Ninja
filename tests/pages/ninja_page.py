from tests.pages.locators.ninja_locators import NinjaLocators


class NinjaPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.device_names = driver.find_elements_by_xpath(NinjaLocators.device_names)
        self.device_types = driver.find_elements_by_xpath(NinjaLocators.device_types)
        self.device_capacities = driver.find_elements_by_xpath(NinjaLocators.device_capacities)
        self.add_device_button = driver.find_element_by_xpath(NinjaLocators.add_device_button)

    def get_device_names(self):
        return self.device_names

    def get_device_types(self):
        return self.device_types

    def get_device_capacities(self):
        return self.device_capacities

    def add_device_button_click(self):
        self.add_device_button.click()
