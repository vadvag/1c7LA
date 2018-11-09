import datetime
import fileinput
import Hoster


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
    
    def decode(self, dline):
        tmp = dline.split(";")
        d = {}
        d['datetime'] = self.convertdatetime(tmp[0], tmp[1])
        d['user'] = tmp[2]
        d['mode'] = tmp[3]
        d['objtype'] = tmp[4]
        d['action'] = tmp[5]
        d['wtf2'] = tmp[6]
        d['wtfr'] = tmp[7]
        d['objid'] = tmp[8]
        d['descr'] = tmp[9]
        print(d) #debug info
        return d


    def read(self,  filename):
        #with open(filename,  'rt', encoding='cp1251') as f:
        with open(filename,  'rt') as f:    
            for line in f:
                self.ldb.add(self.decode(line.rstrip('\n'))) 

        
    def read1(self,  filename):
        for line in fileinput.input([filename]):
            self.data = line #debug info
            print(self.data) #debug info. print last line.

        
    def __init__(self, dbase):
        self.ldb = dbase
    
    
    def __del__(self):
        ...

        
if __name__ == '__main__':
    db = Hoster.DB()
    cur = db.con.cursor()
    cur.execute("select * from rawdata where ((user = 'prg') and (action='OpenSession'))")
    print(cur.fetchall())
    #logger = Logger(db)
    #    logger.read("/home/pavlo72/XPCommon/test.mlg")
#    print(logger.data)
