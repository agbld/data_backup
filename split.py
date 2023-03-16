import os
import pandas as pd
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description='Split a csv file into chunks')
parser.add_argument('file_path', type=str, help='Path to csv file')
args = parser.parse_args()

# define the directory to scan
directory = args.file_path

# define the size limit for csv files in bytes
size_limit = 50 * 1024 * 1024 # 50mb

# loop through all files in the directory
for filename in os.listdir(directory):
    # check if the file is a csv file
    if filename.endswith(".csv"):
        # get the full path of the file
        filepath = os.path.join(directory, filename)
        # get the size of the file
        filesize = os.path.getsize(filepath)
        # check if the file is larger than size limit
        if filesize > size_limit:
            # read the csv file using pandas
            df = pd.read_csv(filepath)
            # get the number of rows of the csv file
            nrows = len(df)
            # calculate the number of chunks to split
            nchunks = (filesize // size_limit) + 1
            # calculate the number of rows per chunk
            chunksize = nrows // nchunks + 1 
            # loop through each chunk using tqdm for progress bar
            for i, (group, chunk) in tqdm(enumerate(df.groupby(pd.np.arange(nrows) // chunksize))):
                # get the new file name with suffix "_split.N"
                new_filename = filename.replace(".csv", f"_split.{i+1}.csv")
                # get the new file path 
                new_filepath = os.path.join(directory, new_filename)
                # save the chunk as a new csv file using pandas 
                chunk.to_csv(new_filepath, index=False)
            os.remove(filepath)