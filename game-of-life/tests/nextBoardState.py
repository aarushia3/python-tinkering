import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import numpy as np

from testUtils import test
from life import nextBoardState

def nextBoardStateTests():
    test1 = "dead cells with no live neighbors"
    init_state1 = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])

    expected_next_state1 = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])

    actual_next_state1 = nextBoardState(init_state1)
    test(expected_next_state1, actual_next_state1, test1)