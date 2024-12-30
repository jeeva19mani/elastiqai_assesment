from src_files.workflow.selenium_operations import \
    SeleOperation
from src_files.testcases.locator_elements import WebLocator, Constants
from src_files.workflow.footprint_helper import FootprintHelper


class Helper(WebLocator, Constants):

    def __init__(self):
        self.sele_op = SeleOperation(self.base_url)
        self.foot = FootprintHelper()

    def home_page(self):
        """
        Validates the landing page
        return: Nothing
        """
        validate_home = self.sele_op.wait_for_element_visible(
            "css", self.homepage_title)
        assert validate_home is not False, \
            "Home Page Title is unavailable"
        self.foot.info(f'Entered into HomePage')

    def table_content(self):
        """
        Verifies the Table is visible
        """
        element = self.sele_op.wait_for_element_visible(
            "id",self.table_id)
        assert element is not False, "Table content is Invisible"
        self.foot.info(" Verified the Table is visible")

    def search_input(self, input_text):
        """
        To search and return the Result
        param input_text: Input text to be entered
        return: Table Body content
        """
        self.sele_op.wait_for_element_visible(
            "id", self.search_filter_id)
        self.foot.info(" Verified the Search bar is visible")
        text = self.sele_op.get_element("xpath",
                                        self.search_field)
        self.foot.step("Entering the Input")
        text.send_keys(input_text)
        t_body = (self.sele_op.wait_for_element_visible
                  ("xpath", self.table_body))
        assert t_body is not False, "Table Element is Unavailable"
        self.foot.info("Returning the Table Body Content")
        return t_body

    def filter_content(self):
        """
        return: Filtered result
        """
        f_result = self.sele_op.get_element("xpath",
                                            self.filter_result)
        assert f_result is not False, "Table Element is Unavailable"
        self.foot.info("Returning the Filter Message Content")
        return f_result
