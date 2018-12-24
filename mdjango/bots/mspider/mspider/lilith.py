import sqlite3
#connect = sqlite3.connect('database.db')#接数据库文件
#cursor = connect.cursor()#获取数据库游标

class DataBase(object):
    def __init__(self):
        self.name = "No database connected"
        self.connect = "No database connected"
        self.cursor = "No database connected"
    def link(self,name):#建立或链接数据库
        self.name = name
        self.connect = sqlite3.connect(self.name)#接收数据库文件
        self.cursor = self.connect.cursor()#获取数据库游标
    def create_table(self):
        if(self.name == "No database connected"):
            print("No database connected or established")
            return
        film_table = "CREATE TABLE Film (filmid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, type TEXT ,country TEXT ,date TEXT, boxoffice INTEGER ,score FLOAT)"#影片名、类型、国家、上映日期、票房、评分
        self.cursor.execute(film_table)
        actor_table = "CREATE TABLE Actor (actorid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, filmid INTEGER)"
        self.cursor.execute(actor_table)
        director_table = "CREATE TABLE Director (directorid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, filmid INTEGER)"
        self.cursor.execute(director_table)
    def film_in(self,film):#接收字典传入
        if(self.name == "No database connected"):
            print("No database connected or established")
            return
        insert_sql = "INSERT INTO Film(filmid, name, type, country, date, boxoffice, score) VALUES(NULL, "
        insert_sql = insert_sql + "'" +str(film['name']) + "'"  + ", "
        insert_sql = insert_sql +  "'" +str(film['type'])+ "'"  + ", "
        insert_sql = insert_sql +  "'" +''+ "'"  + ", "
        film['date'] = film['date'][0:10]
        insert_sql = insert_sql +  "'" +str(film['date'])+ "'"  + ", "
        if film['boxoffice'] == '':
            box = 0
        elif film['boxoffice'][-1] =='亿':
            box = float(film['boxoffice'][:-1])
            box = box * 10000
        elif film['boxoffice'][-1] == '万':
            box = float(film['boxoffice'][:-1])
        else:
            box = float(film['boxoffice']) / 10000
        insert_sql = insert_sql + str(box) + ", "
        insert_sql = insert_sql + str(film['score']) + ") "
        #print(insert_sql)
        self.cursor.execute(insert_sql)
        self.connect.commit()
    def actor_in(self,actor,film):#接收字典,film为string
        if(self.name == "No database connected"):
            print("No database connected or established")
            return
        select = "SELECT filmid, name FROM Film WHERE name = '" + film + "'"
        res = self.cursor.execute(select)
        for i in res:
            fid = i[0]
        #fid = res[0][0]
        insert_sql = "INSERT INTO Actor(actorid, name,filmid) VALUES(NULL, "
        insert_sql = insert_sql + "'" +str(actor['name']) + "'"  + ", "
        insert_sql = insert_sql + str(fid) + ")"
        self.cursor.execute(insert_sql)
        self.connect.commit()
    def director_in(self,director,film):#接收字典,film为string
        if(self.name == "No database connected"):
            print("No database connected or established")
            return
        select = "SELECT filmid, name FROM Film WHERE name = '" + film + "'"
        res = self.cursor.execute(select)
        for i in res:
            fid = i[0]
        #fid = res[0][0]
        insert_sql = "INSERT INTO Director(directorid, name,filmid) VALUES(NULL, "
        insert_sql = insert_sql + "'" +str(director['name']) + "'"  + ", "
        insert_sql = insert_sql + str(fid) + ")"
        self.cursor.execute(insert_sql)
        self.connect.commit()
    def film_out(self):
        return self.cursor.execute("select * from Film")
    def quit(self):#保存并退出数据库
        if(self.name == "No database connected"):
            print("No database connected or established")
            return
        self.connect.commit()
        self.cursor.close()
        self.connect.close()