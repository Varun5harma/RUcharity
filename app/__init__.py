from flask import Flask
import mysql.connector
from flask import request
from flask import render_template, json
from decimal import *

#importing Flask (class that holds the entire app)


app = Flask(__name__)
from app import views

global connection
connection = mysql.connector.connect(user='kc650', password='rucharity',
                              host='rutgerscharity.cjsliricy0ds.us-east-1.rds.amazonaws.com',
                              database='MainCharityDB')

global cursor;
cursor = connection.cursor()

operation = 'SELECT count(name) from Givers'
for result in cursor.execute(operation, multi=True):
  if result.with_rows:
    print("Rows produced by statement")
    print(result.fetchall())
  else:
    print("Number of rows affected by statement '{}': {}".format(
      result.statement, result.rowcount))


cursor.execute(operation)

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

@app.route('/signUp', methods=["GET"])
def signUp():
    global connection
    connection = mysql.connector.connect(user='kc650', password='rucharity',
                                  host='rutgerscharity.cjsliricy0ds.us-east-1.rds.amazonaws.com',
                                  database='MainCharityDB')
    global cursor;
    cursor = connection.cursor()
    ruid = request.args.get("recieverRUID")

    if(ruid):
        operation = "select Swipes_Recieved from Recievers where ruid = {0}".format(ruid)
#    for result in cursor.execute(operation, multi=True):
#        if result.with_rows:
#            print("Rows produced by statement!!!")
#            print "this is the result:", (result.fetchall())
#        else:
#                print("Number of rows affected by statement '{}': {}".format(
#                        result.statement, result.rowcount))


        cursor.execute(operation)
        result = cursor.fetchall()
        connection.commit()
        return json.dumps(result)

    campus = request.args.get("CommuterCheck")
    if(campus):
            operation = "select count(*) from Recievers where Commuter =  '{0}'".format(campus)
            cursor.execute(operation)
            result = cursor.fetchall()
            connection.commit()
            return json.dumps(result)


    major_swipe = request.args.get("MajorSwipe")
    if(major_swipe):
            operation = "select avg(swipes_left) from Givers where Majors =  '{0}'".format(major_swipe)
            cursor.execute(operation)
            result = cursor.fetchall()
            connection.commit()

            return json.dumps(str(result))

    #read values of Giving Form
    _name = request.args.get("UserName")
    print 'This is the name', _name
    _RUID = request.args.get("RUID")
    _MEALPLAN = request.args.get("MealPlan")
    _SwipesLeft = request.args.get("SwipesLeft")
    _MAJOR = request.args.get("Major")
    _CAMPUS = request.args.get("Campus")

    #read values for Recieveing form
    _Rname = request.args.get("rUserName")
    _rRUID = request.args.get("r_RUID")
    _ANNUALINCOME = request.args.get("AnnualIncome")
    _SWIPESRECIEVED = 0
    _COMMUTER = request.args.get("Commuter")
    _MAJOR = request.args.get("r_Major")

    if(_name):
        query_giver = """INSERT INTO Givers (Name,RUID,MEALPLAN,SWIPES_Left,MAJORS,CAMPUS)
                VALUES (%s,%s,%s,%s,%s,%s); """
        cursor.execute(query_giver, (_name, _RUID, _MEALPLAN, _SwipesLeft, _MAJOR, _CAMPUS))
        connection.commit()

    if(_Rname):
        query_reciever = """INSERT INTO Recievers (Name,RUID,Annual_Income,Swipes_Recieved,Commuter,Major)
                VALUES (%s,%s,%s,%s,%s,%s); """
        cursor.execute(query_reciever, (_Rname, _rRUID, _ANNUALINCOME, _SWIPESRECIEVED, _COMMUTER, _MAJOR))
        connection.commit()


    return render_template("index.html")


print ("Command executed!");
