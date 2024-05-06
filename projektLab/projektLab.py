
## Example 1 - modules in python
## See example in calculator folder
## Example 2 - datatime module
# from datetime import date
# print(date.today())
###########################################
## Zapis/odczyt danych typ s�ownik do pliku
## Example 3 - load .csv file as dictionary
# import csv
# with open('customer.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)     # each line as dict
#     for row in csv_reader:
#         print(row)

## more option, see info: https://docs.python.org/3/library/csv.html
################# Task
## Twoim zadaniem jest utworzenie pakietu obs�ugi
## nowych i aktualnych klient�w nowo-utworzonej biblioteki
## oraz jej dost�pnych zasob�w. Administratorem w/w wypo�yczalni
## jest biolotekarka, kt�ra �wietnie zna pythona.
###############################################
############    Zasoby:
## Folder Library zawiera 3 pliki zawieraj�ce nast�puj�ce dane:
## book.csv - dane ksi��ek
## address.csv - baza adres�w aktualnych czytelnik�w
## customer.csv - dane osobowe aktualnych czytelnik�w
################################################
############  Specyfikacja oprogramowania:
## Utw�rz nast�puj�ce modu�y:
## 1. Modu� main - g��wny modu�, kt�ry administruje zasobami wypo�yczalni
## musi zawiera�:  def __main__() ( uruchamia program)
## 2. Modu� obs�ugi ksi��ek zawieraj�cy 2 funkcje:
## funkcja 1: dodanie nowej ksi��ki do bazy (book.csv)
## funkcja 2: usuwanie ksi��ki do bazy opcje: wgl�dem ID lub tytu�u (book.csv)
##
## 3. Modu� obs�ugi klienta zawieraj�cy funkcje:
## funkcja 1: rejestracja nowego klienta lub usuwanie danych klienta z bazy
## funkcja 2: dodawanie (przez administratora) danych
## nowego klienta do bazy tj. do pliku customer.csv i address.csv
## Nowy klient podaje swoje dane (imie, nazwisko), nadawany jest w/w klientowi losowy numer ID z�o�ony z 4 cyfr
## w folderze DATABASE tworzony jest plik tekstowy (nazwa pliku to ID klienta)
## do kt�rego b�d� zapisywane dane wypo�yczonej przez klienta ksi��ki oraz
## data wypo�yczenia a potem zwrotu ksi��ki
## funkcja 3: usuwanie danych klienta opcje: wzgl�dem ID lub NAME
## Wypo�yczanie ksi��ki/-ek przez u�ytkownika 2 funkcje:
## funkcja 4: wypo�yczenie ksi��ki lub kilku ksi��ek przez klienta
## funkcja 5: zwrot 1 ksi��ki przez klienta
##
## Je�li sko�czy�e� zadanie, przyjmij rol� kolejnego programisty
## kt�ry dosta� zadanie aktualizacji Twojego oprogramowania
## Nie modyfikuj�c i nie zmieniaj�c nazwy funkcji "udekoruj"
# funkcja nr 5: "zwrot 1 ksi��ki przez klienta" i nadpisz jej zawarto��
## tak aby klient mia� mo�liwo�� zwrotu dowolnej liczby ksi��ek

## WYMAGANIA:
## - mo�esz programowa� wy��cznie w paradygmacie funkcyjnym
## - utw�rz funkcj� wy�szego rz�du
## - utw�rz funkcj� wielu zmiennych wej�ciowych
## - utw�rz funkcj� zagnie�dzon�
## - u�yj dekoratora
## - wykonaj dokumentacj� dla conajmniej 1 funkcji i 1 modu�u
## - conajmniej dla 2 funkcji wykonaj obs�ug� wyj�tk�w  (dotyczy modu��w 2-4)

## WSKAZANIA:
## - mo�esz zwi�kszy� liczb� modu��w
## - dla zapisu/odczytu daty oraz danych do bazy wykorzystaj odpowiednie pakiety

