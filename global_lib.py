from Selenium2Library import Selenium2Library
from robot.api import logger

__all__ = ['Global']

class Global:
    global browser
    browser = Selenium2Library()

    @staticmethod
    def open_browser(self, url, browser_name='firefox', desired_capabilities=None, ff_profile_dir=None):
        """
        Open the browser and creates a connection alias to the browser object.
        | url | url of the page to be launched |
        | browser_name | name of the browser |
        | desired_capabilities | expected capabilities if any |
        | ff_profile_dir | FF profile directory details |

        Example:
        | Open Browser | https:\\www.google.com | chrome |

        Return:
            None
        """
        browser.open_browser(url, browser=browser_name,
                          desired_capabilities=desired_capabilities,
                          ff_profile_dir=ff_profile_dir)
        # Maximize Browser Window
        browser.maximize_browser_window()
        logger.info("Successfully Opened Browser Connection")

    @staticmethod
    def close_browser(self):
        """
        close the browser and deletes the connection alias and browser object references .
        | browser_alias |  alias of the browser |

        Example:
        | Close Browser | browser_1 |

        Return:
            None
        """
        browser.close_browser()
        logger.info("Closed Browser")

    @staticmethod
    def input_text(self, locator, text):
        for _ in xrange(3):
            try:
                browser.wait_until_element_is_visible(locator)
                browser.input_text(locator, text)
                break
            except:
                browser.wait_until_element_is_visible(locator)

    @staticmethod
    def click_element(self,locator):
        browser.wait_until_page_contains_element(locator)
        browser.wait_until_element_is_visible(locator)
        browser.click_element(locator)