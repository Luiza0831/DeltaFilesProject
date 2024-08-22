import os,shutil
if os.path.exists('test_file/content.txt'):
    os.rename('test_file/content.txt','content.txt')
    os.remove('test_file/logs.json')
    shutil.rmtree('test_file/versioning')