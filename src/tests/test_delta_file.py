import os,sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)
from delta_file import DeltaFile

df=DeltaFile('E:/IT School/Probleme/Curs35/test_file/', 'E:/IT School/Probleme/Curs35/','content.txt','generator')