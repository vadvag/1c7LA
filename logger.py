class Logger():
    data = ""
    
    def read(self,  filename):
        print(2)
        with open(filename,  'rt', encoding='cp1251') as f:
            #fn = f.readline()
            for line in f:
                print(1)
                self.data = line
                print(self.data)
            
        print('read filename {}'.format(filename))
        
    def __init__(self):
        ...
        
    def __del__(self):
        ...

if __name__ == '__main__':
    logger = Logger()
    logger.read("/home/pavlo72/XPCommon/1cv7.mlg")
    print(logger.data)
    
