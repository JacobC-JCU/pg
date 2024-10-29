def je_prvocislo():
    cislo = input("Zadej číslo: ")
    trueFalse = 0
    cislo = int(cislo)
    odmocnina = cislo ** 0.5

    scale_List = range(2, int(odmocnina + 1))

    for number in scale_List:
        if cislo % number == 0:
            trueFalse += 1

    if trueFalse > 0:
        print("Ćíslo není prvočíslo.")
    if trueFalse == 0:
        print("Číslo je prvočíslo.")

def vrat_prvocislo():
    cislo = input("Zadej horní rozsah: ")
    cislo = int(cislo)

    scale_list = range(2, cislo + 1)
    seznam_Cisel = []


    for number in scale_list:
        prvocislo = True

        for odmocnitel in range(2, int(number ** 0.5) + 1):
            if number % odmocnitel == 0:
                prvocislo = False
                continue

        if prvocislo:
            seznam_Cisel.append(number)
    print(seznam_Cisel)


if __name__ == "__main__":
    print("1) Zjisti, zda je číslo prvočíslem")
    print("2) Vrať všechna čísla v rozsahu 0 - zadané číslo.")
    menu = input("Zvolte možnost: ")

    if menu == "1":
        je_prvocislo()
    elif menu == "2":
        vrat_prvocislo()
    else:
        print("Chybný formát odpovědi..")

