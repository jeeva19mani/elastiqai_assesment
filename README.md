# QA Selenium Automation with Python

Here we are Automating the UI of LambdaTest https://www.lambdatest.com/selenium-playground/table-sort-search-demo Selenium-Playground page to validate search functionality.

## Feature
- Opens the Selenium-Playground Page,
- Validating Search Functionality of that page.
- Chrome Browser used in this Testing

## Prerequisites
- `Python` 3.9.6 or higher
- `selenium` 4.27.1 or higher Library
- `pytest` 8.3.4 or higher Library
- `Chrome` 131.0.6778.205 or higher

## Environmental Setup
- Attached Bash Script for venv setup `test_venv_setup.sh`
- Execute this setup script on console`./test_venv_setup.sh` or `sh test_venv_setup.sh`

# Workflow File Details
- files available under `src_files/workflow/`.

### selenium_operations.py
- First started with `selenium_operations.py`. Here we imported selenium library.
- Drawn the methods for browser actions.
- First created a Static Method `get_locator_type` it returns the Type of the Locator required for `SeleOperation` Class.
- Since it doesn't need any dependency of a class.
- declared`SeleOperation` class
- `__init__()` Constructor Function of `SeleOperation` Class takes source web url to start Chrome browser later we are maximizing it and implicitly waiting for 10 sec to load completely.
- then`wait_for_element_visible`, functions implemented with explicit wait. It waits until the web element to present be later returns it. Added`try` block and handled expected `TimeoutException` exception. if the exception Varies it will raise that exception.
- `get_element` Function returns the web element.  Added`try` block and handled expected `NoSuchElementException` exception.
- `close_browser` It closes the browser once all the operations completes.
### helper.py
- This file imports the class `SeleOperation` from `selenium_operations.py`.
- Here we have all the helper files with test actions.
- `Helper` class implemented with multiple inheritance of classes `WebLocator` and `Constants`.
- `__init__()` Constructor Function initialises `SeleOperation` class by passing the source web url and `FootprintHelper` Class.
- `home_page` functions validates the Selenium-playground page on it's first landing.
- `table_content`functions validates the table content.
- `search_input`functions verifies the search bar, And it will enter the `input text`. finally returns the filtered table body content.
- `filter_content`functions verifies the result of the searched test.
- The above each function has the Assertion function to verify the expected outcome from the respective operation.
- `final_cleanup` it just closes the browser.
### footprint_helper.py
- Simple logging file returns the level of the operations and timing.
- By importing datetime module initialised in `FootprintHelper` constructor file.
- `info` and `step` two basic log functions prints the message in formatted way.

# Testcases File Details
- files available under `src_files/testcases/`

### locator_elements.py
- Based on Page Object Module structure of Selenium created a separate file for web locators. 
- Holds two classes `WebLocator` and `Constants` has the web locators and expected output constants.
### qa_selenium_test.py
- test case file imported `Helper`, `Constants` and `FootprintHelper`classes.
- `TestSelenium` class inherited `Constants` class.
- Starting by initializing `Helper` and `FootprintHelper1` classes.
- later called `home_page`, `table_content` functions from `Helper` class.
- then passing the input argument to the `search_input` and from the returned value asserting with the expected table body count.
- Finally, verified the expected filtered result.

## To Run a File
- Execute `test_venv_setup.sh` file by `./test_venv_setup.sh` or `sh test_venv_setup.sh`. It will install the required softwares, libraries and create Virtual Environment to execute the test.
- Use `python3 -m pytest -s (use entire file path) test file.py::class name::testcase name`
- Or Use Pycharm IDE or other IDE import pytest module into it. then Configure the run console and run it.  
