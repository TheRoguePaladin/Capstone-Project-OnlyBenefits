import mysql.connector
import sys
db=mysql.connector.connect(
host="localhost",
  user="root",
  passwd="",
  database="Innovatech" # Only used if DATABASE is created already.
)


mycursor = db.cursor(buffered=True)

STUDENTNUMBER="123456"

def Password(User,Pass):

    Script= "SELECT Password FROM Student WHERE StudentNum = "+User
    mycursor.execute(Script)
    C=mycursor.fetchall()
    if(C[0][0] ==Pass):
        Scr= "SELECT Name FROM Student WHERE StudentNum = "+User
        mycursor.execute(Scr)
        D=mycursor.fetchall()
        D=D[0][0]
        print("Welcome to Only Benefits "+ D)
        STUDENTNUMBER=User
        return 1
    else:
        return 0

def AdminPassword():
    User=input("Enter Your Email ")
    Pass=input("Password ")
    Script= "SELECT Password FROM Admin WHERE Email = "+User
    mycursor.execute(Script)
    C=mycursor.fetchall()
    if(C[0][0] ==Pass):
        Scr= "SELECT Name FROM Admin WHERE Email = "+User
        mycursor.execute(Scr)
        D=mycursor.fetchall()
        D=D[0][0]
        print("Welcome to Only Benefits "+ D)
        STUDENTNUMBER=User
        return 1
    else:
        return 0

def Redeem(Code):
    A="'"+Code+"'"
    Script1="SELECT Cost FROM Benefits WHERE BenefitCode ="+A
    Script2="SELECT CurrentPoints, CurrentBenefits FROM Student WHERE StudentNum=" + STUDENTNUMBER
    mycursor.execute(Script1)
    C=mycursor.fetchall()
    Price=int(C[0][0])
    print("Price is "+str(Price))
    mycursor.execute(Script2)
    C=mycursor.fetchall()
    Points=C[0][0]
    Benefits=C[0][1]
    print("Points is "+str(Points))
    print("Benefits is "+str(Benefits))
    if(Points>=Price):
        Points=Points-Price

        Script="UPDATE Student SET CurrentPoints="+ str(Points)+ " WHERE StudentNum=" + STUDENTNUMBER
        mycursor.execute(Script)
        if Benefits==None:
            Benefits="'"+Code+"'"
            print(Benefits)
        else:
            Benefits="'"+Benefits+","+Code+"'"
            print(Benefits)

        Script="UPDATE Student SET CurrentBenefits="+Benefits +" WHERE StudentNum=" + STUDENTNUMBER
        mycursor.execute(Script)

        db.commit()


def SignUP(StudentName,StudentEmail, Password):

    Script="INSERT INTO Student(Name,Email,Password) VALUES ('"+StudentName+"','"+StudentEmail+"','"+Password+"')"
    mycursor.execute(Script)

    db.commit()

def AddEvent(Code,Description,Cost):


    Script="INSERT INTO Event(EventID,EventName,PointsReward) VALUES ('"+Code+"','"+Description+"','"+Cost+"')"
    mycursor.execute(Script)

    db.commit()
def AddBenefits(Code,Description,Cost):


    Script="INSERT INTO Benefits(BenefitCode,BenefitDescription,Cost) VALUES ('"+Code+"','"+Description+"','"+Cost+"')"
    mycursor.execute(Script)

    db.commit()


def RemoveEvent(A):
    Script="DELETE FROM Event WHERE EventID=" + A
    mycursor.execute(Script)

    db.commit()
def Benefit(A):
    Script="DELETE FROM Benefit WHERE BenefitCode=" + A
    mycursor.execute(Script)

    db.commit()

def EditPass(A):
    if(STUDENTNUMBER.indexof()!=-1):
        Script="UPDATE Student SET VALUES Password = "+ A +"WHERE StudentNum = "+STUDENTNUMBER
    else:
        Script="UPDATE Admin SET VALUES Password = "+ A +"WHERE EmailAdrress = "+STUDENTNUMBER
    mycursor.execute(Script)

    db.commit()
while True:
    PP= input("1 for login \n2 for Redeem points \n3 for Sign-up an account \n4 for admin login \n5 Add Benefits \n6 Add Events \n7 Remove Event \n8 Remove Benefit \n9 Edit Password ")
    if PP =="1":

        a=input("StudentNumber ")
        b=input("Password ")
        Password(a,b)

    if PP =="2":

        Code = input("Please enter your Benefits Code:")
        Redeem(Code)

    if PP =="3":

        a=input("Please enter your Student Number")
        b=input("Please enter your Student Name")
        c=input("Please enter your EmailAdrress")
        SignUp(a,b,c)

    if PP =="4":
        AdminPassword()
    if PP =="5":
        a=input("Please enter the unique Code of the new benefit ")
        b=input("Please enter a short Description of the benefit ")
        c=input("Please enter the desired cost ")
        AddBenefits(a,b,c)
    if PP =="6":
        a=input("Please enter the unique Code of the Event")
        b=input("Please enter a short Description of the event")
        c=input("Please enter the desired reward")
        AddEvent(a,b,c)

    if PP =="7":
        Code=input("Please enter the unique Code of the Event")
        RemoveEvent(Code)
    if PP =="8":
        Code=input("Please enter the unique Code of the Benefit")
        RemoveBenefit(Code)
    if PP=="9":
        New=input("Please enter your new password")
        EditPass(New)


db.commit()
