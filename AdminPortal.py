import os
import time
import mysql.connector as mc
from PrintTools import title, cut
paas = 'root'

#GARAGE
def garage():
    os.system('cls')
    title()
    print('\t\t<<<- ADMIN PORTAL ->>>')
    print('\t\t     <- GARAGE ->')
    print('''\
\t1       -->     View Cars
\t2       -->     Add Car
\t3       -->     Remove Car
\n\tEnter   -->     Back
    ''')
    ch=input('\tEnter the choice: ')
    if ch=='1':
        view_cars_admin()
    elif ch=='2':
        add_car()
    elif ch=='3':
        remove_car()
    else:
        try:
            from MenuControl import admin_portal
            admin_portal()
        finally:
            if 'admin_portal' in locals():
                del admin_portal
    return

#VIEW CARS ADMIN
def view_cars_admin():
    os.system('cls')
    title()
    print('\t\t<<<- ADMIN PORTAL ->>>')
    print('\t\t     <- GARAGE ->')
    print()
    print('\t\t      VIEW CARS')

    cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    cur=cn.cursor()
    cur.execute('select * from cars order by Car_Class;')
    l=cur.fetchall()
    if len(l)==0:
        print('\n\tGarage empty! Press enter to go back!')
        input()
        cn.close()
        garage()
        return

    #printing table
    print('')
    sp=[10,15,20,15,10,15,15,10]
    z='+'
    for y in sp:
        z=z+'-'*(y+1)+'+'
    print(z)
    time.sleep(0.03)
    print('| ',cut('CAR_NO',10),'| ',\
            cut('CAR_CLASS',15),'| ',\
            cut('MODEL_NAME',20),'| ',\
            cut('CAR_COLOR',15),'| ',\
            cut('CAPACITY',10),'| ',\
            cut('DAILY_RENT',15),'| ',\
            cut('CAR_STATUS',15),'| ',\
            cut('RENT_ID',10),'| ',sep="")
    time.sleep(0.03)
    print(z)
    time.sleep(0.03)
    for y in range(0,len(l)):
        print('| ',end='')
        for x in range(0,len(l[y])):
            print(cut(l[y][x],sp[x]),end='') 
            print('| ',end='')
        print('')
        time.sleep(0.03)
    print(z)       
    input('\n\tPress ENTER to go back to Garage')
    garage()
    cn.close()
    return

#ADD CAR
def add_car():
    os.system('cls')
    title()
    print('\t\t<<<- ADMIN PORTAL ->>>')
    print('\t\t     <- GARAGE ->')
    print()
    print('\t\t       ADD CAR')

    #fetching details
    car_no=int(input('\tEnter the car number: '))

    cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    cur=cn.cursor()
    cur.execute('select car_no from cars;')
    l=cur.fetchall()
    x=(car_no,)
    if x in l:
        print('\n\tThe car_no you entered is already in use..Enter again')
        time.sleep(0.5)
        add_car()  
    car_class=input('\tEnter the car class: ')
    model_name=input('\tEnter the model name: ')
    car_color=input('\tEnter the car color: ')
    capacity=int(input('\tEnter the capacity: '))
    daily_rent=int(input('\tEnter the daily rent: '))

    #adding
    q="insert into cars(car_no,car_class,model_name,car_color,capacity,\
daily_rent) values('{}','{}','{}','{}','{}','{}');".format(car_no,\
car_class.upper(),model_name.upper(),car_color.upper(),capacity,daily_rent)
    cur=cn.cursor()
    cur.execute(q)
    print('\n\tCAR ADDED..... \n')
    cn.commit()
    print('\n\tRedirecting to Garage.... Press Enter')
    input('')
    garage()
    cn.close()
    return

