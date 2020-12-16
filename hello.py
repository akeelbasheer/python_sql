import sqlite3
from flask import Flask, request,render_template, redirect, send_from_directory
import app
import os


app = Flask(__name__)




@app.route('/')
def home_page():
 
    message = "My, Fullstack app"
    return render_template('index.html', message=message)

@app.route('/users')
def get_all_users_page():

    #connect to database
    conn = sqlite3.connect("user.db")
 
    select_users = "SELECT * FROM users;"
    
    cur = conn.cursor()
    cur.execute(select_users)
    
    users = cur.fetchall()
    
    print("Total col are:  ", len(users))
    
    return render_template('users.html', users=users)
    

@app.route('/user/<int:id>')
def get_single_user_page(id):

    #connect to database
    conn = sqlite3.connect("user.db")
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (id,))

    user = cur.fetchone()
    return render_template('user.html', user=user)
@app.route('/delete/<int:id>')
def delete_single_user(id):

    #connect to database
    conn = sqlite3.connect("user.db")
    
    sql = ''' DELETE FROM users
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()    


     
    return render_template('delete.html')
    
@app.route('/delete-all')
def delete_all_users():   

    #connect to database
    conn = sqlite3.connect("user.db")
    
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM users'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    
    return render_template('delete_all.html')
    
@app.route('/create', methods=['GET', 'POST'])
def create_single_user():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        form_data = request.form
        print(form_data)
    
        uploaded_file = request.files['file']
        uploaded_file.save(os.path.join('./uploads',uploaded_file.filename))    
        
        user = (form_data["first_name"], form_data["last_name"], form_data["phone"
        ], uploaded_file.filename);
    
        conn = sqlite3.connect("user.db")
        sql = ''' INSERT INTO users (first_name, last_name, phone_number, user_image)
              VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user)
        conn.commit()
    
    
        return redirect(request.url)
    return render_template('create.html')
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_single_user(id):
    if request.method == 'POST':  #this block is only entered when the form is submitted
        #get all the posted form data
        form_data = request.form
        #print(form_data)
    
        #get the user profile image
        uploaded_file = request.files['file']
        #Save the user profile image into the uploads folder
        uploaded_file.save(os.path.join('./uploads',uploaded_file.filename))    
        
        #Construct a tuple with the user first_name, last_name, phone, and the profile image name
        user = (form_data["first_name"], form_data["last_name"], form_data["phone"
        ], uploaded_file.filename, id);
    
        
        #save the tuple data from above into the database
        conn = sqlite3.connect("user.db")
       
        
    
        sql = ''' UPDATE users 
             SET first_name = ? ,
                  last_name = ? ,
                  phone_number = ? ,
                  user_image = ?
              WHERE id = ?'''
                  
        cur = conn.cursor()
        cur.execute(sql, user)
        
        conn.commit()    


    
        return redirect('/users')
    return render_template('update.html', user_id=id)
    
    
#without these we cant view images
@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory('uploads', filename)


