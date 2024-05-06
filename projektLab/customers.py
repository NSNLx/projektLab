import pandas as pd
from datetime import date
import random
import os

def add_customer(id,name,email,phone):
    df=pd.read_csv("customer.csv")
    new=pd.DataFrame({"ID":[id],"NAME":[name],"E-MAIL":[email],"PHONE":[phone],"CREATED":[date.today()],"UPDATED":[date.today()]})
    df=pd.concat([df,new],ignore_index=True)
    df.to_csv("customer.csv",index=False)
    print("utworzono klienta "+name)
#add_customer("199","andrzej bialobrzeski","xxx@gmail.com","231213321")
def remove_customer(id):
    df=pd.read_csv("customer.csv")
    df=df[df['ID']!=id]
    df.to_csv('customer.csv',index=False)
    print("usunieto klienta")
#remove_customer(199)
os.chdir("DATABASE")

def add_customer_admin(name):
    os.chdir("DATABASE")
    df=pd.read_csv("customer.csv")
    id=random.randint(1000,10000)
    id=string(id)
    new=pd.DataFrame({"ID":[id],"NAME":[name],"E-MAIL":["null"],"PHONE":["null"],"CREATED":[date.today()],"UPDATED":[date.today()]})
    df=pd.concat([df,new],ignore_index=True)
    df.to_csv("customer.csv")
    f=open(id+".csv","w")
#add_customer_admin("dawid trochimczuk")