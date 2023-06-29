import datetime

def title():
    print()
    print("\t\t---------G MAJOR CAR RENTALS ---------")
    print('\t\tDATE : '+ datetime.datetime.now().strftime("%d-%m-%y"))
    print('\t\tTIME - '+ datetime.datetime.now().strftime("%H:%M"))
    print("\t\t--------------------------------------")
    print()
    print()

def cut(s,n):
    s=str(s)
    if len(s)>n:
        return(s[:n])
    elif len(s)==n:
        return s
    else:
        return s+' '*(n-len(s))