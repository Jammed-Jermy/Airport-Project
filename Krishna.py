#ProjectKrishnaHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHA



#NECESSARY MODULES--#NECESSARY MODULES--#NECESSARY MODULES--#NECESSARY MODULES--#NECESSARY MODULES--#NECESSARY MODULES--#NECESSARY MODULES--#NECESSARY MODULES--#NECESSARY MODULES--#NECESSARY MODULES--


import random 
import sys
import time
import math
import ctypes
import webbrowser
import datetime





#NECESSARY FUNCTIONS--#NECESSARY FUNCTIONS--#NECESSARY FUNCTIONS--#NECESSARY FUNCTIONS--#NECESSARY FUNCTIONS--#NECESSARY FUNCTIONS--#NECESSARY FUNCTIONS--#NECESSARY FUNCTIONS--#NECESSARY FUNCTIONS--#NECESSARY FUNCTIONS--


def typer2(text,end=''):
    for x in text:
        print(x, end='', flush=True)  
        time.sleep(0.1) 
    print() 
def typer(text):
    for x in text:
        print(x, end='', flush=True)  
        time.sleep(0.01) 
    print() 
def redirection():
    webbrowser.open("https://dev.mysql.com/downloads/mysql/")
def guided():
    print("Guidation download begining")
    time.sleep(1)
    typer2("Step 0: Install MySQL Server")
    time.sleep(1)
    typer2("Step 1: Follow the installation instructions provided by the MySQL installer.")
    time.sleep(2)
    typer2("Step 2: Please click the box which puts the MySQL in environment root directory")
    time.sleep(2)
    typer2("Step 3: During the installation process, you will be prompted to set a root password for the MySQL server. Make sure to remember this password, as you will need it later.")
    time.sleep(3)
    typer2("Step 4: Open a command prompt")
    time.sleep(1)
    typer2("Step 5: Install the MySQL Connector package using pip (Python's package manager) by running the following command")
    print("pip install mysql-connector-python")
    time.sleep(8)
    typer2("Redirecting you towards the download")
    time.sleep(1)
    redirection()
import mysql.connector as ms
import pandas as pd
try: 
    con = ms.connect(host="localhost", user="root", password="hello123", database="airport")
except Exception as e:
    ask4=input("Do you have MYSQL installed?: ")
    if ask4.upper()=="YES" or ask4.upper()=="Y":
        ask=input("Have you created a mysql database named 'airport': ")
        if ask.upper()=='YES' or ask.upper()=='Y':
            pw=input("Enter mysql password:")
            try: 
                con = ms.connect(host="localhost", user="root", password=pw, database="airport")
                print("Connected!")
            except Exception as f:
                db=input("Enter database name:")
                try: 
                    con = ms.connect(host="localhost", user="root", password=pw, database=db)
                    print("Connected!")
                except Exception as f:
                    host=input("Enter host name (By default host= localhost):")
                    try: 
                        con = ms.connect(host=host, user="root", password=pw, database=db)
                        print("Connected!")
                    except Exception as f:
                        user=input("Enter user name (By default user= root):")
                        try: 
                            con = ms.connect(host=host, user=user, password=pw, database=db)
                            print("Connected!")
                        except Exception as f:
                            print(f)
                            sys.exit()
        else:
            print("Please create a mysql database before entering this program \nYou can create a mysql database using this querry= 'Create database airport;")
            sys.exit()
    else:
        print("\t\t---------------------------------")
        print("\t\t| 1. Guided Download            |")
        print("\t\t| 2. Manual Download            |")
        print("\t\t---------------------------------")
        resp=input("Enter response: ")
        if resp.upper()=="1":
                guided()
                exit()
        else:
            print("Please download mysql manually")
            exit()
cursor=con.cursor()





#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--
masterpass=321
#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--#PASSWORD--







#CODE FUNCTIONS--#CODE FUNCTIONS--#CODE FUNCTIONS--#CODE FUNCTIONS--#CODE FUNCTIONS--#CODE FUNCTIONS--#CODE FUNCTIONS--#CODE FUNCTIONS--#CODE FUNCTIONS--#CODE FUNCTIONS--#CODE FUNC


def rerun():                                                          #working properly (test 4 conductedd)
    query="Insert ignore into test values(1);"
    cursor.execute(query)
    con.commit()

def no_rerun():  #working properly (test 4 conductedd)
    query="Select * from test;"
    cursor.execute(query)
    resulta=cursor.fetchone()
    if resulta is not None:
        return resulta[0]
    else:
        return 0  


def menu ():                 #working properly (test 4 conductedd)
    typer( "\n\n\n\n"+"*"*70+"Welcome to Flight Booking System"+ "*"*297)
    time.sleep(1)
    typer("\t\t---------------------------------")
    typer("\t\t| 1. Book Flight                |")
    typer("\t\t| 2. Check Existing Tickets     |")
    typer("\t\t| 3. Make changes in details    |")
    typer("\t\t| 4. Continue Payment?          |")
    typer("\t\t| 5. Exit                       |")
    typer("\t\t---------------------------------")

def menu_2 ():                 #working properly (test 4 conductedd)
    print( "\n\n\n\n","*"*60,"Welcome to Flight Booking System", "*"*196)
    time.sleep(1)
    print("\t\t---------------------------------")
    print("\t\t| 1. Book Flight                |")
    print("\t\t| 2. Check Existing Tickets     |")
    print("\t\t| 3. Make changes in details    |")
    print("\t\t| 4. Continue Payment?          |")
    print("\t\t| 5. Exit                       |")
    print("\t\t---------------------------------")

def introduction():
    text = '''                 Project submitted by KRISHNA VOHRA of class 12TH 
                                        __|__            
                                --------(_)--------     
                                    O  O       O  O 
                            PROJECT ON AIRPORT BOOKING SYSTEM'''

    for x in text:
        print(x, end='', flush=True)
        if x == ' ':
            time.sleep(0.0001)  
        else:
            time.sleep(0.08)  
    print()
    


def get_upcoming_dates():
    current_date = datetime.date.today()
    upcoming_dates = []

    for i in range(75):
        date = current_date + datetime.timedelta(days=random.randint(0, 6))
        upcoming_dates.append(date)

    return upcoming_dates

