# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
import numpy as np
from q01_zeros_array.build import array_zeros

def array_reshaped_zeros():
    ans = array_zeros()
    return ans.reshape(2,3,4)
