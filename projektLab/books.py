import pandas as pd

def add_book(id,author,title,pages,created,updated):
    df=pd.read_csv("book.csv")
    new=pd.DataFrame({"ID": [id], "AUTHOR": [author], "TITLE": [title], "PAGES": [pages], "CREATED": [created], "UPDATED": [updated]})
    df=pd.concat([df,new],ignore_index=True)
    df.to_csv('book.csv',index=False)
    print("dodano ksiazke "+title)
#add_book("155","nigga","cotton work","123","yesterday","never")


def remove_book(category,name):
    """
    Usuwa ksiazki z bazy danych.
    
    args:
    category(str): zmienna sluzaca do rozpoznania, czy chcemy usunac po ID, badz tytule.
    name(str): podany tytul, albo ID usuwanej ksi¹¿ki w zaleznoœci od zmiennej category.
    """
    if(category=="id"):
        df=pd.read_csv("book.csv")
        df=df[df['ID']!=name]
        df.to_csv('book.csv',index=False)
        print("usunieto ksiazke")
    elif(category=="title"):
        df=df[df['TITLE']!=name]
        df.to_csv("book.csv",index=False)
#remove_book("id",155)