#REMOVE CAR
def remove_car():
    os.system('cls')
    title()
    print('<<<- ADMIN PORTAL ->>>')
    print('     <- GARAGE ->')
    print()
    print('     REMOVE CAR')

    #printing cars
    print("\t You can only remove the cars which aren't rented\n")

    cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    cur=cn.cursor()
    cur.execute('select car_no,car_class,model_name,car_color,\
capacity, daily_rent, car_status from cars order by Car_Class;')
    l=cur.fetchall()
    print('')
    sp=[15,15,20,15,15,15,15]
    z='+'
    for y in sp:
        z=z+'-'*(y+1)+'+'
    print(z)
    time.sleep(0.03)
    print('| ',cut('CAR_NO',15),'| ',\
            cut('CAR_CLASS',15),'| ',\
            cut('MODEL_NAME',20),'| ',\
            cut('CAR_COLOR',15),'| ',\
            cut('CAPACITY',15),'| ',\
            cut('DAILY_RENT',15),'| ',\
            cut('CAR_STATUS',15),'| ',sep="")
    time.sleep(0.03)
    print(z)
    time.sleep(0.03)
    for y in range(0,len(l)):
        print('| ',end='')
        for x in range(0,len(l[y])):
            print(cut(l[y][x],sp[x]),end='')
            print('| ',end='')
        print('')
        time.sleep(0.03)
    print(z)

    #validating car_no
    cur=cn.cursor()
    cur.execute("select car_no from cars where car_status='AVAILABLE';")
    l=cur.fetchall()
    if len(l)==0:
        print('\n\tNo cars can be removed currently!, Press enter to go\
back')
        input()
        garage()
        cn.close()
        return
    c_no=input('\n\tEnter the car_no of the car to be remove: ')
    x=(int(c_no),)
    if x not in l:
        print('\n\tPlease enter valid car_no...')
        time.sleep(0.5)
        remove_car()
        

    #confirmation
    s=input('\tPlease confirm if you want to delete this car (y/n): ')
    if s=='y':
        pass
    else:
        print('\n\tRedirecting to Garage....Press Enter')
        input()
        garage()
        cn.close()
        return

    #removing
    cur=cn.cursor()
    q='delete from cars where Car_no={};'.format(c_no)
    cur.execute(q)
    print('\n\tCAR DELETED.....')
    cn.commit()
    print('\n\tRedirecting to Garage....Press Enter')
    input()
    cn.close()
    garage()

    #VIEW CURRENT BOOKINGS
def view_current_rentings():
    os.system('cls')
    title()
    print('\t\t<<<- ADMIN PORTAL ->>>')
    print('\t\t <-CURRENT RENTINGS->')
    
    cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    cur=cn.cursor()
    cur.execute('select * from rentings order by return_date;')
    l=cur.fetchall()
    if len(l)==0:
        print('\n\tNo cars rented currently!, Press enter to go back')
        input()
        cn.close()
        try:
            from MenuControl import admin_portal
            admin_portal()
        finally:
            if 'admin_portal' in locals():
                del admin_portal
        return

    #printing table
    sp=[10,20,15,10,15,15,10,10]
    z='+'
    for y in sp:
        z=z+'-'*(y+1)+'+'
    print(z)
    time.sleep(0.03)
    print('| '+cut('RENT_ID',10)+\
             '| '+cut('CUSTOMER_NAME',20)+\
             '| '+cut('PHONE NUMBER',15)+\
             '| '+cut('CAR_NO',10)+\
             '| '+cut('DATE_RENTED',15)+\
             '| '+cut('RETURN_DATE',15)+\
             '| '+cut('DRIVER',10)+\
             '| '+cut('TOTAL_RENT',10)+\
             '| ',sep='')
    time.sleep(0.03)
    print(z)
    time.sleep(0.03)
    for y in range(0,len(l)):
        print('| ',end='')
        for x in range(0,len(l[y])):
            print(cut(l[y][x],sp[x]),end='')
            print('| ',end='')
        print('')
        time.sleep(0.03)
    print(z)
    input('\n\tPress ENTER to go back')
    cn.close()
    try:
        from MenuControl import admin_portal
        admin_portal()
    finally:
        if 'admin_portal' in locals():
            del admin_portal
    return

#SALES TABLE
def sales_table():
    os.system('cls')
    title()
    print('\t\t<<<- ADMIN PORTAL ->>>')
    print('\t\t  <- SALES TABLE ->')

    cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    cur=cn.cursor()
    cur.execute('select * from sales order by return_date;')
    l=cur.fetchall()
    if len(l)==0:
        print('\n\tNo sales to show!, Press enter to go back')
        input()
        cn.close()
        try:
            from MenuControl import admin_portal
            admin_portal()
        finally:
            if 'admin_portal' in locals():
                del admin_portal
        return

    #printing table
    sp=[15,15,20,15,15,15]
    z='+'
    for y in sp:
        z=z+'-'*(y+1)+'+'
    print(z)
    time.sleep(0.03)
    print('| '+cut('RENT_ID',15)+\
             '| '+cut('CAR_NO',15)+\
             '| '+cut('CUST_NAME',20)+\
             '| '+cut('PHONE_NUMBER',15)+\
             '| '+cut('RETURN_DATE',15)+\
             '| '+cut('SALES',15)+\
             '| ',sep='')
    time.sleep(0.03)
    print(z)
    time.sleep(0.03)
    for y in range(0,len(l)):
        print('| ',end='')
        for x in range(0,len(l[y])):
            print(cut(l[y][x],sp[x]),end='')
            print('| ',end='')
        print('')
        time.sleep(0.03)
    print(z)
    input('\n\tPress ENTER to go back')
    cn.close()
    try:
        from MenuControl import admin_portal
        admin_portal()
    finally:
        if 'admin_portal' in locals():
            del admin_portal
    return