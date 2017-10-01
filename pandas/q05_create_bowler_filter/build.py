# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
from q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def create_bowler_filter(bowler):

    return (ipl_df['bowler'] == bowler)