from read_dir import read_filenames
from md5_calculator import md5_calculator
import sys

try:
    filename = sys.argv[1]
    i = 1
    for files in read_filenames(filename):
        full_path = filename+"/"+files
        # print(full_path)
        # print(type(full_path))
        # exit()
        md5_value = md5_calculator(full_path)
        print(str(i)+"-"+files+"  "+"[MD5 : "+md5_value+"]")
        i = i+1
except:
    print("Please use linux format to provide the path")
