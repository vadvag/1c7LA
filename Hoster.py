import sqlite3


class DB():
     
    def __init__(self):
        con = sqlite3.connect("loggerdb.db")
        self.cur = con.cursor()
        self.cur.execute("""CREATE TABLE if not exists rawdata 
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
        

    
    
if __name__ == "__main__":
    print(1)
    db = DB()
    sql = sqlite3
