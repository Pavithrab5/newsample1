import os
import re
import time
import win32api

start=time.perf_counter()
class Find_File_Location:
    start = time.perf_counter()
    def find_file(self, root_folder,rex):
        list_drives=[]
        for root, dirs, files in os.walk(root_folder):
            for file in files:
                result = rex.search(file)
                if result:
                    list_drives.append(os.path.join(root,file))
        return list_drives


    def find_file_in_all_drives(self, file_name):
        # create a regular expression for the file
        rex = re.compile(file_name)
        list_all_drives=[]
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            if Find_File_Location().find_file(drive,rex):
                list_all_drives.append(Find_File_Location().find_files(drive,rex))
            return list_all_drives
obj_Find_File_Location=Find_File_Location()
print(obj_Find_File_Location.find_file_in_all_drives('SAMPLE.txt'))
finish=time.perf_counter()
print(f'time= {finish-start} seconds')

