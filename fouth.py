def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.
    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    :return: True, pokud je tah možný, jinak False.
    """
    # Podmínky pro jednotlivé úseky
    podminka1 = 1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8
    podminka2 = cilova_pozice not in obsazene_pozice
    podminka3 = True
    podminka4 = True

    # Pěšec
    if figurka["typ"] == "pěšec":
        if figurka["pozice"][0] == 2:
            x = 2
        else:
            x = 1
        podminka3 = figurka["pozice"][0] < cilova_pozice[0] <= figurka["pozice"][0] + x

    # Jezdec
    elif figurka["typ"] == "jezdec":
        osa1 = abs(cilova_pozice[0] - figurka["pozice"][0])
        osa2 = abs(cilova_pozice[1] - figurka["pozice"][1])
        podminka3 = (osa1 == 2 and osa2 == 1) or (osa1 == 1 and osa2 == 2)


    # Královna
    elif figurka["typ"] == "dáma":
        # Kontrola vertikálního pohybu
        if cilova_pozice[0] == figurka["pozice"][0]:
            podminka3 = True
            min0, max0 = sorted([cilova_pozice[1], figurka["pozice"][1]])
            for i in range(min0 + 1, max0):
                if (cilova_pozice[0], i) in obsazene_pozice:
                    podminka4 = False

        # Kontrola horizontálního pohybu
        elif cilova_pozice[1] == figurka["pozice"][1]:
            podminka3 = True
            min0, max0 = sorted([cilova_pozice[0], figurka["pozice"][0]])
            for i in range(min0 + 1, max0):
                if (i, cilova_pozice[1]) in obsazene_pozice:
                    podminka4 = False

        # Kontrola diagonálního pohybu
        elif abs(figurka["pozice"][0] - cilova_pozice[0]) == abs(figurka["pozice"][1] - cilova_pozice[1]):
            podminka3 = True
            min0, max0 = sorted([cilova_pozice[0], figurka["pozice"][0]])
            min1, max1 = sorted([cilova_pozice[1], figurka["pozice"][1]])
            for i, j in zip(range(min0 + 1, max0), range(min1 + 1, max1)):
                if (i, j) in obsazene_pozice:
                    podminka4 = False
        else:
            podminka3 = False

    # Věž
    elif figurka["typ"] == "věž":
        # Kontrola vertiálního pohybu
        if cilova_pozice[0] == figurka["pozice"][0]:
            podminka3 = True
            min0, max0 = sorted([cilova_pozice[1], figurka["pozice"][1]])
            for i in range(min0 + 1, max0):
                if (cilova_pozice[0], i) in obsazene_pozice:
                    podminka4 = False

         # Kontrola horizontálního pohybu
        elif cilova_pozice[1] == figurka["pozice"][1]:
            podminka3 = True
            min0, max0 = sorted([cilova_pozice[0], figurka["pozice"][0]])
            for i in range(min0 + 1, max0):
                if (i, cilova_pozice[1]) in obsazene_pozice:
                    podminka4 = False
        else:
            podminka3 = False


    # Král
    elif figurka["typ"] == "král":
        # Kontrola vertikálního pohybu
        if cilova_pozice[0] == figurka["pozice"][0] and abs(cilova_pozice[0] - figurka["pozice"][0] <= 1):
            podminka3 = True
            min0, max0 = sorted([cilova_pozice[1], figurka["pozice"][1]])
            for i in range(min0 + 1, max0):
                if (cilova_pozice[0], i) in obsazene_pozice:
                    podminka4 = False

        # Kontrola horizontálního pohybu
        elif cilova_pozice[1] == figurka["pozice"][1] and abs(cilova_pozice[0] - figurka["pozice"][0] <= 1):
            podminka3 = True
            min0, max0 = sorted([cilova_pozice[0], figurka["pozice"][0]])
            for i in range(min0 + 1, max0):
                if (i, cilova_pozice[1]) in obsazene_pozice:
                    podminka4 = False

        # Kontrola diagonálního pohybu
        if abs(cilova_pozice[0] - figurka["pozice"][0]) <= 1 and abs(cilova_pozice[1] - figurka["pozice"][1]) <= 1:
            podminka3 = True
            min0, max0 = sorted([cilova_pozice[0], figurka["pozice"][0]])
            min1, max1 = sorted([cilova_pozice[1], figurka["pozice"][1]])
            for i, j in zip(range(min0 + 1, max0), range(min1 + 1, max1)):
                if (i, j) in obsazene_pozice:
                    podminka4 = False

        else:
            podminka3 = False

        
                    #    print(je_tah_mozny(kral, (3, 4), obsazene_pozice))  True?
                    #    kral = {"typ": "král", "pozice": (1, 4)}


    # Střelec
    elif figurka["typ"] == "střelec":
        # Kontrola diaonálního pohybu
        if abs(figurka["pozice"][0] - cilova_pozice[0]) == abs(figurka["pozice"][1] - cilova_pozice[1]):
            podminka3 = True
            min0, max0 = sorted([cilova_pozice[0], figurka["pozice"][0]])
            min1, max1 = sorted([cilova_pozice[1], figurka["pozice"][1]])
            for i, j in zip(range(min0 + 1, max0), range(min1 + 1, max1)):
                if (i, j) in obsazene_pozice:
                    podminka4 = False

        else:
            podminka3 = False

    # Pokud všechno True, vrací True, v opačném případě False
    return f"Tah figurkou {figurka["typ"]} z pozice {figurka["pozice"]} na pozici {cilova_pozice} je {podminka1 and podminka2 and podminka3 and podminka4}"


# Testing the function
if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True  


