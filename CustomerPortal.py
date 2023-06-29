import os
import time
import random
import datetime
import mysql.connector as mc
from PrintTools import title, cut
paas = 'root'


#VIEW CARS CUSTOMER
def view_cars_customer():
    os.system('cls')
    title()
    print('\t\t<<<- CUSTOMER PORTAL ->>>')
    print('\t\t    <- VIEW CARS ->')
    
    cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    cur=cn.cursor()
    cur.execute('select car_class,model_name,car_color,\
capacity,daily_rent,car_status from cars order by Car_Class;')
    l=cur.fetchall()   
    if len(l)==0:
        print('\n\tNo cars available in the store! Press enter to go \
back!')
        input()
        cn.close()
        try:
            from MenuControl import customer_portal
            customer_portal()
        finally:
            if 'customer_portal' in locals():
                del customer_portal
        return
    
    #printing table
    print('')
    sp=[15,20,15,15,15,15]
    z='+'
    for y in sp:
        z=z+'-'*(y+1)+'+'
    print(z)
    time.sleep(0.03)
    print('| ',cut('CAR_CLASS',15),'| ',\
            cut('MODEL_NAME',20),'| ',\
            cut('CAR_COLOR',15),'| ',\
            cut('CAPACITY',15),'| ',\
            cut('DAILY_RENT',15),'| ',\
            cut('CAR_STATUS',15),'|  ',sep="")
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
        from MenuControl import customer_portal
        customer_portal()
    finally:
        if 'customer_portal' in locals():
            del customer_portal
    return

