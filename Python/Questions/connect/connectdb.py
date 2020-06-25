import sqlite3
def connect():
    conn = sqlite3.connect('C:\\Users\\DELL\\Desktop\\Questions\\test.db')
    cur=conn.cursor()
    return cur,conn
def select(conn):
    str1=''
    a=cur.execute('select * from dept');
    for i in a:
        s=','.join(i)
        str1=str1+s+'\n'
    return str1

if __name__ == '__main__':
    cur,conn=connect()
    with open('data.txt','r+') as d:
        for j in d.readlines():
            input=j.replace('\n','').split(',')
            #cur.execute(f'INSERT INTO dept (dept_no,d_name)'\
                      #f"VALUES ('{input[0]}','{input[1]}')")
    
    conn.commit()
    c=select(cur)
    print(c)
    conn.close()