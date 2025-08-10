import unittest
import HtmlTestRunner
import importlib  # dynamic importing of modules like test0_smoke.py
import sys
import os

# add project root directory to sys.path so 'tests' package can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

test_modules = [
    'test0_smoke'
]
report_dir = "debug/"

if __name__ == "__main__":
    for module_name in test_modules:
        print(f" Running {module_name}...")
    
        # importing the test modules from the "tests" package (folder)
        full_module_name = f"tests.{module_name}"
        module = importlib.import_module(full_module_name)
        
        # load tests from the module
        suite = unittest.defaultTestLoader.loadTestsFromModule(module)
        
        # define HtmlTestRunner
        runner=HtmlTestRunner.HTMLTestRunner(
            output=report_dir,
            report_name=f"{module_name}_debug_report",
            combine_reports=True,
            add_timestamp=False
        )
        
        # run the test suite
        runner.run(suite)
        
        print(f"Done: {module_name}_debug_report.html\n")
