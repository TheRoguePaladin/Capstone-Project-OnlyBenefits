from __future__ import print_function
from re import U
import mysql.connector
import sys
from flask import Flask, render_template, request, jsonify, json
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Innovatech'

db=mysql.connector.connect(
host="localhost",
  user="root",
  passwd="",
  database="Innovatech" # Only used if DATABASE is created already.
)
mysql = MySQL(app)

mycursor = db.cursor(buffered=True)

@app.route('/signup.html', methods=['POST', 'GET'])
def signup():
    return render_template('signup.html')


@app.route('/signUpSave', methods=['POST', 'GET'])
def insertUser():
  if request.method == "POST":
    userData = request.get_json()
    print(userData)
    userDetails = json.dumps(userData)
    print(userDetails)
    userDetailsToInsert = eval(userDetails)
    StudentNum = userDetailsToInsert["StudentNum"]
    StudentName = userDetailsToInsert["StudentName"]
    StudentEmail = userDetailsToInsert["Email"]
    StudentPass = userDetailsToInsert["Password"]
    Script="INSERT INTO Student(StudentNum,Name,Email,Password) VALUES ('"+StudentNum+"','"+StudentName+"','"+StudentEmail+"','"+StudentPass+"')"
    mycursor.execute(Script)
    db.commit()
    results = {'processed': 'true'}
    return jsonify(results)

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/loginCheck', methods=['POST', 'GET'])
def CheckUser():
  if request.method == "POST":
    userData = request.get_json()
    print(userData)
    userDetails = json.dumps(userData)
    print(userDetails)
    userDetailsToInsert = eval(userDetails)
    StudentNum = userDetailsToInsert["StudentNum"]
    StudentPass = userDetailsToInsert["Password"]
    Script="SELECT StudentNum,Password from Student"
    mycursor.execute(Script)
    students = mycursor.fetchall()
    if StudentNum and StudentPass in students:
        results = {'processed': 'true'}
        return jsonify(results)
    else:
        results = {'processed': 'false'}
        return jsonify(results)

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/editProfile.html')
def editProfile():
    return render_template('editProfile.html')

@app.route('/editadminprofile.html')
def editadminprofile():
    return render_template('editadminprofile.html')

@app.route('/availEB.html')
def availEB():
    return render_template('availEB.html')

@app.route('/loadEvents', methods=['POST', 'GET'])
def loadEvents():
    Script="SELECT * from Event"
    mycursor.execute(Script)
    row_headers=[x[0] for x in mycursor.description]
    events = mycursor.fetchall()
    json_data=[]
    for result in events:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/loadBenefits', methods=['POST', 'GET'])
def loadBenefits():
    Script="SELECT * from Benefits"
    mycursor.execute(Script)
    row_headers=[x[0] for x in mycursor.description]
    benefits = mycursor.fetchall()
    json_data=[]
    for result in benefits:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/registerEvent', methods=['POST', 'GET'])
def AddPoints():
  if request.method == "POST":
    userData = request.get_json()
    print(userData)
    userDetails = json.dumps(userData)
    print(userDetails)
    userDetailsToInsert = eval(userDetails)
    StudentNum = userDetailsToInsert["StudentNum"]
    EventID = userDetailsToInsert["EventID"]
    EventPoints = userDetailsToInsert["EventPoints"]
    Script="INSERT INTO EventAttendees(StudentNumber,EventNumber) VALUES ('"+StudentNum+"','"+EventID+"')"
    mycursor.execute(Script)
    Script="UPDATE Student set CurrentPoints =CurrentPoints+"+EventPoints+" where StudentNum="+StudentNum
    mycursor.execute(Script)
    db.commit()
    results = {'processed': 'true'}
    return jsonify(results)

@app.route('/redeemBenefits', methods=['POST', 'GET'])
def RedeemBenefit():
  if request.method == "POST":
    userData = request.get_json()
    print(userData)
    userDetails = json.dumps(userData)
    print(userDetails)
    userDetailsToInsert = eval(userDetails)
    StudentNum = userDetailsToInsert["StudentNum"]
    BenefitCode = userDetailsToInsert["BCode"]
    BenefitPoints = userDetailsToInsert["BPoints"]
    Script="UPDATE Student set CurrentPoints =CurrentPoints-'"+BenefitPoints+"',CurrentBenefits='"+BenefitCode+"' where StudentNum="+StudentNum
    mycursor.execute(Script)
    db.commit()
    results = {'processed': 'true'}
    return jsonify(results)

@app.route('/adminProfile.html')
def adminProfile():
    return render_template('adminProfile.html')

@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

app.run(host='localhost', port=5000)
