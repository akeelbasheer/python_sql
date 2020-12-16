#updating the table/user
import sqlite3
from shutil import copyfile

id = input("Please enter a user_id of the user :\n")
first_name = input("Please enter a firstname of the user :\n")
last_name = input("Please enter a lastname of the user :\n")
phone_number = input("Please enter a phonenumber :\n")
user_image = input("Please enter a imagepath :\n")


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

def update_user(conn,user):
    
    des =  "/home/user/Documents/Python_projects/SQL/static/"+user[4]+".jpg"
       
    copyfile(user_image, des)    
    
    sql = ''' UPDATE users 
             SET last_name = ? ,
                  first_name = ? ,
                  phone_number = ? ,
                  user_image = ?
              WHERE id = ?'''
              
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()    
user = (last_name, first_name, phone_number, user_image, id);

update_user(c,user)

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
            print("phone_number: ", col[3]) 
            print("user_image: ", col[4])
            
select_all_users(c)


