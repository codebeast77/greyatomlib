# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))

from q05_read_csv_data.build import read_ipl_data_csv
def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv('../../data/ipl_matches_small.csv', dtype='|S50')
    return len(set(ipl_matches_array[:, 0]))