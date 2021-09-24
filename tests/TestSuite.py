
# set test modules path
import sys
import pathlib

curr_path = str(pathlib.Path(__file__).parent.resolve())
sys.path.insert(0, curr_path + "/modules")

# import test modules

import Greedy_test
import DivideAndConquer_test
import DynamicProgramming_test

# init test suite
import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Greedy_test))
suite.addTests(loader.loadTestsFromModule(DivideAndConquer_test))
suite.addTests(loader.loadTestsFromModule(DynamicProgramming_test))

# run test cases
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)