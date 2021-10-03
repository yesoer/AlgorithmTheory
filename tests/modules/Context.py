import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../../src')))

from DivideConquer import DivideAndConquer  # nopep8
from DynamicProgramming import DynamicProgramming  # nopep8
from Greedy import Greedy  # nopep8

############
# Helper
############


def run_cases(self, cases, to_test):
    # a case is a tuple (input, expected result) where input is a list
    # [arg1, arg2 ...]
    for _input, expected in cases:
        print(
            "\n\ntesting input : ",
            _input,
            "\nwith expected output : ",
            expected,
            "\n")
        output = to_test(*_input)
        self.assertEquals(output, expected)