def table():                                                      #working properly (test 4 conductedd)
    introduction()
    time.sleep(3)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    typer2("Running The Program.")
    time.sleep(1)
    typer2("Running The Program..")
    time.sleep(1)
    typer2("Running The Program...")
    time.sleep(1)
    print("Loading Tips.", end=" ")
    time.sleep(1)
    print("Loading Tips..", end=" ")
    time.sleep(1)
    print("Loading Tips...",end=" ")
    time.sleep(1)
    print("-Make sure you have Mysql")
    time.sleep(2)
    print("-If you face any errors, Make sure you have created a database named 'airport'")
    time.sleep(3)
    print("-The rest will be created by the code")
    time.sleep(2)
    print("-This is a one time process, it won't happen if you rerun the code")
    z=0
    try:
        dates = get_upcoming_dates()
        formatted_dates = [date.strftime('%Y-%m-%d') for date in dates]
        cursor.execute("CREATE TABLE IF NOT EXISTS customer (Passenger INT NOT NULL PRIMARY KEY,Fname VARCHAR(15) NOT NULL,Lname VARCHAR(15) NOT NULL,Phone CHAR(10) NOT NULL,Meal VARCHAR(10),Pid INT,Pw VARCHAR(20) NOT NULL);")
        cursor.execute("CREATE TABLE IF NOT EXISTS payment_info (Card INT NOT NULL PRIMARY KEY, Price INT NOT NULL, Passenger INT, CVV INT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS airlines (Pid INT NOT NULL PRIMARY KEY,Airlines VARCHAR(30) NOT NULL,Arrival VARCHAR(20) NOT NULL,Departure VARCHAR(20) NOT NULL,TOD VARCHAR(10) NOT NULL, Date VARCHAR(15),Ticket INT NOT NULL,RT VARCHAR(3) NOT NULL);")
        cursor.execute('''INSERT IGNORE INTO airlines
        VALUES
        (68, 'Vistara', 'Goa', 'Delhi', '5:30', '{}', 6000, 'no'),
        (69, 'Flydubai', 'Delhi', 'Mumbai', '12:00', '{}', 8000, 'yes'),
        (70, 'Vistara', 'Mumbai', 'Goa', '18:00', '{}', 5000, 'no'),
        (71, 'IndiGo', 'Delhi', 'Goa', '21:45', '{}', 7000, 'yes'),
        (72, 'Flydubai', 'Mumbai', 'Delhi', '5:30', '{}', 6000, 'yes'),
        (73, 'Vistara', 'Goa', 'Mumbai', '12:00', '{}', 9000, 'no'),
        (74, 'IndiGo', 'Delhi', 'Goa', '18:00', '{}', 4000, 'yes'),
        (75, 'Flydubai', 'Mumbai', 'Goa', '21:45', '{}', 11000, 'no'),
        (76, 'Vistara', 'Delhi', 'Goa', '5:30', '{}', 7500, 'yes'),
        (77, 'IndiGo', 'Mumbai', 'Goa', '12:00', '{}', 8500, 'yes'),
        (78, 'Flydubai', 'Pune', 'Mumbai', '18:00', '{}', 7000, 'no'),
        (79, 'Vistara', 'Pune', 'Delhi', '21:45', '{}', 9000, 'yes'),
        (80, 'IndiGo', 'Mumbai', 'Pune', '5:30', '{}', 6000, 'no'),
        (81, 'Flydubai', 'Pune', 'Mumbai', '12:00', '{}', 6500, 'yes'),
        (82, 'Vistara', 'Delhi', 'Goa', '18:00', '{}', 7500, 'yes'),
        (83, 'IndiGo', 'Goa', 'Delhi', '21:45', '{}', 7000, 'no'),
        (84, 'Flydubai', 'Pune', 'Delhi', '5:30', '{}', 8000, 'no'),
        (85, 'Vistara', 'Mumbai', 'Goa', '12:00', '{}', 6000, 'yes'),
        (86, 'IndiGo', 'Delhi', 'Mumbai', '18:00', '{}', 7500, 'yes'),
        (87, 'Flydubai', 'Goa', 'Mumbai', '21:45', '{}', 9000, 'no'),
        (88, 'Vistara', 'Delhi', 'Goa', '5:30', '{}', 7000, 'yes'),
        (89, 'IndiGo', 'Mumbai', 'Goa', '12:00', '{}', 5500, 'no'),
        (90, 'Flydubai', 'Pune', 'Mumbai', '18:00', '{}', 6500, 'yes'),
        (91, 'Vistara', 'Pune', 'Delhi', '21:45', '{}', 7500, 'yes'),
        (92, 'IndiGo', 'Mumbai', 'Pune', '5:30', '{}', 7000, 'no'),
        (93, 'Flydubai', 'Pune', 'Mumbai', '12:00', '{}', 8000, 'no'),
        (94, 'Vistara', 'Delhi', 'Goa', '18:00', '{}', 6000, 'yes'),
        (95, 'IndiGo', 'Goa', 'Delhi', '21:45', '{}', 7000, 'yes'),
        (96, 'Flydubai', 'Pune', 'Delhi', '5:30', '{}', 5500, 'no'),
        (97, 'Vistara', 'Mumbai', 'Goa', '12:00', '{}', 8500, 'yes'),
        (98, 'IndiGo', 'Delhi', 'Mumbai', '18:00', '{}', 7500, 'no'),
        (99, 'Flydubai', 'Goa', 'Mumbai', '21:45', '{}', 9000, 'yes'),
        (100, 'Vistara', 'Delhi', 'Goa', '5:30', '{}', 7000, 'yes'),
        (101, 'IndiGo', 'Mumbai', 'Goa', '12:00', '{}', 5500, 'no'),
        (102, 'Flydubai', 'Pune', 'Mumbai', '18:00', '{}', 6500, 'no'),
        (103, 'Vistara', 'Pune', 'Delhi', '21:45', '{}', 7500, 'yes'),
        (104, 'IndiGo', 'Mumbai', 'Pune', '5:30', '{}', 7000, 'yes'),
        (105, 'Flydubai', 'Pune', 'Mumbai', '12:00', '{}', 8000, 'no'),
        (106, 'IndiGo', 'Goa', 'Delhi', '21:45', '{}', 7000, 'yes'),
        (107, 'Flydubai', 'Pune', 'Delhi', '5:30', '{}', 5500, 'no'),
        (108, 'Vistara', 'Mumbai', 'Goa', '12:00', '{}', 8500, 'yes'),
        (109, 'IndiGo', 'Delhi', 'Mumbai', '18:00', '{}', 7500, 'no'),
        (110, 'Flydubai', 'Goa', 'Mumbai', '21:45', '{}', 9000, 'yes'),
        (111, 'Vistara', 'Mumbai', 'Delhi', '5:30', '{}', 8000, 'no'),
        (112, 'IndiGo', 'Delhi', 'Mumbai', '12:00', '{}', 7500, 'yes'),
        (113, 'Flydubai', 'Goa', 'Delhi', '18:00', '{}', 6000, 'yes'),
        (114, 'Vistara', 'Delhi', 'Goa', '21:45', '{}', 7000, 'no'),
        (115, 'IndiGo', 'Pune', 'Mumbai', '5:30', '{}', 6500, 'no'),
        (116, 'Flydubai', 'Mumbai', 'Pune', '12:00', '{}', 7000, 'yes'),
        (117, 'Vistara', 'Goa', 'Mumbai', '18:00', '{}', 5500, 'yes'),
        (118, 'IndiGo', 'Mumbai', 'Goa', '21:45', '{}', 7500, 'no'),
        (119, 'Flydubai', 'Delhi', 'Goa', '5:30', '{}', 8000, 'no'),
        (120, 'Vistara', 'Goa', 'Delhi', '12:00', '{}', 6000, 'yes'),
        (121, 'IndiGo', 'Pune', 'Mumbai', '18:00', '{}', 7000, 'no'),
        (122, 'Flydubai', 'Mumbai', 'Pune', '21:45', '{}', 5500, 'no'),
        (123, 'IndiGo', 'Delhi', 'Goa', '5:30', '{}', 7000, 'yes'),
        (124, 'Flydubai', 'Goa', 'Delhi', '12:00', '{}', 8000, 'yes'),
        (125, 'Vistara', 'Mumbai', 'Goa', '18:00', '{}', 5500, 'no'),
        (126, 'IndiGo', 'Goa', 'Mumbai', '21:45', '{}', 7500, 'no'),
        (127, 'Flydubai', 'Delhi', 'Mumbai', '5:30', '{}', 6500, 'no'),
        (128, 'Vistara', 'Mumbai', 'Goa', '12:00', '{}', 6000, 'yes'),
        (129, 'IndiGo', 'Pune', 'Goa', '18:00', '{}', 7000, 'yes'),
        (130, 'IndiGo', 'Goa', 'Delhi', '12:00', '{}', 6000, 'yes'),
        (131, 'Flydubai', 'Delhi', 'Goa', '18:00', '{}', 7000, 'yes'),
        (132, 'Vistara', 'Mumbai', 'Goa', '21:45', '{}', 5500, 'no'),
        (133, 'IndiGo', 'Goa', 'Mumbai', '5:30', '{}', 7500, 'no'),
        (134, 'Flydubai', 'Delhi', 'Mumbai', '12:00', '{}', 6500, 'no'),
        (135, 'Vistara', 'Mumbai', 'Delhi', '18:00', '{}', 8000, 'no'),
        (136, 'IndiGo', 'Pune', 'Mumbai', '21:45', '{}', 7000, 'yes'),
        (137, 'Flydubai', 'Mumbai', 'Pune', '5:30', '{}', 5500, 'yes'),
        (138, 'Vistara', 'Goa', 'Mumbai', '12:00', '{}', 7500, 'no'),
        (139, 'IndiGo', 'Mumbai', 'Goa', '18:00', '{}', 6000, 'no'),
        (140, 'Flydubai', 'Delhi', 'Goa', '21:45', '{}', 7000, 'yes'),
        (141, 'Vistara', 'Goa', 'Delhi', '5:30', '{}', 8000, 'yes'),
        (142, 'IndiGo', 'Delhi', 'Goa', '12:00', '{}', 5500, 'no');  
        '''.format(*formatted_dates))
        testables()                
        con.commit()
        time.sleep(3)
        print("Succesfully data created")
        time.sleep(1)
        typer2("Loading the program.")
        time.sleep(1)
        typer2("Loading the program..")
        time.sleep(1)
        typer2("Loading the program...")
        time.sleep(0.5)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    except Exception as e:
        print("Error while creating data for prerequists", e)
    return z

