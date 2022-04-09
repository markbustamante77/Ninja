import json
import requests

from tests.pages.locators.ninja_locators import NinjaLocators
from tests.pages.new_device_page import NewDevicePage
from tests.pages.ninja_page import NinjaPage


def get_device_list_api(api):
    # hit device endpoint for list
    endpoint = api + 'devices'
    response = requests.get(url=endpoint)
    return response.text


def test_one(api, driver):
    device_list = get_device_list_api(api)
    # check for list of devices details in ui
    ninja_page = NinjaPage(driver)
    device_names = ninja_page.get_device_names()
    device_types = ninja_page.get_device_types()
    device_capacities = ninja_page.get_device_capacities()
    i = 0
    # assert device details in api list
    while i < len(device_names):
        assert device_names[i].text in device_list
        assert device_types[i].text in device_list
        assert device_capacities[i].text.split(' ')[0] in device_list
        i += 1
    # check that devices contain edit and delete buttons
    device_list = device_list.split('},')
    assert len(device_list) == len(driver.find_elements_by_xpath(NinjaLocators.edit_buttons))
    assert len(device_list) == len(driver.find_elements_by_xpath(NinjaLocators.remove_buttons))


def test_two(driver):
    new_device_sys_name = 'NEW DEVICE SYSTEM'
    new_device = 'MAC'
    new_device_capacity = '100'
    # click on add device button
    ninja_page = NinjaPage(driver)
    ninja_page.add_device_button_click()
    # enter new device details
    new_device_page = NewDevicePage(driver)
    new_device_page.enter_system_name(new_device_sys_name)
    new_device_page.make_device_selection(new_device)
    new_device_page.enter_hdd_capacity(new_device_capacity)
    new_device_page.click_save_button()
    # verify new device in list
    ninja_page = NinjaPage(driver)
    device_names = ninja_page.get_device_names()
    device_types = ninja_page.get_device_types()
    device_capacities = ninja_page.get_device_capacities()
    i = 0
    while i < len(device_names):
        if device_names[i].text == new_device_sys_name:
            assert device_types[i].text == new_device
            assert device_capacities[i].text == new_device_capacity + ' GB'
            break
        else:
            pass
        i += 1


def test_three(api, url, driver):
    # click first edit button
    driver.find_element_by_xpath('(//a[text()="Edit"])[1]').click()
    new_device_page = NewDevicePage(driver)
    sys_type = new_device_page.system_type.text.split('\n')[1]
    sys_cap = new_device_page.hdd_capacity.get_attribute('value')
    uid = driver.current_url.split('/')
    # add edit name string to api
    endpoint = api + 'devices/' + uid[-1]
    body = {
        "id": uid[-1],
        "system_name": "Renamed Device",
        "type": sys_type,
        "hdd_capacity": sys_cap
    }
    response = requests.put(url=endpoint, data=body)
    # get home page and assert top element is renamed
    driver.get(url)
    ninja_page = NinjaPage(driver)
    edited_names = ninja_page.get_device_names()
    assert edited_names[0].text == 'Renamed Device'


def test_four(api, url, driver):
    # get home page and gather names for comparison
    ninja_page = NinjaPage(driver)
    device_names = ninja_page.get_device_names()
    device_name_0 = device_names[0].text
    # click edit button on top element to get uid
    driver.find_element_by_xpath('(//a[text()="Edit"])[1]').click()
    new_device_page = NewDevicePage(driver)
    uid = driver.current_url.split('/')
    endpoint = api + 'devices/' + uid[-1]
    # delete via api
    response = requests.delete(url=endpoint)
    assert response.status_code == 200
    driver.get(url)
    # get home page anda assert item deleted
    ninja_page = NinjaPage(driver)
    new_device_names = ninja_page.get_device_names()
    assert len(device_names) != len(new_device_names)
    assert device_name_0 != new_device_names[0].text
