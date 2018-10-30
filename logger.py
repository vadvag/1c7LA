import datetime

class Logger():
    data = ""
    
    def convertdatetime(self, tdate,  ttime):
        _tm = ttime.split(":")
        _rawdata = datetime.datetime(int(tdate[:4])
                                    , int(tdate[4:6])
                                    , int(tdate[6:8])
                                    , int(_tm[0]) 
                                    , int(_tm[1])
                                    , int(_tm[2]))
        return _rawdata
    
    def read(self,  filename):
        with open(filename,  'rt', encoding='cp1251') as f:
            for line in f:
                self.data = line #debug info
                print(self.data) #debug info. print last line.
        
        #print('read filename {}'.format(filename))
        
    def __init__(self):
        ...
        
    def __del__(self):
        ...

if __name__ == '__main__':
    logger = Logger()
    #logger.read("/home/pavlo72/XPCommon/1cv7.mlg")
    #print(logger.data)
    print(logger.convertdatetime("20181005", "22:00:00"))