def ran_price():#working properly (test 4 conductedd)
    cursor.execute("SELECT Ticket FROM airlines WHERE pid = {}".format(plane_ids))
    row = cursor.fetchone()
    price=row[0] 
    price=int(price)
    x=random.uniform(-0.1, 0.2)
    new_price= price + price * x
    new_price=math.ceil(new_price)
    return int(new_price)






def save_payment_details():  #working properly (test 4 conductedd)             #checked
    try:
        x=0
        passenger__id = int(input("Enter passenger ID: "))
        print("Checking.")
        time.sleep(1)
        print("Checking..")
        time.sleep(1)
        print("Checking...")
        time.sleep(1)
        if passenger__id==passenger_id:
            cursor.execute("Select pid from customer where Passenger={}".format(passenger__id))
            pid=cursor.fetchall()
            pid=str(pid[0][0])
            cursor.execute("SELECT Ticket FROM airlines WHERE pid = {}".format(pid))
            row = cursor.fetchone()
            price=row[0]
            price=int(price)
            x=random.uniform(-0.1, 0.2)
            new_price= price + price * x
            new_price=math.ceil(new_price)
            print("Success!")
            credit_card_number = input("Enter credit card number: ")
            price=new_price
            print("Your final Price is: ","₹",price)
            user_ver = input("Do you want to continue to pay? (Y/N): ")
            try:
                if user_ver.upper() == "Y" or user_ver.upper() == "YES":
                    name=input("Enter your Full Name on Card: ")
                    expiry=input("Enter your Expiry Date on Card: ")
                    Cvv=input("Enter your CVV: ")
                    name=name
                    expiry=expiry
                    insert_query = "INSERT INTO payment_info values('{}','{}','{}','{}')".format(credit_card_number,new_price, passenger__id, Cvv)
                    cursor.execute(insert_query)
                    con.commit()
                    typer2("Sending the OTP.",end='\r')
                    time.sleep(0.4)
                    typer2("Sending the OTP..",end='\r')
                    time.sleep(0.4)
                    typer2("Sending the OTP...")
                    time.sleep(1)
                    typer2("Receiving the OTP.",end='\r')
                    time.sleep(0.4)
                    typer2("Receiving the OTP..",end='\r')
                    time.sleep(0.4)
                    typer2("Receiving the OTP...")
                    time.sleep(3)
                    print("Payment successfully!")
                    x=1
                else:
                    print("Payment cancelled.")
            except ValueError:
                print("Invalid input. Please enter 'Y' or 'N'.")
        else:
            print("Your passenger ID is INVALID")
    except Exception as e:
        print("Error occurred while saving payment details:", e)
    return x

