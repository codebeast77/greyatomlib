# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..','..'))
import numpy as np

def create_3d_array():
    total_elements = 3 * 3 * 3
    array_1d = np.arange(total_elements)
    return array_1d.reshape(3, 3, 3)