#RENT CARS
def rent_cars():
    os.system('cls')
    
    print('<<<- CUSTOMER PORTAL ->>>')
    print('<- RENT CARS ->')

    #printing available cars
    cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    cur=cn.cursor()
    cur.execute("select car_no,car_class,model_name,car_color,capacity,\
daily_rent from cars where car_status='AVAILABLE' order by Car_Class;")
    l=cur.fetchall()
    if len(l)==0:
        print('\n\n\t\tSORRY! ALL CARS ARE CURRENTLY RENTED!!')
        print('\n\t\tRedirecting to Customer Portal... Press Enter')
        input()
        cn.close()
        try:
            from MenuControl import customer_portal
            customer_portal()
        finally:
            if 'customer_portal' in locals():
                del customer_portal

    print('\tAVAIABLE CARS:\n')
    print('')
    sp=[15,15,20,15,15,15]
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
            cut('DAILY_RENT',15),'| ',sep="")
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
    
    #obtaining details & validation
    cust_name=input('\n\tEnter your Full Name: ') #full name
    cust_no=input('\tEnter your Phone Number: ') #phone number        

    cur=cn.cursor()  #car_nos
    cur.execute("select car_no from cars where car_status='AVAILABLE'")
    l=cur.fetchall()
    while True:
        cars=input('\tEnter the car_nos of the cars you wish to rent \
separated by "," with no spaces: ')
        cars=cars.split(',')
        z='valid'
        for y in cars:
            x=(int(y),)
            if x not in l:
                z='invalid'
        if z=='invalid':
            print("\n\tPlease enter valid and available car_nos...\n")
            continue
        break
        
    while True:   #days
        days=int(input('\tEnter the no. of days you wish to borrow the car \
including today (max 15): '))
        if days in range(1,16):
            days=int(days)
            break
        print("\n\tPlease enter valid no. of days...\n")

    while True:   #driver
        driver=input('\tWill you need a driver (y/n) \
[ Rs. 500 per day per car ]: ')
        if driver.lower() in ['y','n']:
            break
        print('\n\tPlease enter valid answer...\n')

    #unique rent_id generation
    rent_id=random.randint(1000,10000)
    cur=cn.cursor()
    cur.execute('select rent_id from rentings;')
    l=cur.fetchall()
    x=(rent_id,)
    while x in l:
        x=random.randint(1000,10000)
    rent_id=x[0]
    
    #dates
    rent_date=datetime.datetime.now()
    return_date = rent_date + datetime.timedelta(days=days)
    rent_date=rent_date.strftime("%d-%m-%y")
    return_date=return_date.strftime("%d-%m-%y")

    #receipt table and preparing for renting
    print('\n\tRedirecting to Receipt Table....Press Enter')
    input()

    os.system('cls')
    title()
    print('<<<- CUSTOMER PORTAL ->>>')
    print('   <- RECEIPT TABLE ->')

    print('\n')
    col,lin=os.get_terminal_size()
    L=[]
    n=30
    print(' '*n+'+'+'='*(col-2*n-2)+'+')
    L.append('CAR RENTAL'+' : RENT RECEIPT')
    L.append('='*(col-2*n-2))
    L.append('RENT-ID : '+str(rent_id))
    L.append('CUSTOMER NAME: '+cust_name.upper())
    L.append('-'*(col-2*n-2))
    L.append('RENT DATE: '+rent_date)
    L.append('RETURN DATE: '+return_date)
    L.append('DAYS RENTED: '+str(days))
    L.append('-'*(col-2*n-2))
    L.append('-:PROJECTED RENT:-')

    car_and_rent=[]
    total=0
    for car_no in cars:
        cur=cn.cursor()
        cur.execute('select daily_rent from cars where car_no={};'\
                    .format(car_no))
        x=cur.fetchall()
        x=x[0][0]
        rent=x*days
        total=total+(x*days)
        L.append('CAR NO.'+str(y)+' --> '+str(x)+' * '+str(days)+' = '+\
                 str(x*days))
        if driver=='y':
            L.append('DRIVER --> 500 * '+str(days)+' = '+str(days*500))
            rent=rent+(days*500)
            total=total+(days*500)
        car_and_rent.append({'car_no':car_no,'rent':rent})
        
    L.append('-'*(col-2*n-2))
    L.append('TOTAL :- Rs.'+str(total))
    L.append('-'*(col-2*n-2))
    L.append('Please print this receipt and take it to our')
    L.append(' shop to get the cars')
    L.append('-'*(col-2*n-2))
    L.append('(:  HAVE A NICE DAY  :)')

    for y in L:
        sp=' '*n
        d1=' '*int((col-2*n-len(y)-2)/2)
        d2=' '*( col-2*n-2-len(y) - int((col-2*n-len(y)-2)/2) )
        print(sp+'|'+d1+y+d2+'|')
        time.sleep(0.03)
    print(' '*n+'+'+'='*(col-2*n-2)+'+')
    print('')

    #confirmation
    print('\n\tEnter y when you have shown this receipt and taken \
the cars')
    print('\tEnter n to cancel the renting')
    an=input('\tAnswer : ')
    if an=='y':
        pass
    else:
        print('\n\tRenting Cancelled....')
        print('\n\tRedirecting to Customer Portal.... Press Enter')
        input()
        cn.close()
        try:
            from MenuControl import customer_portal
            customer_portal()
        finally:
            if 'customer_portal' in locals():
                del customer_portal
        return

    #renting the cars
    cur=cn.cursor()
    for y in car_and_rent:
        q="insert into rentings values('{}','{}','{}','{}','{}','{}','{}'\
,'{}');".format(rent_id,cust_name,cust_no,y['car_no'],rent_date,return_date\
                ,driver,y['rent'])
        cur.execute(q)
        q="update cars set rent_id={},car_status='{}' where car_no={};"\
           .format(rent_id,'RENTED',y['car_no'])
        cur.execute(q)
    cn.commit() 
    print('\n\tCARS RENTED.... Press Enter')
    input()

    #important note
    os.system('cls')
    title()
    print('\t\t    <<<- CUSTOMER PORTAL ->>>')
    print('\t\t-.-.-.-.-.IMPORTANT NOTE.-.-.-.-.-')
    print('')
    print('''
\t\tTHE CUSTOMER HAS TO TAKE THE RECEIPT TO THE OFFICE TO GET THE CARS!
\t\tTHE PRICE OF FUEL IS NOT INCLUDED IN THE RECEIPT!

\t\tTHE CARS CAN BE RETURED EARLIER, RENT WILL BE ADJUSTED!
\t\tDELAYED REUTURNS WILL RESULT IN PENALTY!

\t\tIF ANY VEHICLE IS DAMAGED DUE TO CARELESSNESS OF CUSTOMER THE
\t\tCUSTOMER IS RESPONSIBLE TO PAY THE REPAIR EXPENSES!
''')
    
    print('\t\tRedirecting to Customer Portal.... Press Enter')
    input()
    cn.close()
    try:
        from MenuControl import customer_portal
        customer_portal()
    finally:
        if 'customer_portal' in locals():
            del customer_portal
    return

