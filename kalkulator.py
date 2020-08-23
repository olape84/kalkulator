import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kalkulator") 

if __name__ == "__main__":
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")
    action=input()
    print("podaj skladnik 1 ")
    element1=float(input())
    print("podaj składnik 2 ")
    element2=float(input())
    if action == '1':
       logger.info(f"Dodaję {element1} i {element2}")
       print(f"Wynik to {(element1 + element2):.2f}")
    elif  action=='2':
       logger.info(f"Odejmmuję od {element1} {element2}")
       print(f"Wynik to {element1-element2:.2f}")
    elif action =='3':
       logger.info(f"Mnożę {element1} i {element2}")
       print(f"Wynik to {element1*element2:.2f}")
    elif action =='4':
       logger.info(f"Dzielę {element1} przez {element2}")
       print(f"Wynik to {element1/element2:.2f}")

