def je_prvocislo(cislo):
    trueFalse = 0
    cislo = int(cislo)
    odmocnina = cislo ** 0.5

    scale_List = range(2, int(odmocnina + 1))

    for number in scale_List:
        if cislo % number == 0:
            trueFalse += 1

    if trueFalse > 0:
        return False
    if trueFalse == 0:
        return True

def vrat_prvocislo(cislo):
    cislo = int(cislo)
    scale_list = range(2, cislo + 1)
    seznam_Cisel = []

    for number in scale_list:
        if je_prvocislo(number):
            seznam_Cisel.append(number)

    return seznam_Cisel


if __name__ == "__main__":
    print("1) Zjisti, zda je číslo prvočíslem")
    print("2) Vrať všechna čísla v rozsahu 0 - zadané číslo.")
    menu = input("Zvolte možnost: ")

    if menu == "1":
        cislo = input("Zadej číslo: ")
        vysledek = je_prvocislo(cislo)
        if vysledek:
            print("Ćíslo je prvočíslo.")
        else:
            print("Číslo není prvočíslo.")
    elif menu == "2":
        cislo = input("Zadej horní hranici: ")
        print(vrat_prvocislo(cislo))
    else:
        print("Chybný formát odpovědi..")
