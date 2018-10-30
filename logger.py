import datetime


class Logger():
    data = ""
    
    
    def convertdatetime(self, tdate,  ttime):
        """
        >>> l = Logger()
        >>> print(l.convertdatetime("20181005", "22:00:00"))
        2018-10-05 22:00:00
        >>> print(l.convertdatetime("20181305", "22:00:00"))
        Traceback (most recent call last):
        ...
        ValueError: month must be in 1..12
        >>> print(l.convertdatetime("20181032", "22:00:00"))
        Traceback (most recent call last):
        ...
        ValueError: day is out of range for month
        >>> print(l.convertdatetime("20181005", "25:00:00"))
        Traceback (most recent call last):
        ...
        ValueError: hour must be in 0..23
        >>> print(l.convertdatetime("20181005", "22:63:00"))
        Traceback (most recent call last):
        ...
        ValueError: minute must be in 0..59
        >>> print(l.convertdatetime("20181005", "22:00:-17"))
        Traceback (most recent call last):
        ...
        ValueError: second must be in 0..59
        >>> print(l.convertdatetime("20181005", "22:00:77"))
        Traceback (most recent call last):
        ...
        ValueError: second must be in 0..59
        
        """
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
