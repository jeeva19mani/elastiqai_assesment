class WebLocator:
    """
    Class Contains the Web Locators
    """
    base_url = ("https://www.lambdatest.com/"
                "selenium-playground/table-sort-search-demo")
    homepage_title = "div[class='container'] div[class='w-12/12']"
    table_id = "example_wrapper"
    search_filter_id = "example_filter"
    search_field = "//div[@id='example_filter'] //input"
    table_body = ("//div[@id='example_wrapper'] "
                  "//table[@id='example'] //tbody")
    filter_result = ("//div[@id='example_wrapper'] "
                     "//div[@id='example_info']")


class Constants:
    """
    Contains Expected Results
    """
    expected_output_count = 5
    expected_filtered_result = "5 entries filtered from 24 total entries"
