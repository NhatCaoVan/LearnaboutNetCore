#!/usr/bin/env python3
import unittest
import os
import sys
import traceback

if __name__ == "__main__":
    try:
        # Set up the path properly
        project_root = os.path.abspath(os.path.dirname(__file__))
        sys.path.insert(0, project_root)
        
        # Print all environment details for debugging
        print(f"Python version: {sys.version}")
        print(f"System path: {sys.path}")
        print(f"Current directory: {os.getcwd()}")
        print(f"Project root: {project_root}")
        print(f"Directory contents: {os.listdir(project_root)}")
        
        # Try to import the calculator module directly as a test
        print("Testing direct import of calculator module...")
        try:
            import calculator
            print(f"Successfully imported calculator from {calculator.__file__}")
            print(f"add_numbers(5, 3) = {calculator.add_numbers(5, 3)}")
        except Exception as e:
            print(f"Error importing calculator module: {e}")
            print(traceback.format_exc())
        
        # Print test directory contents
        test_dir = os.path.join(project_root, 'tests')
        if os.path.exists(test_dir):
            print(f"Test directory contents: {os.listdir(test_dir)}")
        else:
            print(f"Test directory not found at {test_dir}")
        
        # Discover and run tests
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover('tests', pattern='test_*.py')
        
        test_runner = unittest.TextTestRunner(verbosity=2)
        result = test_runner.run(test_suite)
        
        # Exit with non-zero code if tests failed
        sys.exit(not result.wasSuccessful())
    
    except Exception as e:
        print(f"Error in run_tests.py: {e}")
        print(traceback.format_exc())
        sys.exit(1) 