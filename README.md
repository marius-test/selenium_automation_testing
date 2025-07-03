# selenium_automation_testing

Target website: [https://the-internet.herokuapp.com/](https://the-internet.herokuapp.com/)

Built with **Python**, **Selenium WebDriver**, and the **unittest** framework, this project explores complex web automation challenges with a focus on problem-solving and testing.

Each feature pushes testing boundaries, whether it’s locating tricky elements, simulating user behavior, or handling browser quirks, driving the creation of both positive and negative test cases.

I chose `unittest` for its simplicity, standard library support, and suitability for learning projects.

The project includes a custom test runner, debug tools, and a reusable test template. Future plans include a custom reporter and more fine-grained test control.

👉 For a full Selenium framework implementation, see: [selenium_automation_framework](https://github.com/marius-test/selenium_automation_framework)

---

### Test Independence

Each test runs **independently**, creating and managing its own WebDriver instance without a shared driver factory. This deliberate design supports the goal of stress-testing complex and tricky functionalities by:

- Ensuring tests do not share state or affect each other  
- Allowing tests to run in any order or parallel without interference  
- Making debugging easier by isolating failures  
- Accepting some overhead from repeated driver setup for maximum robustness

---

### Tools and Libraries

- **Python** - core programming language  
- **unittest** - testing framework  
- **Selenium WebDriver** - browser automation  
- **ChromeDriver** - main driver  
- **MSEdgeDriver** - alternative driver  
- **Visual Studio Code** - main IDE  
- **PyCharm** - secondary IDE  
- **GitHub** - version control system

---

### Status

🚧 This project is currently **in progress** and continuously evolving as I automate more features and refine test design and structure. 🚧
