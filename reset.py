import os
import shutil

os.rename('E:/IT School/Probleme/Curs35/test_file/content.txt','E:/IT School/Probleme/Curs35/content.txt')
os.remove('E:/IT School/Probleme/Curs35/test_file/logs.json')
shutil.rmtree('E:/IT School/Probleme/Curs35/test_file/versioning')