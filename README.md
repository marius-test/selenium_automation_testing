# selenium_automation_testing

Target website: [https://the-internet.herokuapp.com/](https://the-internet.herokuapp.com/)

Built with **Python**, **Selenium WebDriver**, and the **unittest** framework, this project explores web automation challenges with a focus on problem-solving and test design.

Each feature pushes testing boundaries by requiring tricky element location, simulating user actions, or handling browser quirks, leading to both positive and negative test cases.

I chose `unittest` for its simplicity, built-in support, and suitability for learning-focused projects.

The project includes a custom test runner, debug tools, and a reusable test template. Future plans include a custom reporter and more granular test control.

👉 For a full Selenium framework implementation, see: [selenium_automation_framework](https://github.com/marius-test/selenium_automation_framework)

---

### Test Independence

Each test runs **independently**, creating and managing its own WebDriver instance without a shared driver factory. This supports stress-testing complex features by:

- Preventing shared state or test interference  
- Allowing any test order or parallel execution  
- Simplifying debugging by isolating failures  
- Trading speed for greater reliability and robustness

---

### Tools and Libraries

- **Python** – core programming language  
- **unittest** – testing framework  
- **Selenium WebDriver** – browser automation  
- **ChromeDriver** – main driver  
- **MSEdgeDriver** – alternative driver  
- **Visual Studio Code** – main IDE  
- **PyCharm** – secondary IDE  
- **GitHub** – version control system

---

### Status

🚧 This project is currently **in progress** and evolving as I automate more features and refine test design. 🚧
