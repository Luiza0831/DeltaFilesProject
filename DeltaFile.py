import os,time,json,shutil

class DeltaFile():
    def __init__(self,path,textFilePath,mode):
        if mode not in ['generator','reader']:
            raise ValueError('Modul trebuie sa fie generator sau reader')
        self.path=path
        if mode=='generator':
            os.rename(textFilePath,path+'content.txt')
            os.makedirs(self.path+'versioning')
            shutil.copyfile(self.path+'content.txt',self.path+'versioning/v1.txt')
            modifiedTime=os.path.getmtime(self.path+'content.txt')
            self.__generate_log_file(modifiedTime)
            self.__listener()
        else:
            self.textfilePath=textFilePath

        
    def __generate_log_file(self,modifiedTime):        
        content={
            modifiedTime:"v1.txt"
        }
        self.__save_logs(content)
    
    def __get_logs(self):
        with open(self.path+'logs.json','r') as file: 
            content=json.load(file)
            return content
        
    def __save_logs(self,content):
        with open(self.path+'logs.json','w') as file:
            json.dump(content,file)

    def __generate_new_version(self,modifiedTime):
        versions=os.listdir(self.path+'versioning')
        maxVersion=max(versions).split('.')[0][1:]
        maxVersion=str(int(maxVersion)+1)
        shutil.copyfile('test_file/content.txt',f'test_file/versioning/v{maxVersion}.txt')
        content=self.__get_logs()
        content[modifiedTime]=f"v{maxVersion}.txt"
        self.__save_logs(content)

    def __listener(self):
       while True:
            print('In while')
            files=os.listdir(self.path)
            for file in files:
                if file.endswith('.txt'):
                        modifiedTime=os.path.getmtime(self.path+file)
                        if str(modifiedTime) not in self.__get_logs().keys():
                            self.__generate_new_version(modifiedTime)
                        else:
                            print('No changes!')
            time.sleep(3)

    def get_content(self,version=None,timestamp=None):
        '''Functia va returna fisierul de la o anumita data sau o anumita versiune 
        specificata la apelarea functiei'''
        filepath=self.path+self.textfilePath
        if version is not None:
            filepath=f'{self.path}versioning/v{version}.txt'
        elif timestamp is not None:
            logs=self.__get_logs()
            timestamp=str(timestamp)
            keys=[key for key in logs.keys()]
            if timestamp<keys[0]:
                raise ValueError('Timestampul este de dinainte ca fisierul sa fi fost creat')
            for i in range(len(keys)-1):
                if timestamp>keys[i] and timestamp<keys[i+1]:
                    ver=logs[keys[i]]
                if timestamp==keys[i]:
                    ver=logs[keys[i]]
            filepath=f'{self.path}versioning/{ver}'
            if timestamp>keys[-1]:
                filepath=f'{self.path}versioning/{logs[keys[-1]]}'
        try:
            with open(filepath,'r')as file:
                content=file.read()
                return content
        except FileNotFoundError:
            return 'Versiunea introdusa nu exista!'