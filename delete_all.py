#delete all 

import sqlite3

def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
        
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect("user.db")
        return conn
    except Error as e:
        print(e)

    return conn
    
c= create_connection()


def delete_all_users(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM users'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    
delete_all_users(c) 


#select from table

def select_all_users(conn):
    
    select_users = "SELECT * FROM users;"
    
    cur = conn.cursor()
    cur.execute(select_users)
    
    records = cur.fetchall()
    print("Total col are:  ", len(records))
    for col in records:
            print("Id: ", col[0])
            print("first_name: ", col[1]) 
            print("last_name: ", col[2])
            
select_all_users(c)
  
    
