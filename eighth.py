def bin_to_dec(binarni_cislo):
    # Funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int)
    # 111 -> 7
    # "101" -> 5

    vysledek = 0
    hodnota_binu = 1

    cislo = ''.join(reversed(str(binarni_cislo)))

    for e in cislo:
        if e == "1":
            vysledek += hodnota_binu
        hodnota_binu *= 2

    return vysledek

def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

print(test_bin_to_dec())

