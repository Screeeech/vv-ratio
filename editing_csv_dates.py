from datetime import timedelta
import pandas as pd
import glob


def edit_csv_dates():
    extension = 'csv'
    all_filenames = [i for i in glob.glob('S&P500 Prices/*.{}'.format(extension))]
    all_dfs = []
    for f in all_filenames:
        # Load csv
        temp_df = pd.read_csv(f)

        # Use filename to add data information
        temp_df['timestamp'] = pd.to_datetime(temp_df["timestamp"], format='%Y-%m-%d %H:%M:%S')
        temp_df['timestamp'] = temp_df['timestamp'] + timedelta(hours=17)
        temp_df.to_csv(f, sep='\t', encoding='utf-8')


if __name__ == '__main__':
    edit_csv_dates()
