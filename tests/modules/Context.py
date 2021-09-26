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