def login():                                                  #working properly (test 4 conductedd)
    print("Please Enter the Plane id (Pid) you want to book","\n")
    try:
        pid = int(input("Response: "))
        time.sleep(1)
        print("Checking for flight availibility.")
        time.sleep(1)
        print("Checking for flight availibility..")
        time.sleep(1)
        print("Checking for flight availibility...")
        if pid in plane_ids:
            time.sleep(1)
            print("Available!")
            fname = input("Enter your First Name: ")
            lname = input("Enter your Last Name: ")
            fname=fname.title()
            lname=lname.title()
            test_digit="1234567890"
            while True:
                phone=input("Enter your phone number: ")
                if len(phone)==len(test_digit):
                    break
                else:
                    print("Please make sure the number is valid")
                    continue
            meal = input("Are you vegetarian (y/n): ")
            
            if meal.lower() == "y" or meal.lower() == "yes":
                meal = "Veg"
            elif meal.lower() == "n" or meal.lower() == "no":
                meal = "Non Veg"
            else:
                print("Option, INCORRECT, auto meal = VEG")
                meal="Veg"
            final = [pid, fname, lname, phone, meal]
            finalDf = pd.DataFrame(final)
            finalDf = finalDf.rename(index={0: 'Pid'})
            finalDf = finalDf.rename(index={1: 'Fname'})
            finalDf = finalDf.rename(index={2: 'Lname'})
            finalDf = finalDf.rename(index={3: 'Phone'})
            finalDf = finalDf.rename(index={4: 'Meal'})
            
            print("\n", finalDf, "\n", "This is Your Login information. Do you want To change anything? (Y/N)")
            response = input("RESPONSE: ")
            
            while True:
                if response.upper() == "Y" or response.upper() == "YES" :
                    print("\n", "Please tell us what you want to change", finalDf)
                    changes = input("Enter Row name: ")
                    
                    if changes == "Pid":
                        pid = int(input("Enter new Pid: "))
                    elif changes == "Fname":
                        fname = input("Enter new Fname: ")
                    elif changes == "Lname":
                        lname = input("Enter new Lname: ")
                    elif changes == "Phone":
                        phone = int(input("Enter new Phone: "))
                    elif changes == "Meal":
                        meal = input("Enter meal Veg or Non-Veg: ")
                    else:
                        print("error sherror aagya ji ye toh")
                        pass
                    print("Making the changes.")
                    time.sleep(1)
                    print("Making the changes..")
                    time.sleep(1)
                    print("Making the changes...")
                    time.sleep(1)
                    print("Changes have been made.")
                    break
                else:
                    break
            password = password_gen()
            password = str(password)
            fname=fname.lower().title()
            lname=lname.lower().title()
            phone = str(phone)
            fname = "'" + fname + "'"
            lname = "'" + lname + "'"
            phone = "'" + phone + "'"
            meal = "'" + meal + "'"
            password1 = "'" + password + "'"
            
            passenger_id = get_next_passenger_id()
            loginquery = "INSERT INTO customer VALUES ({}, {}, {}, {}, {}, {}, {})".format(
                passenger_id, fname, lname, phone, meal, pid, password1)
            try:
                cursor.execute(loginquery)
                con.commit()
            except Exception as e:
                print("Your data was not saved, an error occured",e)
                sys.exit()
            time.sleep(2)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYour Data is Saved")
            time.sleep(1)
            print("\nYour passenger id is:",passenger_id,)
            time.sleep(1)
            print("Your password is:",password)
            time.sleep(3)
            print("Please Remember These, These will help you retrive info late\n")
            time.sleep(1)
            #boardin_pass(passenger_id)
        else:
            time.sleep(1)
            print("The plane ID is not available, Exiting")
            sys.exit()
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for Pid or Phone Number.")

def password_gen():#working properly (test 4 conductedd)
    out1=random.randrange(1000,8831)
    out2=random.randrange(100,999)
    out3=random.randrange(0,100)
    out4=68
    masterpass=out1+out2+out3+out4
    return masterpass






def seat():      #working properly (test 4 conductedd)
    a=random.randrange(0,36)
    a=str(a)
    l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    b=random.randint(1,24)
    bethak=str(a+l[b])
    return bethak

def get_next_passenger_id():           #working properly (test 4 conductedd)
    query = "SELECT MAX(Passenger) FROM customer;"
    cursor.execute(query)
    result = cursor.fetchone()
    max_passenger_id = result[0]
    exception_grp=None
    if type(max_passenger_id)==type(exception_grp):
        next_passenger_id=1
    else:
        next_passenger_id = max_passenger_id + 1
    return next_passenger_id


