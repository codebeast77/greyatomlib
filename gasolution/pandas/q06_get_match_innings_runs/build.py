# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
from q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution

def get_match_innings_runs():
    innings_runs = ipl_df[['match_code', 'inning', 'runs']].groupby(['match_code', 'inning']).sum()
    return innings_runs