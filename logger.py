class Logger():
    data = ""
    
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
    logger.read("/home/pavlo72/XPCommon/1cv7.mlg")
    print(logger.data)
    