def modify():#working properly (test 4 conductedd)
    print("Note- We can only update personal information")
    time.sleep(2)
    pw=input("Please enter your 4 digit password:")
    pass_id=int(input("Please enter your Passenger ID:"))
    checkquery=("select * from customer where Pw={} and Passenger={} ").format(pw,pass_id)
    cursor.execute(checkquery)
    checkquery_r = cursor.fetchone()
    test=None
    if type(checkquery_r)==type(test):
        time.sleep(1)
        print("Invalid details")
        sys.exit()
    else:
        pass
    try:
        print("This is your information\n",checkquery_r,"\nWhat do you want to change?")
        print("Enter what do you want to change","\n1.First name","\n2.Last name","\n3.Phone","\n4.Password","\n5.Exit: ")
        modific=int(input("RESPONSE: "))
        if modific==1:
            while True:
                Fname=input("Enter your First name")
                Fname2=input("Confirm your First Name")
                if Fname==Fname2:
                    name_query=("update customer set Fname='{}' where Passenger={};").format(Fname,pass_id)
                    cursor.execute(name_query)
                    con.commit()
                    if cursor.rowcount>0:
                        print("Changed Sucessfully")
                        sys.exit()
                    else:
                        print("Error occured, please try again")
                else:
                    print("Make sure both names are same")
                    break
        elif modific==2:
            while True:
                Lname=input("Enter your Last name")
                Lname2=input("Confirm your Last Name")
                if Lname==Lname2:
                    Lname_query=("update customer set Lname='{}' where Passenger={};").format(Lname,pass_id)
                    cursor.execute(Lname_query)
                    con.commit()
                    if cursor.rowcount>0:
                        print("Changed Sucessfully")
                        sys.exit()
                    else:
                        print("Error occured, please try again")
                else:
                    print("Make sure both names are same")
                    break
        elif modific==3:
            while True:
                Phone=input("Enter your Phone number")
                Phone2=input("Confirm your Phone number")
                if Phone==Phone2:
                    Phone_query=("update customer set Phone='{}' where Passenger={};").format(Phone,pass_id)
                    cursor.execute(Phone_query)
                    con.commit()
                    if cursor.rowcount>0:
                        print("Changed Sucessfully")
                        sys.exit()
                    else:
                        print("Error occured, please try again")
                else:
                    print("Make sure both Phone numbers are same")
                    break
        elif modific==4:
            while True:
                Password=input("Enter your Password")
                Password2=input("Confirm your Password")
                if Password==Password2:
                    pw_query=("update customer set Pw='{}' where Passenger={};").format(Password,pass_id)
                    cursor.execute(pw_query)
                    con.commit()
                    if cursor.rowcount>0:
                        print("Changed Sucessfully")
                        sys.exit()
                    else:
                        print("Error occured, please try again")
                else:
                    print("Make sure both Phone numbers are same")
                    break
        elif modific==5:
            print("Program Exited")
        else:
            print("Invalid Option, Program Exited")
    except AttributeError:
        print("Error accessing database.")




def get_next_pid():
    cursor.execute("Select MAX(pid) from airlines;")
    resulta=cursor.fetchone()
    current_pid=resulta[0]
    test=None
    if type(current_pid)==type(test):
        next_pid=1
    else:
        next_pid = int(current_pid) + 1
    return next_pid

def get_current_pid():
    cursor.execute("Select MAX(pid) from airlines;")
    resulta=cursor.fetchone()
    current_pid=resulta[0]
    test=None
    if type(current_pid)==type(test):
        next_pid=1
    else:
        next_pid = int(current_pid) 
    return next_pid

def checkings():#working properly (test 4 conductedd)
    pass_id=int(input("Enter your passenger Id: "))
    fullname=input("Enter your Full name: ")
    pw = input("Enter your password: ")
    try:
        typer2("Validating Info.")
        time.sleep(1)
        typer2("Validating Info..")
        time.sleep(1)
        typer2("Validating Info...")
        time.sleep(1)
        checker="Select * from customer where Passenger={};".format(pass_id)
        cursor.execute(checker)
        doubler2=cursor.fetchone()
        if doubler2==None:
            print("Invalid details")
            exit()
        doubler=doubler2[6]
        while True:
            if doubler==pw:
                print("\t\t---------------------------------")
                print("\t\t| 1. Extract Flight Details     |")
                print("\t\t| 2. Extract Personal Details   |")
                print("\t\t| 3. Extract Credit Details     |")
                print("\t\t| 4. Boarding Pass              |")
                print("\t\t| 5. Exit                       |")
                print("\t\t---------------------------------")
                pid=int(doubler2[5])
                f=(doubler2[1])
                l=(doubler2[2])
                P=(doubler2[3])
                m=(doubler2[4])
                confirm=int(input("Response: "))
                if confirm==2:
                    print("Extracting Info.")
                    time.sleep(1)
                    print("Extracting Info..")
                    time.sleep(1)
                    print("Extracting Info...")
                    time.sleep(1)
                    print("------------------------------------------------------------------------------------------------------------")
                    print("|      First Name      |      Last Name      |      Phone      |      Meal      |            PID           |")
                    print("------------------------------------------------------------------------------------------------------------")
                    print(f"|         {f}         |        {l}          |      {P}        |       {m}       |           {pid}         |")
                    print("------------------------------------------------------------------------------------------------------------")
                    time.sleep(3)
                elif confirm==1:
                    lastquery="Select * from airlines where PID={};".format(pid)
                    cursor.execute(lastquery)
                    resultant=cursor.fetchone()
                    airline=resultant[1]
                    acity=resultant[2]
                    dcity=resultant[3]
                    tod=resultant[4]
                    date=resultant[5]
                    price=resultant[6]
                    rt=resultant[7]
                    print("Extracting Info.")
                    time.sleep(1)
                    print("Extracting Info..")
                    time.sleep(1)
                    print("Extracting Info...")
                    time.sleep(1)
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print("|      Airlines      |      Arrival      |      Departure      |      Time      |            Date           |          Price           |")
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print(f"|     {airline}     |      {acity}      |      {dcity}        |       {tod}    |           {date}          |            {price}       |")
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    time.sleep(3)
                elif confirm==3:
                    lastquery3="Select * from payment_info where Passenger={} ".format(pass_id)
                    cursor.execute(lastquery3)
                    resultant3=cursor.fetchone()
                    print("Extracting Info.")
                    time.sleep(1)
                    print("Extracting Info..")
                    time.sleep(1)
                    print("Extracting Info...")
                    time.sleep(1)
                    c=resultant3[0]
                    pr=resultant3[1]
                    p=resultant3[2]
                    cv=resultant3[3]
                    print("-------------------------------------------------------------------------")
                    print("|      Passenger      |      Card      |      Price      |      Cvv      |")
                    print("-------------------------------------------------------------------------")
                    print(f"|       {p}         |       {c}       |      {pr}        |      {cv}    |")
                    print("-------------------------------------------------------------------------")
                    time.sleep(3)
                    print("Your credit details are",resultant3)
                elif confirm==4:
                    pid = pass_id
                    cursor.execute("select fname,lname,pid from customer where Passenger='{}';".format(pid))
                    x=cursor.fetchone()
                    print(x)
                    if x is not None:
                        fna=x[0]
                        lna=x[1]
                        p=x[2]
                        print(fna,lna,p)
                        cursor.execute("Select Arrival,Departure,TOD,Date from airlines where pid={}".format(p))
                        y=cursor.fetchall()
                        print(y)
                        if y is not None:
                            arriv=y[0][0]
                            dept=y[0][1]
                            tod=y[0][2]
                            date=y[0][3]
                        seat=12   #seat()
                        print("╭─────────────────────────────────")
                        print("│                                 ")
                        print("│          BOARDING PASS          ")
                        print("│         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         ")
                        print(f"│   Flight:     {p}            ")
                        print(f"│   Date:       {date}           ")
                        print(f"│   Departure:  {dept}           ")
                        print(f"│   Gate:       2B               ")
                        print(f"│   Seat:       {seat}           ")
                        print(f"│   Time:       {tod}            ")
                        print(f"│                                ")
                        print(f"│        {fna} {lna}             ")
                        print(f"│                                ")
                        print(f"│   To:       {arriv}          ")
                        print(f"│   From:        {dept}            ")
                        print("│                                 ")
                        print("│                                 ")
                        print("│   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ")
                        print("│   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ")
                        print("│   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ")
                        print("│             __|__               ")
                        print("│      --------(_)--------        ")
                        print("│        O  O       O  O          ")
                        print("│                                 ")
                        print("╰─────────────────────────────────")
                        time.sleep(3)
                    else:
                        print("The passenger identification failed")
                else:
                    print("Reverting back, choice failed")
                    print("Exiting")
                    exit()
            else:
                print("Please enter info correctly")
                break
                
    except ValueError:
     print("Invalid password.")

