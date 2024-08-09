import unittest


# Define a function to load and run tests
def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for test in tests:
        suite.addTests(loader.loadTestsFromModule(test))
    return suite


if __name__ == '__main__':
    # Create a test loader
    loader = unittest.TestLoader()

    # Discover and load all test cases from modules
    tests = loader.discover(start_dir='test', pattern='*_test.py')

    # Create a test runner
    runner = unittest.TextTestRunner()

    # Run the tests
    runner.run(tests)
