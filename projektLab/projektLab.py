
## Example 1 - modules in python
## See example in calculator folder
## Example 2 - datatime module
# from datetime import date
# print(date.today())
###########################################
## Zapis/odczyt danych typ s³ownik do pliku
## Example 3 - load .csv file as dictionary
# import csv
# with open('customer.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)     # each line as dict
#     for row in csv_reader:
#         print(row)

## more option, see info: https://docs.python.org/3/library/csv.html
################# Task
## Twoim zadaniem jest utworzenie pakietu obs³ugi
## nowych i aktualnych klientów nowo-utworzonej biblioteki
## oraz jej dostêpnych zasobów. Administratorem w/w wypo¿yczalni
## jest biolotekarka, która œwietnie zna pythona.
###############################################
############    Zasoby:
## Folder Library zawiera 3 pliki zawieraj¹ce nastêpuj¹ce dane:
## book.csv - dane ksi¹¿ek
## address.csv - baza adresów aktualnych czytelników
## customer.csv - dane osobowe aktualnych czytelników
################################################
############  Specyfikacja oprogramowania:
## Utwórz nastêpuj¹ce modu³y:
## 1. Modu³ main - g³ówny modu³, który administruje zasobami wypo¿yczalni
## musi zawieraæ:  def __main__() ( uruchamia program)
## 2. Modu³ obs³ugi ksi¹¿ek zawieraj¹cy 2 funkcje:
## funkcja 1: dodanie nowej ksi¹¿ki do bazy (book.csv)
## funkcja 2: usuwanie ksi¹¿ki do bazy opcje: wglêdem ID lub tytu³u (book.csv)
##
## 3. Modu³ obs³ugi klienta zawieraj¹cy funkcje:
## funkcja 1: rejestracja nowego klienta lub usuwanie danych klienta z bazy
## funkcja 2: dodawanie (przez administratora) danych
## nowego klienta do bazy tj. do pliku customer.csv i address.csv
## Nowy klient podaje swoje dane (imie, nazwisko), nadawany jest w/w klientowi losowy numer ID z³o¿ony z 4 cyfr
## w folderze DATABASE tworzony jest plik tekstowy (nazwa pliku to ID klienta)
## do którego bêd¹ zapisywane dane wypo¿yczonej przez klienta ksi¹¿ki oraz
## data wypo¿yczenia a potem zwrotu ksi¹¿ki
## funkcja 3: usuwanie danych klienta opcje: wzglêdem ID lub NAME
## Wypo¿yczanie ksi¹¿ki/-ek przez u¿ytkownika 2 funkcje:
## funkcja 4: wypo¿yczenie ksi¹¿ki lub kilku ksi¹¿ek przez klienta
## funkcja 5: zwrot 1 ksi¹¿ki przez klienta
##
## Jeœli skoñczy³eœ zadanie, przyjmij rolê kolejnego programisty
## który dosta³ zadanie aktualizacji Twojego oprogramowania
## Nie modyfikuj¹c i nie zmieniaj¹c nazwy funkcji "udekoruj"
# funkcja nr 5: "zwrot 1 ksi¹¿ki przez klienta" i nadpisz jej zawartoœæ
## tak aby klient mia³ mo¿liwoœæ zwrotu dowolnej liczby ksi¹¿ek

## WYMAGANIA:
## - mo¿esz programowaæ wy³¹cznie w paradygmacie funkcyjnym
## - utwórz funkcjê wy¿szego rzêdu
## - utwórz funkcjê wielu zmiennych wejœciowych
## - utwórz funkcjê zagnie¿dzon¹
## - u¿yj dekoratora
## - wykonaj dokumentacjê dla conajmniej 1 funkcji i 1 modu³u
## - conajmniej dla 2 funkcji wykonaj obs³ugê wyj¹tków  (dotyczy modu³ów 2-4)

## WSKAZANIA:
## - mo¿esz zwiêkszyæ liczbê modu³ów
## - dla zapisu/odczytu daty oraz danych do bazy wykorzystaj odpowiednie pakiety