def get_current_passenger_id():                                                             #working properly (test 4 conductedd)
    query = "SELECT MAX(Passenger) FROM customer;"
    cursor.execute(query)
    result = cursor.fetchone()
    max_passenger_id = result[0]
    exception_grp=None
    if type(max_passenger_id)==type(exception_grp):
        current_passenger_id=1
    else:
        current_passenger_id = max_passenger_id
    return current_passenger_id

def continue_payment ():                    #working properly (test 4 conductedd)
    query="select * from payment_info"
    cursor.execute(query)
    Data=cursor.fetchall()
    Data2=pd.DataFrame(Data)
    Data2.columns=["1","2","3","4"]
    paid=Data2['3'].tolist()
    query2="select Passenger from customer"
    cursor.execute(query2)
    notpaid=cursor.fetchall()
    notpaid=pd.DataFrame(notpaid)
    notpaid.columns=['1']
    notpaid=notpaid['1'].tolist()
    x=[]
    for i in notpaid:
        if i not in paid:
            x.append(i)
    notpaid=x
    pasenger=int(input("Enter your passenger id: "))
    if pasenger in paid:
        print("Already paid")
        sys.exit()
    elif pasenger in notpaid:
        cursor.execute("Select pid from customer where Passenger={}".format(pasenger))
        pid=cursor.fetchall()
        pid=str(pid[0][0])
        cursor.execute("SELECT Ticket FROM airlines WHERE pid = {}".format(pid))
        row = cursor.fetchone()
        price=row[0]
        price=int(price)
        x=random.uniform(-0.1, 0.2)
        new_price= price + price * x
        new_price=math.ceil(new_price)
        credit_card_number = input("Enter credit card number: ")
        print("Your final Price is: ", new_price)
        user_ver = input("Do you want to continue? (Y/N): ")
        try:
            if user_ver.lower() == "y" or user_ver.upper() == "yes":
                name=input("Enter your Full Name on Card: ")
                expiry=input("Enter your Expiry Date on Card: ")
                Cvv=input("Enter your CVV: ")
                name=name
                expiry=expiry
                insert_query = "INSERT INTO payment_info values('{}','{}','{}','{}')".format(credit_card_number,new_price, pasenger, Cvv)
                cursor.execute(insert_query)
                con.commit()
                print("Saving.")
                time.sleep(1)
                print("Saving..")
                time.sleep(1)
                print("Saving...")
                time.sleep(1)
                print("Payment successfully!")
                x=1
            elif user_ver.lower()=="n" or user_ver.lower()=="no":
                print("Payment cancelled.")
        except Exception as e:
            print("Error occurred while saving payment details:", e)
        return x
    elif pasenger not in paid and pasenger not in notpaid:
        print("Pleaes, First book a flight")
    else:
        print("ERror")

def tickets():#working properly (test 4 conductedd)
    time.sleep(2)
    webbrowser.open("https://www.youtube.com/watch?v=KUW_3t4SmL0") 
    time.sleep(16)

    ctypes.windll.user32.keybd_event(0x12, 0, 0, 0) 
    ctypes.windll.user32.keybd_event(0x73, 0, 0, 0) 
    ctypes.windll.user32.keybd_event(0x73, 0, 0x0002, 0) 
    ctypes.windll.user32.keybd_event(0x12, 0, 0x0002, 0)





def admin_control():                                                              #working properly (test 4 conductedd)
    print("\t\t---------------------------------")
    print("\t\t|--------Manual Controls--------|")
    print("\t\t|                               |")
    print("\t\t| 1. Free-Based System          |")
    print("\t\t| 2. Add a flight               |")
    print("\t\t| 3. Modify an Existing flight  |")
    print("\t\t| 4. Delete a flight            |")
    print("\t\t|                               |")
    print("\t\t|------Automated Controls-------|")
    print("\t\t|                               |")
    print("\t\t| 5. Refresh Dates              |")
    print("\t\t| 6. Flight Generator           |")
    print("\t\t| 7. Exit                       |")
    print("\t\t|                               |")
    print("\t\t---------------------------------") 

def update():                   #working properly (test 4 conductedd)
    print("")
    cursor.execute("Select * from airlines")
    result2=cursor.fetchall()
    df_result3=pd.DataFrame(result2)
    print(df_result3)
    ifpid=input("Enter the flight pid you want to update:")
    cursor.execute("Select pid from airlines")
    pid=cursor.fetchall()
    if type(ifpid)!=None:
        airlines=input("Enter airline name: ")
        airlines=airlines.title()
        arrival=input("Enter Arrival location: ")
        arrival=arrival.title()
        departure=input("Enter Departure location: ")
        departure=departure.title()
        tod=input("Enter Time of Departure: ")
        date=input("Enter airline Date (yy-mm-dd): ")
        rt=input("Will flight convey a round trip?: ")
        rt=rt.title()
        pid=get_next_pid()
        price=input("Enter the base price (note the price will be affected on different days for user): ")
        add = ("UPDATE airlines SET pid = '{}', airlines = '{}', arrival = '{}', departure = '{}', tod = '{}', date = '{}', price = '{}',rt='{}' WHERE pid = {};".format(pid,airlines,arrival, departure, tod,date,price,rt,pid))
        cursor.execute(add)
        con.commit()
    elif type(ifpid) ==None:
        print("The pid you have entered does not exist please provide a valid pid, or add a new flight")
        exit()
    else:
        print("Values Erorr occured")

