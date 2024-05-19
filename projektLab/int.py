import customers
import books
import tkinter as tk
from datetime import date

def add_book_interface():
    def add_book():
        id=int(entry1.get())
        author=entry2.get()
        title=entry3.get()
        pages=int(entry4.get())
        created=entry5.get()
        updated=entry6.get()
                
        books.add_book(id,author,title,pages,created,updated)
    
    window=tk.Tk()
    label1=tk.Label(window, text="podaj id")
    entry1=tk.Entry(window)
    label2=tk.Label(window, text="podaj autora")
    entry2=tk.Entry(window)
    label3=tk.Label(window, text="podaj tytul")
    entry3=tk.Entry(window)
    label4=tk.Label(window, text="podaj ilosc stron")
    entry4=tk.Entry(window)
    label5=tk.Label(window, text="podaj date stworzenia")
    entry5=tk.Entry(window)
    label6=tk.Label(window, text="podaj date aktualizacji")
    entry6=tk.Entry(window)
    button=tk.Button(window,command=add_book,text="dodaj ksiazke")
    
    entry1.grid(row=1,column=1)
    entry2.grid(row=2,column=1)
    entry3.grid(row=3,column=1)
    entry4.grid(row=4,column=1)
    entry5.grid(row=5,column=1)
    entry6.grid(row=6,column=1)
    
    label1.grid(row=1,column=2)
    label2.grid(row=2,column=2)
    label3.grid(row=3,column=2)
    label4.grid(row=4,column=2)
    label5.grid(row=5,column=2)
    label6.grid(row=6,column=2)
    
    button.grid(row=7,column=2)
    window.mainloop()        


