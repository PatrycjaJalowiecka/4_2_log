def kalkulator():
    import logging
    logging.basicConfig(level=logging.DEBUG)

    print("Witaj, oto Twój kalkulator. Podaj działani e, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    działanie = int(input(""))
    print("Podaj liczby, na których chcesz wykonać działania")
    liczba1 = float(input(""))
    liczba2 = float(input(""))
    if działanie == 1:
        print("Może chcesz dodać więcej liczb T/N?")
        YN = input("")
        if YN == "T":
            print("Podaj 3 dodatkowe liczby")
            liczba3 = float(input(""))
            liczba4 = float(input(""))
            liczba5 = float(input(""))
            logging.info("Dodawanie %s, %s, %s. %s. %s" % (liczba1, liczba2, liczba3, liczba4, liczba5))
            result = (liczba1 + liczba2 + liczba3 + liczba4 + liczba5)
            print(result)
        elif YN == "N":
            logging.info("Dodawanie %s i %s" % (liczba1, liczba2))
            result = (liczba1 + liczba2)
            print(result)
        else:
            print("Niewłaściwe parametry")
            exit(1)  
    elif działanie == 2:
        logging.info("Odejmowanie %s od %s" % (liczba2, liczba1))
        result = (liczba1 - liczba2)
        print(result)
    elif działanie == 3:
        print("Może chcesz pomnożyć więcej liczb T/N?")
        YN = input("")
        if YN == "T":
            print("Podaj 3 dodatkowe liczby. Jeżeli chcesz użyć mniej niż trzech, wstaw 1")
            liczba3 = float(input(""))
            liczba4 = float(input(""))
            liczba5 = float(input(""))
            logging.info("Mnożenie %s, %s, %s, %s, %s" % (liczba1, liczba2, liczba3, liczba4, liczba5))
            result = (liczba1 * liczba2 * liczba3 * liczba4 * liczba5)
            print(result)
        elif YN == "N":
            logging.info("Mnożenie %s i %s" % (liczba1, liczba2))
            result = (liczba1 * liczba2)
            print(result)
        else:
            print("Niewłaściwe parametry")
            exit(1)    
    elif działanie == 4:
        if liczba2 == 0:
            logging.warning("Nie można dzielić przez 0. Wybierz inną liczbę")
            liczba2 = float(input(""))
            if liczba2 !=0:
                logging.info("Dzielenie %s przez %s" % (liczba1, liczba2))
                result = (liczba1 / liczba2)
                print(result)
            else: 
                  logging.warning("Błąd dzielenia przez 0. Uruchom ponownie kalkulator")
                exit(1)
        else: liczba2 != 0:   
            logging.info("Dzielenie %s przez %s" % (liczba1, liczba2))
            result = (liczba1 / liczba2)
            print(result)
    else:
        print("Niewłaściwe parametry")
        exit(1) 

    logging.debug("Aby skorzystać z kalkulatora, uruchom ponownie funkcję") 

kalkulator()