def delete():#working properly (test 4 conductedd)
    cursor.execute("Select * from airlines")
    result2=cursor.fetchall()
    df_result3=pd.DataFrame(result2)
    print(df_result3)
    ifpid=input("Enter the flight pid you want to delete: ")
    delete=("delete from airlines where pid={}".format(ifpid))
    cursor.execute(delete)
    con.commit()
    print("Deleted")

def add():                                             #working properly (test 4 conductedd)
        airlines=input("Enter airline name: ")
        airlines=airlines.title()
        arrival=input("Enter Arrival location: ")
        arrival=arrival.title()
        departure=input("Enter Departure location: ")
        departure=departure.title()
        tod=input("Enter Time of Departure: ")
        date=input("Enter airline Date (yy-mm-dd): ")
        rt=input("Will flight convey a round trip?: ")
        rt=rt.title()
        pid=get_next_pid()
        price=input("Enter the base price (note the price will be affected on different days for user): ")
        add = ("insert INTO airlines values({},'{}','{}','{}','{}','{}','{}','{}')".format(pid,airlines,arrival, departure, tod,date,price,rt))
        cursor.execute(add)
        con.commit()
        print("Added")

def airlines_gen():
    print("This can create an infinite number of airlines mockups which you can fill in the table of airlines")
    continues=input("Do you want to continue? (y/n): ")
    if continues.upper()=='Y' or continues.upper()=='YES':
        user_wants=int(input("Enter the number of mocks up you need: "))
        arrival=['Goa','Mumbai','Delhi','Pune']
        departure=['Goa','Mumbai','Delhi','Pune']
        tod=['5:30','18:00','12:00','21:45']
        airlines=['Vistara','Flydubai','IndiGo']
        ticket=['6000','11000','9000','7500','8000']
        rt=['no','yes']
        pid=get_current_pid()
        while True:
            x=random.randint(0,3)
            y=random.randint(0,3)
            z=random.randint(0,3)
            a=random.randint(0,2)
            b=random.randint(0,4)
            c=random.randint(0,1)
            if x==y:                                             #pid,name,arr,dept,tod,date,price,rt
                continue
            else:
                pid+=1
                zam=(pid,airlines[a],arrival[x],departure[y],tod[z],'{}',ticket[b],rt[c])
                zam=tuple(zam)
                print(zam)
                time.sleep(0.3)
                if pid==get_current_pid()+user_wants:
                    print(user_wants," generated")
                    exit()
    else:
        print("Exiting")
        exit()


def root_pw():             #working properly (test 4 conductedd)
    webbrowser.open("https://www.youtube.com/watch?v=V4MF2s6MLxY") 
    time.sleep(21)

    ctypes.windll.user32.keybd_event(0x12, 0, 0, 0) 
    ctypes.windll.user32.keybd_event(0x73, 0, 0, 0) 
    ctypes.windll.user32.keybd_event(0x73, 0, 0x0002, 0) 
    ctypes.windll.user32.keybd_event(0x12, 0, 0x0002, 0)

def reset():
    print("Note: This will ERASE the existing DATA")
    userint=input("Are you sure you want to PROCEED?: ")
    if userint.upper()=="Y" or userint.upper()=="YES":
        typer2("Erasing...")
        time.sleep(2)
        userint2=input("THE ENTIRE DATA HAS BEEN ERASED YOU CAN STILL RETRIVE THE DATA, DO YOU WANT TO RETRIVE IT?: ")
        if userint2.upper()=="Y" or userint2.upper()=="YES":
            print("Retriving")
            time.sleep(2)
            print("Retrived")
            exit()
        else:
            cursor.execute("Delete from test;")
            cursor.execute("Drop table airlines;")
            cursor.execute("Drop table customer;")
            cursor.execute("Drop table payment_info;")
            print("THE DATA HAS BEEN ERASED, RERUN THE CODE for a new experience")
            con.commit()
            exit()
    else:
        print("Exi8ng")
        exit()


def boardin_pass():
    pid = input("Enter your passenger identifier: ")
    cursor.execute("select fname,lname,pid from customer where Passenger='{}';".format(pid))
    x=cursor.fetchone()
    print(x)
    if x is not None:
        fna=x[0]
        lna=x[1]
        p=x[2]
        print(fna,lna,p)
        cursor.execute("Select Arrival,Departure,TOD,Date from airlines where pid={}".format(p))
        y=cursor.fetchall()
        print(y)
        if y is not None:
            arriv=y[0][0]
            dept=y[0][1]
            tod=y[0][2]
            date=y[0][3]
        seat=12   #seat()
        print("╭─────────────────────────────────")
        print("│                                 ")
        print("│          BOARDING PASS          ")
        print("│         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         ")
        print(f"│   Flight:     {p}            ")
        print(f"│   Date:       {date}           ")
        print(f"│   Departure:  {dept}           ")
        print(f"│   Gate:       2B               ")
        print(f"│   Seat:       {seat}           ")
        print(f"│   Time:       {tod}            ")
        print(f"│                                ")
        print(f"│        {fna} {lna}             ")
        print(f"│                                ")
        print(f"│   To:       {arriv}          ")
        print(f"│   From:        {dept}            ")
        print("│                                 ")
        print("│                                 ")
        print("│   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ")
        print("│   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ")
        print("│   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ")
        print("│             __|__               ")
        print("│      --------(_)--------        ")
        print("│        O  O       O  O          ")
        print("│                                 ")
        print("╰─────────────────────────────────")
    else:
        print("The passenger identification failed")

def testables():
    cursor.execute("insert into customer values(1,'test','test','0000000000','Veg',698,'0000');")
    cursor.execute("insert into payment_info values(0000,0000,1,000);")
    con.commit()



#RERUNING PROHIBTION--#RERUNING PROHIBTION--#RERUNING PROHIBTION--#RERUNING PROHIBTION--#RERUNING PROHIBTION--#RERUNING PROHIBTION--#RERUNING PROHIBTION--#RERUNING PROHIBTION--#RERUNING PROHIBTION--


cursor.execute("CREATE TABLE if not exists test (num INTEGER);")
con.commit()
y=no_rerun()
if y==1:
    pass
else:
    table()
    rerun()








