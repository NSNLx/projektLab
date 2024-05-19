import customers
import books
import tkinter as tk
from datetime import date
from tkinter import messagebox


def add_book_interface():
    def add_book():
        try:
            id=int(entry1.get())
            author=entry2.get()
            title=entry3.get()
            pages=int(entry4.get())
            created=entry5.get()
            updated=entry6.get()
                    
            books.add_book(id,author,title,pages,created,updated)
            messagebox.showinfo("dodano ksiazke "+title)
        except ValueError:
            messagebox.showerror("nalezy podac opdowiednie rodzaje wartosci")
        except Exception as e:
            messagebox.showerror(e)


    window=tk.Tk()

    window.title("Graficzny manager")
    window.configure(bg='grey')

    label1=tk.Label(window, text="podaj id", bg='grey')
    entry1=tk.Entry(window, bg='grey')
    label2=tk.Label(window, text="podaj autora", bg='grey')
    entry2=tk.Entry(window, bg='grey')
    label3=tk.Label(window, text="podaj tytul", bg='grey')
    entry3=tk.Entry(window, bg='grey')
    label4=tk.Label(window, text="podaj ilosc stron", bg='grey')
    entry4=tk.Entry(window, bg='grey')
    label5=tk.Label(window, text="podaj date stworzenia", bg='grey')
    entry5=tk.Entry(window, bg='grey')
    label6=tk.Label(window, text="podaj date aktualizacji", bg='grey')
    entry6=tk.Entry(window, bg='grey')
    button=tk.Button(window,command=add_book,text="dodaj ksiazke", bg='grey')
    
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

def remove_book_interface():
    def remove_book():
        name=entry1.get()
        
        if(category.get()==1):
            choice="id"
        elif(category.get()==2):
            choice="title"
        books.remove_book(choice,name)
    
    window=tk.Tk()

    window.title("Graficzny manager")
    window.configure(bg='grey')

    category=tk.IntVar()
    category.set(1)

    label1=tk.Label(window,text="po czym chcesz usunac?", bg='grey')
    radio1=tk.Radiobutton(window, text="po ID", variable=category, value=1, bg='grey')
    radio2=tk.Radiobutton(window, text="po tytule", variable=category, value=2, bg='grey')
    entry1=tk.Entry(window, bg='grey')
    button=tk.Button(window,text="usun",command=remove_book, bg='grey')
    


    label1.grid(row=1,column=1)
    radio1.grid(row=2,column=1)
    radio2.grid(row=2,column=2)
    entry1.grid(row=3,column=2)
    button.grid(row=4,column=2)
    window.mainloop()


def add_customer_interface_a():
    def add_customer_a():
        
        name=entry1.get()
        email=entry2.get()
        phone=entry3.get()
   
        customers.add_customer_admin(name,email,phone)
        messagebox.showinfo("dodano klienta "+name)
    
    window=tk.Tk()

    window.title("Graficzny manager")
    window.configure(bg='grey')

    label1=tk.Label(window, text="podaj imie i nazwisko", bg='grey')
    entry1=tk.Entry(window, bg='grey')
    label2=tk.Label(window, text="podaj email", bg='grey')
    entry2=tk.Entry(window, bg='grey')
    label3=tk.Label(window, text="podaj numer telefonu", bg='grey')
    entry3=tk.Entry(window, bg='grey')
    button=tk.Button(window,command=add_customer_a,text="dodaj klienta(admin)", bg='grey')
    
    entry1.grid(row=1,column=1)
    entry2.grid(row=2,column=1)
    entry3.grid(row=3,column=1)

    label1.grid(row=1,column=2)
    label2.grid(row=2,column=2)
    label3.grid(row=3,column=2)



    button.grid(row=7,column=2)
    window.mainloop()        


def add_customer_interface():
    def add_customer():
        
        name=entry1.get()
        email=entry2.get()
        phone=entry3.get()
   
        customers.add_customer_admin(name,email,phone)
        messagebox.showinfo("dodano klienta "+name)
    
    window=tk.Tk()

    window.title("Graficzny manager")
    window.configure(bg='grey')

    label1=tk.Label(window, text="podaj imie i nazwisko", bg='grey')
    entry1=tk.Entry(window, bg='grey')
    label2=tk.Label(window, text="podaj email", bg='grey')
    entry2=tk.Entry(window, bg='grey')
    label3=tk.Label(window, text="podaj numer telefonu", bg='grey')
    entry3=tk.Entry(window, bg='grey')
    button=tk.Button(window,command=add_customer,text="dodaj klienta", bg='grey')
    
    entry1.grid(row=1,column=1)
    entry2.grid(row=2,column=1)
    entry3.grid(row=3,column=1)

    label1.grid(row=1,column=2)
    label2.grid(row=2,column=2)
    label3.grid(row=3,column=2)



    button.grid(row=7,column=2)
    window.mainloop()       

def interface():
    interface=tk.Tk()
    
    interface.title("Graficzny manager")
    interface.configure(bg='grey')

    label1=tk.Label(interface, text="co pragniesz zrobic?", bg='grey')
    
    button1=tk.Button(interface,text="dodac ksiazke",command=add_book_interface, bg='grey')
    button2=tk.Button(interface,text="usunac ksiazke",command=remove_book_interface, bg='grey')
    button3=tk.Button(interface,text="dodac klienta(admin)",command=add_customer_interface_a, bg='grey')
    button4=tk.Button(interface,text="dodac klienta",command=add_customer_interface, bg='grey')


    button1.grid(row=1,column=1)
    button2.grid(row=2,column=1)
    button3.grid(row=1,column=2)
    button4.grid(row=2,column=2)
    
    interface.mainloop()
interface()
