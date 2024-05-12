import pandas as pd
from datetime import date
import random
import os

def add_customer(id,name,email,phone):
    try:
        df=pd.read_csv("customer.csv")
    except FileNotFoundError:
        print("plik nie istnieje")
        new=pd.DataFrame({"ID":[id],"NAME":[name],"E-MAIL":[email],"PHONE":[phone],"CREATED":[date.today()],"UPDATED":[date.today()]})
    df=pd.concat([df,new],ignore_index=True)
    df.to_csv("customer.csv",index=False)
    print("utworzono klienta "+name)
#add_customer("199","andrzej bialobrzeski","xxx@gmail.com","231213321")
def remove_customer(id):
    try:
        df=pd.read_csv("customer.csv")
    except FileNotFoundError:
        print("plik nie istnieje")
    df=df[df['ID']!=id]
    df.to_csv('customer.csv',index=False)
    print("usunieto klienta")
#remove_customer(199)

def is_admin():
    a=input("czy jestes adminem? 1-tak, cokolwiek innego-nie ")    
    a=str(a)
    if(a==1):
        return True
    else:
        return False

def add_customer_admin_deco(function):
    def w_add_customer_admin(name,email,phone):        
        df=pd.read_csv("customer.csv")
        id=random.randint(1000,10000)
        while id in df['ID'].values:
            id=id=random.randint(1000,10000)
        id=str(id)
        new=pd.DataFrame({"ID":[id],"NAME":[name],"E-MAIL":[email],"PHONE":[phone],"CREATED":[date.today()],"UPDATED":[date.today()]})
        df=pd.concat([df,new],ignore_index=True)
        df.to_csv("customer.csv",index=False)
        os.chdir("DATABASE")
        id=str(id)
        f=open(id+".csv","w")
        f.write("ID_klienta,ID_ksiazki,data_wypozyczenia,data_zwrotu")    
        return function(name,email,phone)
    return w_add_customer_admin

@add_customer_admin_deco
def add_customer_admin(name,email,phone):
    pass
#add_customer_admin("wojchiech s","xx@x","123312123")


def borrow(id, *books):
    """
    Wypozycza ksiazki/ksiazke poprzez ID klienta
    
    args:
    id(int): ID klienta, ktory wypozycza ksiazki.
    books(int): ID ksiazek, ktore zostanq wypozyczone przez klienta.
    """
    os.chdir("DATABASE")
    id = str(id)
    df = pd.read_csv(id + ".csv")
    for book in books:
        new = pd.DataFrame({'ID_klienta': [id], 'ID_ksiazki': [book], 'data_wypozyczenia': [date.today()], 'data_zwrotu': ["brak"]})
        df = pd.concat([df, new], ignore_index=True)
        df.to_csv(id + ".csv",index=False)
#borrow(2094,201,202)
def returnbook(id, *books):
    os.chdir("DATABASE")
    id=str(id)
    df=pd.read_csv(id+".csv")
    for book in books:
        df.loc[df['ID_ksiazki']==book,'data_zwrotu']=date.today()
        df.to_csv(id+".csv")
#returnbook(2094,202,203)
        
        
    