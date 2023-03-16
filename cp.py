#%%
import os
import shutil
import tqdm
import argparse

parser = argparse.ArgumentParser(description='Copy files with progress bar')
parser.add_argument('source', type=str, help='Source folder')
parser.add_argument('destination', type=str, help='Destination folder')
args = parser.parse_args()

source_dir = args.source
destination_dir = args.destination
files_to_copy = ['test', 'filter.csv', 'sc_items.csv', 'test.csv', 'test_raw.csv', 'train.csv']

total_files = len(files_to_copy)

# 創建一個主進度條，顯示複製了多少個文件或文件夾
main_pbar = tqdm.tqdm(files_to_copy, desc="Files", total=total_files)

for item in main_pbar:
    src_path = os.path.join(source_dir, item)
    dst_path = os.path.join(destination_dir, item)
    if os.path.isfile(src_path):
        # 創建一個子進度條，顯示單個文件的複製情況
        file_size = os.path.getsize(src_path)
        sub_pbar = tqdm.tqdm(total=file_size, desc=item, leave=False)
        def file_progress(count, block_size, total_size):
            # 更新子進度條的值
            sub_pbar.update(min(count * block_size - sub_pbar.n, total_size))
        shutil.copyfile(src_path, dst_path)
        sub_pbar.close()
    elif os.path.isdir(src_path):
        # 複製整個文件夾，不顯示子進度條
        shutil.copytree(src_path, dst_path)

main_pbar.close()