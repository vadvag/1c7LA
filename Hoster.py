import sqlite3


class DB():
     
    def __init__(self):
        self.con = sqlite3.connect("loggerdb.db")
        cur = self.con.cursor()
        cur.execute("""CREATE TABLE if not exists rawdata 
                                                (id int auto_increment primary key
                                                ,datetime datetime
                                                ,user varchar(50)
                                                ,mode varchar(1)
                                                ,objtype varchar(150)
                                                ,action varchar(50)
                                                ,wtf2 varchar(2)
                                                ,wtfr varchar(20)
                                                ,objid varchar(30)
                                                ,descr varchar(200))""")
        
    def add(self, dline):
        sqltext = ''' INSERT INTO rawdata(datetime,user,mode,objtype,action,wtf2,wtfr,objid,descr)
              VALUES(?,?,?,?,?,?,?,?,?) '''
        cur = self.con.cursor()
        cur.execute(sqltext,    ( dline["datetime"]
                                , dline["user"]
                                , dline["mode"]
                                , dline["objtype"]
                                , dline["action"]
                                , dline["wtf2"]
                                , dline["wtfr"]
                                , dline["objid"]
                                , dline["descr"]))
        self.con.commit()
        #return self.cur.lastrowid
        
    #def update(self):
    #    self.cur.
    
    
if __name__ == "__main__":
    print(1)
    db = DB()
    sql = sqlite3
