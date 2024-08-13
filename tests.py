import unittest
import os

if __name__ == '__main__':
    # Get the directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the project root directory
    os.chdir(os.path.join(current_dir))
    
    # Discover and run tests
    test_suite = unittest.defaultTestLoader.discover('tests')
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)