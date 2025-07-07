import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# <========== TEST CASES STARTS HERE ==========>

import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver, quit_driver

# TEST DATA
URL = "https://the-internet.herokuapp.com"

# <========== TEST CASES ENDS HERE ==========>


if __name__ == "__main__":
    unittest.main(verbosity=2)
