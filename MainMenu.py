import os
import getpass
import mysql.connector as mc
from PrintTools import title
paas = 'root'


def admin_authentication():
    os.system('cls')
    title()
    print('\t\t--------ADMIN AUTHENTICATION--------')
    Pass=getpass.getpass("\tEnter Password: ")

    #password
    cn=mc.connect(host='localhost',user='root',passwd=paas,database='CAR')
    cur=cn.cursor()
    cur.execute('select * from admins')
    l=cur.fetchall()
    passwd=l[0][0]
    if passwd==Pass:
        print('\n\tAccess Granted ..... Press Enter')
        input('')
        cn.close()
        try:
            from MenuControl import admin_portal
            admin_portal()
        finally:
            if 'admin_portal' in locals():
                del admin_portal
    else:
        print('\n\tAccess Denied ..... Press Enter')
        input('')
        cn.close()
        try:
            from MenuControl import main_menu
            main_menu()
        finally:
            if 'main_menu' in locals():
                del main_menu
    return

def program_end():
    print()
    print("\t\tTHANKYOU FOR CHOOSING US!!")
    print("\t\t  SEE YOU AGAIN SOON!")
    print("\t\t         CIAO!")

    return