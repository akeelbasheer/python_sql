import sqlite3
from shutil import copyfile

first_name = input("Please enter a firstname :\n")
last_name = input("Please enter a lastname :\n")
phone_number = input("Please enter a phonenumber :\n")
user_image = input("Please enter a imagepath :\n")
#/home/user/Downloads/johann-siemens-EPy0gBJzzZU-unsplash.jpg

#connect to database
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
    
c = create_connection()

#The SQL neccessary to create the table
create_table_sql = '''CREATE TABLE IF NOT EXISTS users (
	id integer PRIMARY KEY,
	first_name text NOT NULL,
	last_name text NOT NULL,
	phone_number text NOT NULL,
	user_image text NOT NULL
	
);'''

#The functions to create the table
def create_table(conn, create_table_sql):
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
create_table(c,create_table_sql)
        
#The functions to insert the user / create user 
user = (first_name, last_name, phone_number, user_image);
def create_user(conn, user):
    
    sql = ''' INSERT INTO users (first_name, last_name, phone_number, user_image)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    
    
        
    return cur.lastrowid
    
id = create_user(c,user)

des =  "/home/user/Documents/Python_projects/SQL/static/"+str(id)+".jpg"
       
copyfile(user_image, des)


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


        
        
        
