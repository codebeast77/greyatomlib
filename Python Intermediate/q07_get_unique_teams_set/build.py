# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'))

from q06_get_unique_matches_count.build import read_ipl_data_csv

def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv('../../data/ipl_matches_small.csv', dtype='|S50')
    team1_set = set(ipl_matches_array[:, 3])
    team2_set = set(ipl_matches_array[:, 4])
    return team1_set.union(team2_set)