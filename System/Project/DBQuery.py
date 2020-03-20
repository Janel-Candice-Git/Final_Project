import sqlite3 as SQL



#Function for creating connection for the Database
def get_connection(db_path):
    #Initializing connection variable
    db_connection = None
    try:
        db_connection = SQL.connect(db_path)
    except SQL.Error as e:
        print("Error in connecting to Database!", e)
    return db_connection


#Function for creating path directory for Database (location of sql file)
def get_db_path():
    dbpath = "C:/Users/admins/Desktop/Sideline/Sideline/Database/Project.db" #Change this according to current path
    return dbpath


#Retrieves ALL data in Database linked to current account
def get_all_data (username):
    dbpath = get_db_path()
    dbconnection = get_connection(dbpath)
    cursor = dbconnection.cursor()
    cursor.execute("SELECT id_counter, tim_starttime, tim_endtime, dat_startdate, dat_enddate, var_place, var_desc FROM event_plan WHERE var_userid = ?", 
    [username])
    result = cursor.fetchall()
    cursor.close()
    return result


#Search Database based on time, date, place and description (this are not case sensitive)
def get_search_data (username, datacounter):
    dbpath = get_db_path()
    dbconnection = get_connection(dbpath)
    cursor = dbconnection.cursor()
    cursor.execute("SELECT id_counter, tim_starttime, tim_endtime, dat_startdate, dat_enddate, var_place, var_desc FROM event_plan WHERE (id_counter = ? AND var_userid = ?)", 
    (datacounter, username))
    result = cursor.fetchall()
    cursor.close()
    return result


#Funtion for simple login check or verifying the account in the Login
def verification_check(username, password): 
    dbpath = get_db_path()
    dbconnection = get_connection(dbpath)
    cursor = dbconnection.cursor()
    cursor.execute("SELECT var_userid, var_password FROM registration_data WHERE var_userid = ? AND var_password = ? ", 
    (username, password))
    result = cursor.fetchone()
    cursor.close()
    dbconnection.close()
    return result


#Function for SQL Query to insert values/information in Registration Frame
#Adds user to registration database
def insert_user_data(username, name, password, email):
    dbpath = get_db_path()
    dbconnection = get_connection(dbpath)
    cursor = dbconnection.cursor()
    cursor.execute("INSERT INTO registration_data (var_userid, var_name, var_password, var_email) VALUES (?, ?, ?, ?)",
                       (username, name, password, email))
    dbconnection.commit()
    print("inserting registration data complete.")
    cursor.close()
    dbconnection.close()
    
    

#Function for SQL Query to insert values/information in Set Event Frame    
def insert_set_event(username, starttime, endtime, startdate, enddate, place, description): #Adds event planned linked to username via foreign key
    dbpath = get_db_path()
    dbconnection = get_connection(dbpath)
    cursor = dbconnection.cursor()
    cursor.execute("INSERT into event_plan (var_userid, tim_starttime, tim_endtime, dat_startdate, dat_enddate, var_place, var_desc) VALUES ((SELECT var_userid FROM registration_data WHERE var_userid = ?), ?, ?, ?, ?, ?, ?)",
        (username, starttime, endtime, startdate, enddate, place, description))
    dbconnection.commit() 
    print("Insert Complete!")
    cursor.close()
    dbconnection.close()


#Function for SQL Query to Update Values in the Table
def update_set_event(starttime, endtime, startdate, enddate, place, description): #allows for editing event plans
    dbpath = get_db_path()
    dbconnection = get_connection(dbpath)
    cursor = dbconnection.cursor()
    cursor.execute("UPDATE event_plan SET tim_starttime = ?, tim_endtime = ?, tim_startdate = ?, tim_enddate = ?, var_place = ?, var_desc = ? WHERE  var_userid = ?",
        (starttime, endtime, startdate, enddate, place, description)) 
    dbconnection.commit() #remove "#" if insert query doesnt save to database ONLY.
    print("updating event plan complete.")
    cursor.close()
    dbconnection.close()


#Function for SQL Query to Delete Values in the Table
def delete_set_event(id_counter, starttime, endtime, startdate, enddate, place, description): #deletes 1 event plan
    dbpath = get_db_path()
    dbconnection = get_connection(dbpath)
    cursor = dbconnection.cursor()
    cursor.execute("DELETE FROM event_plan WHERE (var_userid = ? AND tim_starttime = ? AND tim_endtime = ? AND dat_startdate = ? AND dat_enddate = ? AND var_place = ? AND var_desc = ? AND id_counter =?)",
        (starttime, endtime, startdate, enddate, place, description, id_counter)) 
    dbconnection.commit() #remove "#" if insert query doesnt delete to database ONLY.
    print("deleting event plan complete.")
    cursor.close()
    dbconnection.close()
    
if __name__ == "__main__":
    get_all_data("admin")