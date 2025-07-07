# selenium_automation_testing

Target website: [https://the-internet.herokuapp.com/](https://the-internet.herokuapp.com/)

Built with **Python**, **Selenium WebDriver**, and the **unittest** framework, this project explores web automation challenges with a focus on problem-solving and test design.

Each feature pushes testing boundaries by requiring tricky element location, simulating user actions, or handling browser quirks, leading to both positive and negative test cases.

I chose `unittest` for its straightforward setup, native Python support, and emphasis on writing clear, maintainable tests.

The project includes a custom test runner, driver factory, debug files, a reusable test template, reusable explicit waits, a custom reporter, and documentation with instructions and commands.

👉 For a full Selenium framework implementation with POM and pytest, see: [selenium_automation_framework](https://github.com/marius-test/selenium_automation_framework)

---

### Test Independence

Each test runs **independently** with its own WebDriver instance, managed by a shared driver factory. This setup provides:

- Isolation to prevent shared state or test interference  
- Flexibility to run tests in any order or in parallel  
- Simplified debugging by isolating failures  
- A trade-off of speed for improved reliability and robustness

---

### Tools and Libraries

- **Python** - core programming language  
- **unittest** - testing framework  
- **Selenium WebDriver** - browser automation  
- **ChromeDriver**, **MSEdgeDriver**, and **GeckoDriver** (Firefox) - supported browsers
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
