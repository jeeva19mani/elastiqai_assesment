from src_files.workflow.helper import Helper
from src_files.testcases.locator_elements import Constants
from src_files.workflow.footprint_helper import FootprintHelper


class TestSelenium(Constants):
    """
    Class Tests Selenium for Tests
    """

    def test_validate_result(self):
        """
        Test to Validate the entities by Filtration
        """
        self.test_helper = Helper()
        self.print = FootprintHelper()
        self.print.step("Entering into HomePage of LambdaTest")
        self.test_helper.home_page()
        self.print.step("Verifying The Table Content")
        self.test_helper.table_content()
        input_text = "New York"
        self.print.step("Navigating through Search Bar")
        result_table_body = self.test_helper. \
            search_input(input_text)
        out_list = [i for i in result_table_body.text.split("\n")
                    if input_text in i]
        assert self.expected_output_count == len(out_list), \
            "Mismatch in count"
        self.print.info("Verified the Expected and Actual count"
                        " of the Search Result")
        f_result = self.test_helper.filter_content()
        f_result_1 = f_result.text.replace("(", "").replace(")", "")
        assert self.expected_filtered_result == f_result_1[18:], \
            f"Filtered output is Mismatch {f_result_1} "
        self.print.info(f"Verified the Expected:"
                        f"{self.expected_filtered_result} and"
                        f"Actual: {f_result_1[18:]} Search Result")
        self.test_helper.closing_browser()
