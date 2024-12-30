from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src_files.workflow.footprint_helper import FootprintHelper


def get_locator_type(locator_type):
    if locator_type == "xpath":
        return By.XPATH
    elif locator_type == "css":
        return By.CSS_SELECTOR
    elif locator_type == "id":
        return By.ID
    elif locator_type == "class":
        return By.CLASS_NAME
    elif locator_type == "link":
        return By.LINK_TEXT


class SeleOperation:

    def __init__(self, url):
        self.foot = FootprintHelper()
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=10)

    def wait_for_element_visible(self, locator_type, locator):

        try:
            wait = WebDriverWait(self.driver, timeout=20)
            condition = (EC.presence_of_element_located
                         ((get_locator_type(locator_type), locator)))
            element = wait.until(condition,
                                 f"Element is unavailable {locator}")
            return element

        except TimeoutException:
            self.foot.info(f"Sorry ! Element is unable to Locate {locator}")
            return False

        except Exception as e:
            self.foot.info(f"Error occurred {e} ")
            raise e

    def get_element(self, locator_type, locator):

        try:
            element = self.driver.find_element(get_locator_type(locator_type), locator)
            return element

        except NoSuchElementException:
            self.foot.info(f"Sorry ! Element is unable to Locate {locator}")
            return False

        except Exception as e:
            self.foot.info(f"Error occurred {e} ")
            raise e
