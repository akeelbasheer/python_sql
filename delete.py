#delete the table/user
import sqlite3

first_name = input("Please enter a firstname of the user :\n")

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

def delete_user(conn,user):
    
    sql = ''' DELETE FROM users
              WHERE first_name = ?'''
    cur = conn.cursor()
    cur.execute(sql, (user,))
    conn.commit()    
user = first_name

delete_user(c,user)

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


