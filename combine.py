import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Combine csv files into one')
parser.add_argument('file_path', type=str, help='Path to csv file')
args = parser.parse_args()

# define the directory to scan
directory = "path/to/directory"

# define the original file name without suffix
original_filename = "data.csv"

# create an empty list to store the chunk dataframes
chunks = []

# loop through all files in the directory
for filename in os.listdir(directory):
    # check if the file is a chunk of the original file
    if filename.startswith(original_filename.replace(".csv", "_split.")) and filename.endswith(".csv"):
        # get the full path of the file
        filepath = os.path.join(directory, filename)
        # read the csv file using pandas and append it to the list
        df = pd.read_csv(filepath)
        chunks.append(df)

# concatenate all chunks into one dataframe using pandas
combined_df = pd.concat(chunks)

# save the combined dataframe as a new csv file using pandas 
combined_df.to_csv(os.path.join(directory, original_filename), index=False)