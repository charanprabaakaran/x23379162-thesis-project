import sqlite3


#database conection
def connection():
    conn = sqlite3.connect('database.db', check_same_thread=False,timeout=10)
    cursor = conn.cursor()
    return cursor,conn

def select(username,password):
    cur,con=connection()
    cur.execute(f"select * from Users where Username='{username}' and password = '{password}'")
    res=cur.fetchone()
    return res
    


def insert(username,password,email):
    cur,con=connection()
    cur.execute(f"select * from Users where email='{email}'")
    res=cur.fetchone()
    if res:
        return "Email already exist!",400 

    else:
        try:
            cur.execute(f"insert into Users(Username,password,email) values ('{username}','{password}','{email}')")
            con.commit()

            return "Successfully inserted",200
        except Exception as e :
            return e,400

