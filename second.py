def cislo_text(cislo):
    cislo = int(cislo)



    if cislo > 20 and cislo < 100:
        desitky = cislo//10
        prvni_cislo = {2: "Dvacet", 3: "Třicet", 4:"Čtyřicet", 5:"Padesát", 6:"Šedesát", 7:"Sedmdesát", 8:"Osmdesát", 9:"Devadesát"}

        jednotky = cislo%10
        druhe_cislo = {2: "dva", 3: "tři", 4:"čtyři", 5:"pět", 6:"šest", 7:"sedm", 8:"osm", 9:"devět"}
        
        return prvni_cislo[desitky] + druhe_cislo[jednotky]

    
    if cislo == 0:
        print("Nula")

    if cislo == 100:
        print("Sto")

    if cislo > 0 and cislo < 10:
        prvni_cislo = {1: "Jedna", 2: "Dva", 3: "Tři", 4:"Čtyři", 5:"Pět", 6:"Šest", 7:"Sedm", 8:"Osm", 9:"Devět"}
        return prvni_cislo[cislo]

    if cislo > 10 and cislo < 20:
        dvojcisli = {11: "Jedenáct", 12: "Dvanáct", 13: "Třináct", 14: "Čtrnáct", 15: "Patnáct", 16:"Šestnáct", 17: "Sedmnáct", 18:"Osmnáct", 19: "Devatenáct"}
        return dvojcisli[cislo]




if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
