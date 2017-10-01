#Default Imports
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.curdir),"..", '..'))

from greyatomlib import pandas as pd
from q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def create_delivery_series():
    return pd.Series(ipl_matches_array[:, 11])