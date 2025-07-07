# selenium_automation_testing

Target website: [https://the-internet.herokuapp.com/](https://the-internet.herokuapp.com/)

This project explores web automation challenges with a focus on problem-solving and test design, and it is built with **Python**, **Selenium WebDriver**, and the **unittest** framework.

Each feature pushes testing boundaries by requiring tricky element location, simulating user actions, or handling browser quirks, leading to both positive and negative test cases.

I chose `unittest` for its straightforward setup, native Python support, and a strong emphasis on writing clear, maintainable tests.

The project includes a custom test runner, driver factory, debug files, a reusable test template, reusable explicit waits, a custom reporter that generates clean HTML reports, and detailed documentation with instructions and commands.

Tests are organized in multiple modules covering sub-pages of the website. Each module targets specific functionalities, providing a robust foundation to expand coverage.

---

### Test Independence

Each test runs **independently** with its own WebDriver instance, created and managed by a shared driver factory. This setup provides:

- Isolation to prevent shared state or test interference  
- Flexibility to run tests in any order or in parallel  
- Simplified debugging by isolating failures  
- A trade-off of speed for improved reliability and robustness  

---

### Requirements and Setup

- Python 3.x  
- Dependencies managed via `requirements.txt`  
- See the documentation in the `docs/` folder at the root of the project for detailed setup and usage instructions.

---

### Handling Flaky Tests

The framework uses reusable explicit waits and safe waiting utilities to handle dynamic page elements and improve test stability.

---

### Tools and Libraries

- **Python** - core programming language  
- **unittest** - testing framework  
- **Selenium WebDriver** - browser automation  
- **ChromeDriver** - browser driver
- **webdriver-manager** - automatic driver management  
- **requests**, **urllib3** - HTTP clients for API testing  
- **pyautogui**, **pynput** - keyboard/mouse automation and input capturing  
- **html-testRunner** - HTML reports for unittest suites  
- **Visual Studio Code**, **PyCharm** - IDEs  
- **GitHub** - version control  

---

### Status

✅ This project is **complete** and provides a robust, scalable automation framework.  
📈 Future work primarily involves adding more tests to cover additional pages and scenarios.
