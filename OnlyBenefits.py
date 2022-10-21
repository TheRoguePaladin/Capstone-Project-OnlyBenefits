import pymysql

hostname = 'localhost'
username = 'root'
password = ''
database = 'innovatech'

myConnection = pymysql.connect(hostname,username,password,database)

def login(conn):
    cursor = conn.cursor()
    sql = """SELECT EXISTS(SELECT * FROM student WHERE Email = sEmail AND Password = sPassword)"""
    #sql == 1 ---> FOUND
    if (sql==1):
        print("Do something about Logging in student")
    else if (sql == 0):
        print("Do something about Logging in admin")
    

def signup(conn,sName, sSurname,sEmail,sPassword):
    cursor = conn.cursor()
    sql = """INSERT INTO admin """
    if (sEmail.endswith("@myuwc.ac.za")== True):
        sql = """INSERT INTO student (Email, Password, Name, Surname, CurrentBenefits, CurrentPoints) VALUES (%s,%s,%s,%s,%s)"""
        val = (sEmail, sPassword, sName, sSurname,null, 150)
        cursor.execute(sql,val)
        conn.commit()
    else if (sEmail.endswith("uwc.ac.za")== True):
        sql = """INSERT INTO admin (Email, Password, Name, Surname) VALUES (%s,%s,%s,%s)"""
        val = (sEmail, sPassword, sName, sSurname)
        cursor.execute(sql,val)
        conn.commit()


        
        
