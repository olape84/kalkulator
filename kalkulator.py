import logging 
input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")
action=input()
input("podaj skladnik 1")
element1=input()
input("podaj składnik 2")
element2=input()
if action == 1:
       logging.info(f"Dodaję {element1} i {element2}")
       print(f"Wynik to {element1 + element2}")
elif  action==2:
       logging.info(f"Odejmmuję od {element1} {element2}")
       print(f"Wynik to {element1-element2}")
elif action ==3:
       logging.info(f"Mnożę {element1} i {element2}")
       print(f"Wynik to {element1*element2}")
elif action ==4:
       logging.info(f"Dzielę {element1} przez {element2}")
       print(f"Wynik to {element1/element2}")
