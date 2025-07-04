# selenium_automation_testing

Target website: [https://the-internet.herokuapp.com/](https://the-internet.herokuapp.com/)

Built with **Python**, **Selenium WebDriver**, and the **unittest** framework, this project explores web automation challenges with a focus on problem-solving and test design.

Each feature pushes testing boundaries by requiring tricky element location, simulating user actions, or handling browser quirks, leading to both positive and negative test cases.

I chose `unittest` for its straightforward setup, native Python support, and focus on writing clear, maintainable tests.

The project includes a custom test runner, driver factory, debug files, a reusable test template, a custom reporter, and documentation with instructions and commands.

👉 For a full Selenium framework implementation, see: [selenium_automation_framework](https://github.com/marius-test/selenium_automation_framework)

---

### Test Independence

Each test runs **independently** with its own WebDriver instance, which is created and managed by a shared driver factory. This setup provides:

- Preventing shared state or test interference  
- Allowing any test order or parallel execution  
- Simplifying debugging by isolating failures  
- Trading speed for greater reliability and robustness

---

### Tools and Libraries

- **Python** - core programming language  
- **unittest** - testing framework  
- **Selenium WebDriver** - browser automation  
- **ChromeDriver** - main driver  
- **MSEdgeDriver** - alternative driver  
- **webdriver-manager** - auto-downloads and manages browser drivers (Chrome, Firefox, etc.)  
- **requests** - simple HTTP requests for REST API testing  
- **urllib3** - low-level HTTP library (used internally by requests)  
- **pyautogui** - automates keyboard/mouse actions outside browser scope (e.g., file uploads)  
- **pynput** - captures keyboard/mouse input, useful for simulating complex user behavior  
- **html-testRunner** - generates clean and readable HTML test reports for unittest-based test suites  
- **Visual Studio Code** - main IDE  
- **PyCharm** - secondary IDE  
- **GitHub** - version control system  

---

### Status

🚧 This project is currently **in progress** and evolving as I automate more features and refine test design. 🚧
