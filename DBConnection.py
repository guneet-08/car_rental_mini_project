import os
import getpass
import time
import mysql.connector as mc
import Database


#If you want to RESET the Database (or CREATE a fresh Instance):
Database.create_database()
Database.create_tables()
Database.populate_tables()

os.system('mode con lines=200 cols=200')

while True:
    os.system('cls')

    print('\t\t MAIN SYSTEM BOOT UP PROCEDURE')

    print('\t\t-----------SQL - PASSWORD-----------')
    print("\n\n\n\t\tEnter your computer's MY_SQL password : ",end='')
    paas=getpass.getpass('')

    try:
        cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    except:
        print('\n\t\tConnection Failed... Enter password again..')
        time.sleep(0.5)
        continue
    break

print('\t\t CONNECTING TO CAR DATABASE SERVER')
print('\t\t VALIDATING CREDENTIALS. PLEASE WAIT!')
time.sleep(2.0)
print('\t\t WELCOME TO G MAJOR CAR RENTALS')
print('\t\t **Your Journey, Our Support!**')
time.sleep(2.0)
try:
    from MenuControl import main_menu
    main_menu()
finally:
    if 'main_menu' in locals():
        del main_menu