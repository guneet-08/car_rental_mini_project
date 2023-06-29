"""CREATING DATABASES AND ALL THE REQUIRED TABLES NEEDED TO RUN THE PROJECT
DATABASE NAME: Car
TABLES: Admins, Cars, Rentings, Sales"""

import mysql.connector as mc

def create_database():
    cn=mc.connect(host='localhost',user='root',passwd='root')
    Cursor = cn.cursor()
    Cursor.execute("drop database if exists CAR;")
    Cursor.execute("create database CAR;")
    Cursor.execute("use CAR;")
    Cursor.close()
    cn.close()

def create_tables():
    cn=mc.connect(host='localhost',user='root',passwd='root',database='CAR')

    t1 = """
    create table cars
    (
    Car_no int(4),
    Car_class char(10),
    Model_name char(50),
    Car_color char(10),
    Capacity int,
    Daily_Rent int,
    Car_Status char(10) default 'AVAILABLE',
    Rent_ID int default NULL
    );
    """
    t2 = """
    create table admins
    (
    password varchar(10)
    );
    """

    t3 = """
    create table rentings
    (
    Rent_ID int,
    Cust_Name varchar(20),
    Cust_Phone_no bigint,
    Car_no int,
    Date_Rented varchar(10),
    Return_Date varchar(10),
    Driver varchar(5),
    Total_Rent int
    );
    """
    t4 = """
    create table sales
    (
    Rent_ID int,
    Car_no int,
    Cust_name varchar(20),
    Phone_No bigint,
    Return_Date varchar(10),
    Sales int
    );
    """
    Cursor = cn.cursor()
    Cursor.execute(t1)
    Cursor.execute(t2)
    Cursor.execute(t3)
    Cursor.execute(t4)
    cn.close()

def populate_tables():
    cn=mc.connect(host='localhost',user='root',passwd='root',database='CAR')

    val1 = """
    insert into cars values
    (1101,'SUV','KIA SELTOS','WHITE',5,1700,'AVAILABLE',NULL),
    (1102,'SUV','MAHINDRA SCORPIO','GREY',7,1500,'AVAILABLE',NULL),
    (1103,'SUV','TOYOTA FORTUNER','BLACK',7,1900,'AVAILABLE',NULL),
    (1104,'SUV','MG HECTOR','RED',5,2000,'AVAILABLE',NULL),
    (1201,'SEDAN','HONDA CITY','RED',5,900,'AVAILABLE',NULL),
    (1202,'SEDAN','HYUNDAI VERNA','WHITE',6,950,'AVAILABLE',NULL),
    (1203,'SEDAN','SKODA RAPID','GREY',5,1000,'AVAILABLE',NULL),
    (1204,'SEDAN','NISSAN SUNNY','GREY',5,850,'AVAILABLE',NULL),
    (1301,'LUXURY','RANGE ROVER EVOQUE','WHITE',4,4000,'AVAILABLE',NULL),
    (1302,'LUXURY','AUDI Q6','BLACK',2,3500,'AVAILABLE',NULL),
    (1303,'LUXURY','LINCHON LIMOUSINE','BLACK',7,6000,'AVAILABLE',NULL),
    (1304,'LUXURY','MERCEDES BENZ S-CLASS','WHITE',4,4500,'AVAILABLE',NULL),
    (1401,'SPORTS','PORSCHE 911 CARRERA','WHITE',2,4800,'AVAILABLE',NULL),
    (1402,'SPORTS','JAGUAR F-TYPE','BLACK',2,4700,'AVAILABLE',NULL),
    (1403,'SPORTS','NISSAN GT-R','BLACK',2,4300,'AVAILABLE',NULL),
    (1404,'SPORTS','BUGGATI CHIRON','SILVER',2,6000,'AVAILABLE',NULL);
    """

    val2 = """
    insert into admins values('025486');
    """

    Cursor = cn.cursor()
    Cursor.execute(val1)
    Cursor.execute(val2)
    cn.commit()
    cn.close()