#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--#MAIN CODE--
menu()
x=1
while True:
    if x==1:
        x=0
    else:
        menu_2()
    try:
        print("ROOT_PW IS REMOVED,TICKETS IS REMOVED,PLEASE REMOVE THE # FOR IT TO WORK")
        user=int(input("Your Response:"))
        if user==1:
            l1=["Goa","Mumbai","Delhi","Pune"]
            while True:
                print("\t\t--------------------------")
                print("\t\t|         CITY TABLE     |")
                print("\t\t--------------------------")
                print("\t\t|   Goa     |   Mumbai   |")
                print("\t\t|-----------|------------|")
                print("\t\t|   Pune    |   Delhi    |")
                print("\t\t--------------------------")
                time.sleep(1)
                Arrival=input("Please choose a Arrival City from Above: ")
                Departure=input("Please choose a Departure City from Above: ")
                Arrival=Arrival.lower().title()
                Departure=Departure.lower().title()
                if Arrival==Departure or Arrival and Departure not in l1:
                    print("\n","\n","\n","Please enter the info Correctly","\n")
                    termination=int(input("PRESS 1 to EXIT or 0 to CONTINUE: "))
                    if termination==1:
                        print("Exiting")
                        break
                    else:
                        continue
                else:
                    Arrival="'"+Arrival+"'"
                    Departure="'"+Departure+"'"
                    query="Select * from airlines where Arrival={} and Departure={}".format(Arrival,Departure)
                    cursor.execute(query)
                    data=cursor.fetchall()
                    df=pd.DataFrame(data)
                    df.columns = ['Plane Id', 'Airline', 'Arrival City','Departure City', 'Time', 'DoD', 'Ticket Price','Round Trip']
                    print("\n","\n","\n","\n","THESE ARE THE AVAILBLE FLIGHTS")
                    print(df.to_string(index=False))
                    plane_ids = df['Plane Id'].tolist()
                    time.sleep(2)
                    print("\n","What would you like to do now?","\n", "1.Choose a flight", "\n","2.Exit","\n")
                    try:
                        user2 = int(input("RESPONSE: "))
                        try:
                            if user2==2:
                                sys.exit()
                            elif user==1:
                                login()
                                passenger_id=get_current_passenger_id()
                                output=input("Do you want to proceed with the payment?(yes/no): ")
                                output=output.upper()
                                if output=="YES" or output=="Y":
                                    if save_payment_details()==1:
                                        time.sleep(1)
                                        print("Flight booked Succesfully")
                                        print("Please remember your Seat number it will help you retrive information about the flight in the future")
                                        time.sleep(1)
                                        print("Your seat number: ", seat())
                                        print("Thankyou for choosing us")
                                        print("Here is your access pass")
                                        time.sleep(2)
                                        boardin_pass()
                                        time.sleep(5)
                                        typer2("Exiting.")
                                        time.sleep(1)
                                        typer2("Exiting..")
                                        time.sleep(1)
                                        typer2("Exiting...")
                                        time.sleep(1)
                                        typer2("Before exiting a message from us:")
                                        #tickets()
                                        time.sleep(1)
                                        sys.exit()
                                    else:
                                        print("Remember your login info is saved, You can check back at us")
                                        break
                                elif output=="NO":
                                    print("Thank You, Your information has been saved for future uses")
                                    sys.exit()
                                else:
                                    print("Invalid Option")
                        except ValueError:
                            print("Invalid input. Please enter a valid response.")
                    except Exception as e:
                        print("An error occured,",e)
        elif user==2:
                checkings()
        elif user==3:
            modify()
        elif user==4:
            print("This is continuation of payment")
            time.sleep(1)
            print("Please make sure your details were saved previously")
            time.sleep(1)
            a=continue_payment()
            if a==1:
                print("Flight booked Succesfully")
                print("Please remember your Seat number it will help you retrive information about the flight in the future")
                time.sleep(1)
                print("Your seat number: ", seat())
                print("Thankyou for choosing us")
                time.sleep(5)
                typer2("Exiting.")
                time.sleep(1)
                typer2("Exiting..")
                time.sleep(1)
                typer2("Exiting...")
                sys.exit()
            else:
                sys.exit()
        elif user==5:
            print("EXITED")
            exit()
        elif user==12:
            masterpass_check=int(input("Enter Master Password: "))
            try:
                if masterpass_check==masterpass:
                    print("Password correct!")
                    #root_pw()
                    time.sleep(1)
                    print("Welcome Krishna")
                    time.sleep(2)
                    print("You have reache Admin Console")
                    time.sleep(1)
                    print("You can control the Backend of MYSQL from here")
                    time.sleep(1)
                    while True:
                        try:
                            admin_control()
                            admin_output=int(input("Enter Response:"))
                            if admin_output==1:
                                print("The existing data is:")
                                print("\t\t--------------------------")
                                print("\t\t| Databases |   Tables   |")
                                print("\t\t--------------------------")
                                print("\t\t|  airport  |  customer  |")
                                print("\t\t|-----------|------------|")
                                print("\t\t|   None    |   airlines |")
                                print("\t\t|-----------|------------|")
                                print("\t\t|   None    |payment_info|")
                                print("\t\t--------------------------")
                                while True:
                                    querry=input("Enter any querry in mysql command form:")
                                    try:
                                        cursor.execute(querry)
                                        result=cursor.fetchall()
                                        df_result=pd.DataFrame(result)
                                        print(df_result)
                                    except Exception as e:
                                        print("An Error occured",str(e) )
                                    inp=input("Want to commit?(y/n): ")
                                    if inp=="y" or inp=="Y":
                                        con.commit()
                                        print("Commited")
                                    else:
                                        pass
                                    inpt=input("Want to continue?(y/n): ")
                                    if inpt.upper()=="Y" or inpt.upper()=="YES":
                                        continue
                                    else:
                                        print("Exiting")
                                        exit()
                            elif admin_output==4:
                                delete()
                            elif admin_output==2:
                                add()
                            elif admin_output==3:
                                update()
                            elif admin_output==6:
                                airlines_gen()
                            elif admin_output==5:
                                reset()
                                print("Dates refreshed")
                            elif admin_output==7:
                                print("Exited")
                                exit()
                        except Exception as f:
                            print("Eror",f)
                else:
                    print("Invalid Masterpassword. ABORTING")
                    sys.exit()
            except ValueError:
                print("an Value Erorr Occured")
                sys.exit()
        else:
            print("Please Choose a Valid Option")
    except ValueError as e:
        print("Please enter an integer")
        continue
