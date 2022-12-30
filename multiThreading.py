import os
import re
import time
import win32api
import concurrent.futures

start=time.perf_counter()


def find_file(self, root_folder, rex):
    list_drives = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            result = rex.search(file)
            if result:
                list_drives.append(os.path.join(root, file))
                print(list_drives)


def find_file_in_all_drives(self, file_name):
    # create a regular expression for the file
    rex = re.compile(file_name)
    Drive=win32api.GetLogicalDriveStrings().split('\000')[:-1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tr=[executor.submit(find_file, drive, rex) for drive in Drive]
    for i in concurrent.futures.as_complete(tr):
        i.result()
print(find_file_in_all_drives,'SAMPLE.txt')
finish = time.perf_counter()
print(f'time= {finish - start} seconds')