#RETURN CARS
def return_cars():
    os.system('cls')
    title()
    print('\t\t<<<- CUSTOMER PORTAL ->>>')
    print('\t\t   <- RETURN CARS ->')
    rent_id=int(input('\n\tEnter the RENT_ID : '))

    #validating
    cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    cur=cn.cursor()
    cur.execute('select rent_id from rentings;')
    l=cur.fetchall()
    x=(rent_id,)
    if x not in l:
        print('\n\tThis RENT_ID does not exist, enter again...')
        time.sleep(0.5)
        return_cars()
    print('\tRedirecting to Bill Table.... Press Enter')
    input()

    #bill table
    os.system('cls')
    title()
    print('\t\t<<<- CUSTOMER PORTAL ->>>')
    print('\t\t  <- BILL TABLE ->')

    #obtaining everything required for bill
    cur=cn.cursor()
    cur.execute('select cust_name,car_no,date_rented,driver,Cust_Phone_no \
from rentings where rent_id={};'.format(rent_id))
    l=cur.fetchall()
    cust_name=l[0][0]
    driver=l[0][3]
    phone=l[0][4]
    
    #dates
    rent_date    =  datetime.datetime.strptime(l[0][2],'%d-%m-%y')
    return_date  =  datetime.datetime.now()
    days         =  return_date-rent_date
    days         =  days.days+1
    rent_date    =  rent_date.strftime('%d-%m-%y')
    return_date  =  return_date.strftime('%d-%m-%y')

    #rent
    car_and_drent=[]
    for y in l:
        for x in range(0,len(y)):
            if x==1:
                car_no=y[x]
                cur=cn.cursor()
                cur.execute('select daily_rent from cars where car_no={};'\
                            .format(car_no))
                rent=(cur.fetchall())[0][0]
                t={'car_no':car_no,'rent':rent}
                car_and_drent.append(t)
                del t

    #printing the bill
    print('\n')
    col,lin=os.get_terminal_size()
    L=[]
    n=30
    total=0

    print(' '*n+'+'+'='*(col-2*n-2)+'+')
    L.append('CAR RENTAL : BILL')
    L.append('='*(col-2*n-2))
    L.append('RENT-ID : '+str(rent_id))
    L.append('CUSTOMER NAME: '+cust_name.upper())
    L.append('-'*(col-2*n-2))
    L.append('RENT DATE: '+rent_date)
    L.append('RETURN DATE: '+return_date)
    L.append('DAYS RENTED: '+str(days))
    L.append('-'*(col-2*n-2))
    L.append('-:RENT TO BE PAID:-')
    
    for y in car_and_drent:
        L.append('CAR NO.'+str(y['car_no'])+' --> '+str(y['rent'])\
                 +' * '+str(days)+' = '+str(y['rent']*days))
        total = total + y['rent']*days
        if driver=='y':
            L.append('DRIVER --> 500 * '+str(days)+' = '+str(days*500))
            total = total + days*500
    L.append('-'*(col-2*n-2))
    L.append('TOTAL :- Rs.'+str(total))
    L.append('-'*(col-2*n-2))
    L.append('Kindly pay this amount')
    L.append('And return the cars back')
    L.append('-'*(col-2*n-2))
    L.append('THANK YOU FOR CHOOSING US')
     
    for y in L:
        sp=' '*n
        d1=' '*int((col-2*n-len(y)-2)/2)
        d2=' '*( col-2*n-2-len(y) - int((col-2*n-len(y)-2)/2) )
        print(sp+'|'+d1+y+d2+'|')
        time.sleep(0.03)
        
    print(' '*n+'+'+'='*(col-2*n-2)+'+')
    print('')
    
    #confirmation
    print('\n\n\tEnter y when you have paid the bill & completed the \
return')
    print('\tEnter n to cancel the return')
    an=input('\tAnswer : ')
    if an!='y':
        print('\tReturn Cancelled....')
        print('\tRedirecting to Customer Portal.... Press Enter')
        input()
        cn.close()
        try:
            from MenuControl import customer_portal
            customer_portal()
        finally:
            if 'customer_portal' in locals():
                del customer_portal
        return

    #updating sales table
    for y in car_and_drent:
        car=y['car_no']
        ear=(y['rent'])*days    
        cur=cn.cursor()
        q="insert into sales values('{}','{}','{}','{}','{}','{}');"\
           .format(rent_id,car,cust_name,phone,return_date,ear)
        cur.execute(q)
        cn.commit()

    #returning
    cur=cn.cursor()
    cur.execute('delete from rentings where rent_id={};'.format(rent_id))
    cur=cn.cursor()
    cur.execute("update cars set car_status='{}', rent_id={} where \
rent_id={};".format('AVAILABLE','NULL',rent_id))
    cn.commit()
    print('\tCARS RETURNED....')
    print('\tRedirecting to Customer Portal.... Press Enter')
    input('')
    cn.close()
    try:
        from MenuControl import customer_portal
        customer_portal()
    finally:
        if 'customer_portal' in locals():
            del customer_portal
    return