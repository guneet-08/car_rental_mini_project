import os
from PrintTools import title

#MAIN PORTAL
def main_menu():
    os.system('cls')
    title()
    print("\t\t------------MAIN MENU-------------")
    print('''\
\t1       -->     Admin Portal
\t2       -->     Customer Portal
\n\tEnter   -->     Exit
    ''')
    
    ch=input('\n\tEnter the choice: ')
    
    if ch=='1':
        try:
            from MainMenu import admin_authentication
            admin_authentication()
        finally:
            if 'admin_authentication' in locals():
                del admin_authentication
    elif ch=='2':
        customer_portal()
    else:
        try:
            from MainMenu import program_end
            program_end()
        finally:
            if 'program_end' in locals():
                del program_end
    return

#ADMIN PORTAL
def admin_portal():
    os.system('cls')
    title()
    print('\t\t--------ADMIN PORTAL--------')
    print('''\
\t1       -->     Open Garage
\t2       -->     View Current Rentings
\t3       -->     View Sales Table
\n\tEnter   -->     Back
    ''')
    ch=input('\tEnter the choice: ')
    if ch=='1':
        try:
            from AdminPortal import garage
            garage()
        finally:
            if 'garage' in locals():
                del garage
    elif ch=='2':
        try:
            from AdminPortal import view_current_rentings
            view_current_rentings()
        finally:
            if 'view_current_rentings' in locals():
                del view_current_rentings
    elif ch=='3':
        try:
            from AdminPortal import sales_table
            sales_table()
        finally:
            if 'sales_table' in locals():
                del sales_table
    else:
        main_menu()
    return

#CUSTOMER PORTAL
def customer_portal():
    os.system('cls')
    title()
    print('\t\t--------CUSTOMER PORTAL--------')
    print('''\
\t1       -->     View Cars
\t2       -->     Rent Cars
\t3       -->     Return Cars
\n\tEnter   -->     Back
    ''')
    ch=input('\tEnter the choice: ')
    if ch=='1':
        try:
            from CustomerPortal import view_cars_customer
            view_cars_customer()
        finally:
            if 'view_cars_customer' in locals():
                del view_cars_customer
    elif ch=='2':
        try:
            from CustomerPortal import rent_cars
            rent_cars()
        finally:
            if 'rent_cars' in locals():
                del rent_cars
    elif ch=='3':
        try:
            from CustomerPortal import return_cars
            return_cars()
        finally:
            if 'return_cars' in locals():
                del return_cars
    else:
        main_menu()
    return