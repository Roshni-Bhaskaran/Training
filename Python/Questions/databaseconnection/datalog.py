import sqlite3
import logg_file
import configparser
class data_base():
    def connect(self,db_path):
        try:
            conn = sqlite3.connect(db_path)
            cur=conn.cursor()
            return cur,conn
        except Exception as e:
            return e
    def select(self,cur):
        str1=''
        try:
            a=cur.execute('select * from dept');
            for i in a:
                s=','.join(i)
                str1=str1+s+'\n'
                l1=logg_file.logg()
                l1.info("selected")
            return str1 
        except Exception as e:
            return e        
    def insert(self,cur,conn):
        try:
            ins=input('Enter the values ')
            inss=ins.split(',')     
            cur.execute(f'insert into dept (dept_no,d_name)'\
                      f"VALUES ('{inss[0]}','{inss[1]}')")
            conn.commit()
            l=logg_file.logg()
            l.info("inserted")
            return('inserted successfully')
        except Exception as e:
               return e            
    def update(self,cur,conn):
        try:
            up=input('Enter the values and col to be updated ')
            upp=up.split(',')
            cur.execute(f'update dept set {upp[0]} = "{upp[1]}" where {upp[2]} = "{upp[3]}"')         
            conn.commit()
            l=logg_file.logg()
            l.info("updated")
            return('updated successfully')
        except Exception as e:
            return e         

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('co.config')
    env='DEV'
    db_path=config.get(env,'db_log')
    obj=data_base()
    cur,conn=obj.connect(db_path)
    #l=obj.log_data()
    inp=input('Enter S to select,I to insert,U to update ')
    if inp=='S' or inp=='s':
        c=obj.select(cur)
        print(c)
    elif inp=='I' or inp=='i':
        n=obj.insert(cur,conn)
        print(n)
    elif inp=='U' or inp=='u':
        u=obj.update(cur,conn)
        print(u)
    conn.close()